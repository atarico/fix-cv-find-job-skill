#!/usr/bin/env python3
"""Regenerate the pandoc reference document used to render CVs.

Pandoc's stock reference.docx is styled for reports: one-inch margins, 12pt
body, oversized headings. A CV rendered with it runs to three or four pages.
This script rebuilds it with CV-appropriate metrics so a two-page CV actually
fits on two pages without shrinking the font below readable size.

Three things about pandoc's default that the obvious implementation gets wrong:

* Its ``sectPr`` carries no ``pgMar`` and no ``pgSz``. Margins have to be
  INSERTED, not substituted, and depending on the pandoc version the element is
  either ``<w:sectPr />`` (self-closing, pandoc <= 3.1) or ``<w:sectPr>...
  </w:sectPr>`` with children (later releases). A naive "insert after the
  opening tag" puts ``pgMar`` *next to* a self-closing ``sectPr`` instead of
  inside it, which is silently ignored -- and the CV comes out with one-inch
  margins again. Both shapes are handled below.
* Without an explicit ``pgSz`` the renderer picks the page size from its
  locale (Letter in en-US, A4 almost everywhere else), so the two-page gate in
  ``references/02-master-cv.md`` would pass on one machine and fail on another.
  The page size is now pinned (A4 by default, ``--page letter`` to change it).
* Several styles carry no ``w:sz`` at all, so sizes likewise have to be
  inserted rather than replaced -- including in ``docDefaults``, where a
  prepended size next to the existing one leaves two ``w:sz`` elements in the
  same ``rPr``, which is invalid OOXML and lets the 12pt default win.

Pandoc's default also paints Title, Heading 1-9 and Hyperlink in theme blue.
The CV phase promises the Harvard style -- black and white -- so every run
colour is stripped and the inspection below refuses a template that carries
one.

Two more things vary with the pandoc version and are pinned here rather than
inherited. pandoc <= 3.1 makes headings bold; pandoc 3.9 does not, and tells
them apart by colour alone -- strip the colour and a heading looks like body
text. So bold is forced on Title, Subtitle and Heading 1-6. And the default
theme fonts moved from Calibri/Cambria (metric-compatible Carlito/Caladea ship
with LibreOffice, so the page count is the same everywhere) to Aptos, which has
no metric-compatible substitute and falls back to DejaVu Sans on Linux, wider
by enough to push a full second page onto a third. So every theme font
reference is removed and one explicit font is set as the document default.

Usage:
    python3 scripts/make-reference-docx.py            # rewrite the shipped asset
    python3 scripts/make-reference-docx.py --out X    # write somewhere else
    python3 scripts/make-reference-docx.py --page letter

Writes: skills/fix-cv-find-job-skill/assets/reference.docx (unless --out).
The result is inspected after writing; the script fails if any metric did not
land, so a broken template never gets committed silently.
``tests/test_reference_docx.py`` runs the same inspection plus a real
markdown -> docx -> pdf render.
"""

from __future__ import annotations

import argparse
import io
import pathlib
import re
import subprocess
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "skills" / "fix-cv-find-job-skill" / "assets" / "reference.docx"

# styleId -> (size in half-points, space before, space after) in twips
# In a CV written as "# Name / ## Section / ### Role", Heading 1 is the name:
# it gets a name's size, not a section's. Title/Subtitle only apply when the
# name is passed as pandoc metadata instead, and are kept in step with it.
STYLES = [
    ("Title", 28, 0, 40),
    ("Subtitle", 22, 0, 60),
    ("Heading1", 28, 0, 40),
    ("Heading2", 21, 140, 40),
    ("Heading3", 20, 120, 40),
    ("Heading4", 20, 100, 40),
    ("Heading5", 20, 80, 40),
    ("Heading6", 20, 80, 40),
    ("BodyText", 20, 0, 60),
    ("Compact", 20, 0, 40),
    ("FirstParagraph", 20, 0, 60),
    ("SourceCode", 18, 0, 40),
]

