#!/usr/bin/env python3
"""Regenerate the pandoc reference document used to render CVs.

Pandoc's stock reference.docx is styled for reports: one-inch margins, 12pt
body, oversized headings. A CV rendered with it runs to four pages. This script
rebuilds it with CV-appropriate metrics so a two-page CV actually fits on two
pages without shrinking the font below readable size.

Two things about pandoc's default that the obvious implementation gets wrong:
its sectPr carries no `pgMar` element at all, so margins have to be INSERTED
rather than substituted; and several styles carry no `w:sz`, so sizes likewise
have to be inserted rather than replaced.

Usage: python3 scripts/make-reference-docx.py
Writes: skills/fix-cv-find-job-skill/assets/reference.docx
"""

import pathlib
import re
import subprocess
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "skills" / "fix-cv-find-job-skill" / "assets" / "reference.docx"

# styleId -> (size in half-points, space before, space after) in twips
STYLES = [
    ("Title", 32, 0, 40),
    ("Subtitle", 22, 0, 60),
    ("Heading1", 22, 160, 60),
    ("Heading2", 21, 140, 40),
    ("Heading3", 20, 120, 40),
    ("Heading4", 20, 100, 40),
    ("BodyText", 20, 0, 60),
    ("Compact", 20, 0, 40),
    ("FirstParagraph", 20, 0, 60),
    ("SourceCode", 18, 0, 40),
]

MARGIN_TWIPS = 720  # half an inch
PGMAR = (
    '<w:pgMar w:top="{m}" w:right="{m}" w:bottom="{m}" w:left="{m}" '
    'w:header="360" w:footer="360" w:gutter="0"/>'
).format(m=MARGIN_TWIPS)


def force_rpr(block: str, size_hp: int) -> str:
    """Ensure the style's run properties carry our size, inserting if absent."""
    sz = f'<w:sz w:val="{size_hp}"/><w:szCs w:val="{size_hp}"/>'
    block = re.sub(r'<w:sz w:val="\d+"\s*/>', "", block)
    block = re.sub(r'<w:szCs w:val="\d+"\s*/>', "", block)
    if "<w:rPr>" in block:
        return block.replace("<w:rPr>", "<w:rPr>" + sz, 1)
    return block.replace("</w:pPr>", "</w:pPr><w:rPr>" + sz + "</w:rPr>", 1)


def force_spacing(block: str, before: int, after: int) -> str:
    spacing = (
        f'<w:spacing w:before="{before}" w:after="{after}" '
        'w:line="240" w:lineRule="auto"/>'
    )
    block = re.sub(r"<w:spacing[^/]*/>", "", block)
    if "<w:pPr>" in block:
        return block.replace("<w:pPr>", "<w:pPr>" + spacing, 1)
    return block.replace("<w:name", "<w:pPr>" + spacing + "</w:pPr><w:name", 1)


def main() -> None:
    default = subprocess.run(
        ["pandoc", "--print-default-data-file", "reference.docx"],
        capture_output=True, check=True,
    ).stdout
    tmp = OUT.parent / ".reference-default.docx"
    tmp.write_bytes(default)

    with zipfile.ZipFile(tmp) as zin:
        items = {n: zin.read(n) for n in zin.namelist()}
    tmp.unlink()

    styles = items["word/styles.xml"].decode("utf-8")
    for style_id, size_hp, before, after in STYLES:
        match = re.search(
            r'<w:style [^>]*w:styleId="%s".*?</w:style>' % style_id, styles, re.S
        )
        if not match:
            continue
        block = force_spacing(force_rpr(match.group(0), size_hp), before, after)
        styles = styles.replace(match.group(0), block)

    # 10pt single-spaced document default
    styles = re.sub(
        r"(<w:docDefaults>.*?<w:rPr>)",
        r'\g<1><w:sz w:val="20"/><w:szCs w:val="20"/>',
        styles, count=1, flags=re.S,
    )
    items["word/styles.xml"] = styles.encode("utf-8")

    document = items["word/document.xml"].decode("utf-8")
    if "pgMar" in document:
        document = re.sub(r"<w:pgMar[^>]*/>", PGMAR, document)
    else:
        document = re.sub(r"(<w:sectPr[^>]*>)", r"\g<1>" + PGMAR, document, count=1)
    items["word/document.xml"] = document.encode("utf-8")

    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in items.items():
            zout.writestr(name, data)

    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