BODY_SIZE_HP = 20  # 10pt document default, single spaced
MARGIN_TWIPS = 720  # half an inch on every side

# One explicit font for the whole document, in place of pandoc's theme fonts.
# Calibri renders as itself on Windows/macOS and as the metric-compatible
# Carlito on Linux (shipped with LibreOffice), so line breaks and page count
# are identical everywhere. ATS-safe, and what most CVs already use.
BODY_FONT = "Calibri"
# Styles that must stand out from body text by weight, since colour is gone.
BOLD_STYLES = ("Title", "Subtitle", "Heading1", "Heading2", "Heading3", "Heading4", "Heading5", "Heading6")

# width x height in twips
PAGE_SIZES = {
    "a4": (11906, 16838),
    "letter": (12240, 15840),
}
DEFAULT_PAGE = "a4"

PGMAR = (
    '<w:pgMar w:top="{m}" w:right="{m}" w:bottom="{m}" w:left="{m}" '
    'w:header="360" w:footer="360" w:gutter="0"/>'
).format(m=MARGIN_TWIPS)


# --------------------------------------------------------------------------- #
# styles.xml
# --------------------------------------------------------------------------- #

def _size_runs(size_hp: int) -> str:
    return f'<w:sz w:val="{size_hp}"/><w:szCs w:val="{size_hp}"/>'


def _strip_sizes(xml: str) -> str:
    xml = re.sub(r'<w:sz\b[^>]*/>', "", xml)
    return re.sub(r'<w:szCs\b[^>]*/>', "", xml)


def force_rpr(block: str, size_hp: int) -> str:
    """Ensure a <w:style> block's run properties carry exactly our size.

    Existing sizes are removed first, so the result never carries two ``w:sz``
    elements. When the style has no ``rPr`` at all, one is appended before
    ``</w:style>`` -- the position the schema puts it in (after ``pPr``).
    """
    block = _strip_sizes(block)
    sz = _size_runs(size_hp)
    if re.search(r"<w:rPr\s*/>", block):
        return re.sub(r"<w:rPr\s*/>", "<w:rPr>" + sz + "</w:rPr>", block, count=1)
    if "<w:rPr>" in block:
        return block.replace("<w:rPr>", "<w:rPr>" + sz, 1)
    return block.replace("</w:style>", "<w:rPr>" + sz + "</w:rPr></w:style>", 1)


def force_spacing(block: str, before: int, after: int) -> str:
    """Ensure a <w:style> block's paragraph properties carry our spacing."""
    spacing = (
        f'<w:spacing w:before="{before}" w:after="{after}" '
        'w:line="240" w:lineRule="auto"/>'
    )
    block = re.sub(r"<w:spacing\b[^>]*/>", "", block)
    if re.search(r"<w:pPr\s*/>", block):
        return re.sub(r"<w:pPr\s*/>", "<w:pPr>" + spacing + "</w:pPr>", block, count=1)
    if "<w:pPr>" in block:
        return block.replace("<w:pPr>", "<w:pPr>" + spacing, 1)
    ppr = "<w:pPr>" + spacing + "</w:pPr>"
    # Schema order inside <w:style>: ... qFormat, pPr, rPr. Put pPr right
    # before an existing rPr, else at the end of the style.
    if "<w:rPr" in block:
        return re.sub(r"<w:rPr\b", ppr + "<w:rPr", block, count=1)
    return block.replace("</w:style>", ppr + "</w:style>", 1)


def force_doc_defaults(styles: str, size_hp: int) -> str:
    """Set the document-default run size, replacing rather than duplicating."""
    m = re.search(r"<w:rPrDefault>.*?</w:rPrDefault>", styles, re.S)
    if not m:
        block = "<w:rPrDefault><w:rPr>" + _size_runs(size_hp) + "</w:rPr></w:rPrDefault>"
        return styles.replace("<w:docDefaults>", "<w:docDefaults>" + block, 1)
    block = _strip_sizes(m.group(0))
    if re.search(r"<w:rPr\s*/>", block):
        block = re.sub(r"<w:rPr\s*/>", "<w:rPr>" + _size_runs(size_hp) + "</w:rPr>", block, count=1)
    elif "<w:rPr>" in block:
        block = block.replace("<w:rPr>", "<w:rPr>" + _size_runs(size_hp), 1)
    else:
        block = block.replace("</w:rPrDefault>", "<w:rPr>" + _size_runs(size_hp) + "</w:rPr></w:rPrDefault>", 1)
    return styles[: m.start()] + block + styles[m.end():]


def strip_colour(styles: str) -> str:
    """Drop every run colour so headings and links render black.

    pandoc's default paints Title, Heading 1-9, Hyperlink and a few others in
    theme blue. The CV phase promises the Harvard style -- black and white --
    so no style may carry a colour; text then inherits the automatic (black)
    colour. Underlines and weights are untouched.
    """
    return re.sub(r"<w:color\b[^>]*/>", "", styles)


def force_bold(block: str) -> str:
    """Ensure a <w:style> block's run properties carry bold (once)."""
    block = re.sub(r"<w:b\s*/>", "", block)
    block = re.sub(r"<w:bCs\s*/>", "", block)
    bold = "<w:b/><w:bCs/>"
    if re.search(r"<w:rPr\s*/>", block):
        return re.sub(r"<w:rPr\s*/>", "<w:rPr>" + bold + "</w:rPr>", block, count=1)
    if "<w:rPr>" in block:
        return block.replace("<w:rPr>", "<w:rPr>" + bold, 1)
    return block.replace("</w:style>", "<w:rPr>" + bold + "</w:rPr></w:style>", 1)


def pin_font(styles: str, font: str) -> str:
    """Replace every theme font reference with one explicit font.

    Theme fonts are resolved through theme1.xml, whose contents change between
    pandoc releases (Calibri/Cambria up to 3.1, Aptos in 3.9). Removing every
    ``rFonts`` that points at the theme and setting one explicit family in
    ``docDefaults`` makes the rendered font -- and therefore the page count --
    independent of the pandoc that built the template.
    """
    styles = re.sub(r'<w:rFonts\b[^>]*Theme="[^"]*"[^>]*/>', "", styles)
    rfonts = '<w:rFonts w:ascii="{f}" w:hAnsi="{f}" w:cs="{f}" w:eastAsia="{f}"/>'.format(f=font)
    m = re.search(r"<w:rPrDefault>.*?</w:rPrDefault>", styles, re.S)
    block = m.group(0)
    block = re.sub(r"<w:rFonts\b[^>]*/>", "", block)
    if re.search(r"<w:rPr\s*/>", block):
        block = re.sub(r"<w:rPr\s*/>", "<w:rPr>" + rfonts + "</w:rPr>", block, count=1)
    else:
        block = block.replace("<w:rPr>", "<w:rPr>" + rfonts, 1)
    return styles[: m.start()] + block + styles[m.end():]


def restyle(styles: str) -> str:
    for style_id, size_hp, before, after in STYLES:
        match = re.search(
            r'<w:style [^>]*w:styleId="%s".*?</w:style>' % style_id, styles, re.S
        )
        if not match:
            continue
        block = force_spacing(force_rpr(match.group(0), size_hp), before, after)
        if style_id in BOLD_STYLES:
            block = force_bold(block)
        styles = styles.replace(match.group(0), block, 1)
    styles = force_doc_defaults(styles, BODY_SIZE_HP)
    styles = pin_font(styles, BODY_FONT)
    return strip_colour(styles)


# --------------------------------------------------------------------------- #
# document.xml
# --------------------------------------------------------------------------- #

# Children that the schema puts BEFORE pgSz/pgMar inside <w:sectPr>.
_SECT_LEADERS = ("headerReference", "footerReference", "footnotePr", "endnotePr", "type")


def force_sect_pr(document: str, page: str) -> str:
    """Pin page size and margins inside the body's section properties.

    Handles a self-closing ``<w:sectPr />`` (pandoc <= 3.1), a populated
    ``<w:sectPr>...</w:sectPr>`` (later pandoc), and a body with no ``sectPr``
    at all. Any existing ``pgSz``/``pgMar`` is replaced.
    """
    width, height = PAGE_SIZES[page]
    pgsz = f'<w:pgSz w:w="{width}" w:h="{height}"/>'
    document = re.sub(r"<w:pgSz\b[^>]*/>", "", document)
    document = re.sub(r"<w:pgMar\b[^>]*/>", "", document)

    self_closing = re.search(r"<w:sectPr\b[^>]*/>", document)
    if self_closing:
        return document.replace(
            self_closing.group(0), "<w:sectPr>" + pgsz + PGMAR + "</w:sectPr>", 1
        )

    populated = re.search(r"<w:sectPr\b[^>]*>(.*?)</w:sectPr>", document, re.S)
    if not populated:
        return document.replace(
            "</w:body>", "<w:sectPr>" + pgsz + PGMAR + "</w:sectPr></w:body>", 1
        )

    inner = populated.group(1)
    anchor = 0
    for tag in _SECT_LEADERS:
        pattern = r"<w:%s\b[^>]*/>|<w:%s\b[^>]*>.*?</w:%s>" % (tag, tag, tag)
        for m in re.finditer(pattern, inner, re.S):
            anchor = max(anchor, m.end())
    new_inner = inner[:anchor] + pgsz + PGMAR + inner[anchor:]
    return document[: populated.start(1)] + new_inner + document[populated.end(1):]


# --------------------------------------------------------------------------- #
# inspection -- shared with tests/test_reference_docx.py
# --------------------------------------------------------------------------- #

def inspect(path: pathlib.Path) -> dict:
    """Read back the metrics that matter from a reference.docx."""
    with zipfile.ZipFile(path) as z:
        styles = z.read("word/styles.xml").decode("utf-8")
        document = z.read("word/document.xml").decode("utf-8")

    result: dict = {"styles": {}, "problems": []}

    sect = re.search(r"<w:sectPr\b[^>]*>(.*?)</w:sectPr>", document, re.S)
    inner = sect.group(1) if sect else ""
    pgmar = re.search(r'<w:pgMar\b[^>]*/>', inner)
    pgsz = re.search(r'<w:pgSz\b[^>]*/>', inner)
    result["pgMar"] = (
        {k: int(v) for k, v in re.findall(r'w:(top|right|bottom|left)="(\d+)"', pgmar.group(0))}
        if pgmar else None
    )
    result["pgSz"] = (
        {k: int(v) for k, v in re.findall(r'w:(w|h)="(\d+)"', pgsz.group(0))}
        if pgsz else None
    )
    stray = re.findall(r"<w:pgMar\b[^>]*/>", document)
    if len(stray) != 1 or not pgmar:
        result["problems"].append(
            "pgMar is missing from sectPr or appears outside it (%d found in document)" % len(stray)
        )
    if not pgsz:
        result["problems"].append("pgSz missing from sectPr")
    if result["pgMar"] and any(v != MARGIN_TWIPS for v in result["pgMar"].values()):
        result["problems"].append("pgMar is not %d twips on every side: %r" % (MARGIN_TWIPS, result["pgMar"]))

    coloured = [
        m.group(1)
        for m in re.finditer(r'<w:style [^>]*w:styleId="([^"]+)".*?</w:style>', styles, re.S)
        if re.search(r"<w:color\b", m.group(0))
    ]
    result["coloured_styles"] = coloured
    if coloured:
        result["problems"].append(
            "Harvard style is black and white, but these styles carry a colour: %s" % ", ".join(coloured)
        )

    not_bold = []
    for sid in BOLD_STYLES:
        m = re.search(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % sid, styles, re.S)
        if m and not re.search(r"<w:b\s*/>", m.group(0)):
            not_bold.append(sid)
    result["unbold_headings"] = not_bold
    if not_bold:
        result["problems"].append(
            "with colour gone, headings must be bold to stand out from body text; these are not: %s" % ", ".join(not_bold)
        )

    theme_fonts = re.findall(r'<w:rFonts\b[^>]*Theme="[^"]*"[^>]*/>', styles)
    rpr_default = re.search(r"<w:rPrDefault>.*?</w:rPrDefault>", styles, re.S)
    default_font = re.search(r'<w:rFonts\b[^>]*w:ascii="([^"]+)"', rpr_default.group(0)) if rpr_default else None
    result["font"] = default_font.group(1) if default_font else None
    if theme_fonts:
        result["problems"].append(
            "%d theme font reference(s) remain; the rendered font would depend on pandoc's theme" % len(theme_fonts)
        )
    if result["font"] != BODY_FONT:
        result["problems"].append("document default font is %r, expected %r" % (result["font"], BODY_FONT))

    sizes = re.findall(r'<w:sz w:val="(\d+)"', rpr_default.group(0)) if rpr_default else []
    result["docDefaults_sz"] = [int(s) for s in sizes]
    if result["docDefaults_sz"] != [BODY_SIZE_HP]:
        result["problems"].append(
            "docDefaults should carry exactly one w:sz=%d, has %r" % (BODY_SIZE_HP, result["docDefaults_sz"])
        )

    for style_id, size_hp, before, after in STYLES:
        m = re.search(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % style_id, styles, re.S)
        if not m:
            result["styles"][style_id] = None  # pandoc's default has no such style; fine
            continue
        block = m.group(0)
        got_sz = [int(s) for s in re.findall(r'<w:sz w:val="(\d+)"', block)]
        sp = re.search(r'<w:spacing\b[^>]*/>', block)
        got_before = int(re.search(r'w:before="(\d+)"', sp.group(0)).group(1)) if sp else None
        got_after = int(re.search(r'w:after="(\d+)"', sp.group(0)).group(1)) if sp else None
        result["styles"][style_id] = {"sz": got_sz, "before": got_before, "after": got_after}
        if got_sz != [size_hp]:
            result["problems"].append("%s: expected one w:sz=%d, got %r" % (style_id, size_hp, got_sz))
        if (got_before, got_after) != (before, after):
            result["problems"].append(
                "%s: expected spacing before=%d after=%d, got %r/%r" % (style_id, before, after, got_before, got_after)
            )
    return result


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def build(out: pathlib.Path, page: str = DEFAULT_PAGE) -> pathlib.Path:
    default = subprocess.run(
        ["pandoc", "--print-default-data-file", "reference.docx"],
        capture_output=True, check=True,
    ).stdout
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(default)) as zin:
        items = {n: zin.read(n) for n in zin.namelist()}

    items["word/styles.xml"] = restyle(items["word/styles.xml"].decode("utf-8")).encode("utf-8")
    items["word/document.xml"] = force_sect_pr(
        items["word/document.xml"].decode("utf-8"), page
    ).encode("utf-8")

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in items.items():
            zout.writestr(name, data)
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", type=pathlib.Path, default=DEFAULT_OUT,
                        help="where to write the reference document (default: the shipped asset)")
    parser.add_argument("--page", choices=sorted(PAGE_SIZES), default=DEFAULT_PAGE,
                        help="page size to pin (default: %s)" % DEFAULT_PAGE)
    args = parser.parse_args(argv)

    out = build(args.out, args.page)
    report = inspect(out)
    try:
        shown = out.relative_to(ROOT)
    except ValueError:
        shown = out
    if report["problems"]:
        print("wrote %s, but it is NOT usable:" % shown, file=sys.stderr)
        for p in report["problems"]:
            print("  - " + p, file=sys.stderr)
        return 1
    print("wrote %s (page=%s, margins=%d twips, body=%dpt)" % (
        shown, args.page, MARGIN_TWIPS, BODY_SIZE_HP // 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
