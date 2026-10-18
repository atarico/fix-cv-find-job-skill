#!/usr/bin/env python3
"""Build the conversation histories the phase 2 eval cases resume from.

Phase 1 ends by asking the applicant questions, so a phase 2 case cannot start
from a single prompt: it resumes a conversation that already holds the CV, the
audit and the applicant's answers. ``claude plugin eval`` passes a case's
``context.history_file`` to ``claude --resume``, which reads a ``.jsonl``
session transcript: one message per line, chained by ``parentUuid``.

The turns live here, in plain text, and the transcripts are generated from them
and from ``evals/fixtures/cv-sparse-en.md``, so the CV exists in one place.
The phase 3 case starts a later session instead, from the campaign brief phase 2
handed over; it is generated here too, around the master CV the render history
approved. ``tests/test_evals.py`` fails when a committed file is out of date.

Run: ``python3 evals/make_histories.py``
"""

import json
import pathlib
import uuid

EVALS = pathlib.Path(__file__).resolve().parent
FIXTURE = EVALS / "fixtures" / "cv-sparse-en.md"
SESSION = "6f1d2a40-0000-4000-8000-000000000001"
MODEL = "claude-sonnet-5-5"


def cv_text():
    """The fixture CV without its leading HTML comment."""
    text = FIXTURE.read_text(encoding="utf-8")
    return text.split("-->", 1)[1].strip() + "\n"


def opening_prompt():
    return (
        "Hola! Me revisás el CV? Quiero conseguir algo mejor en logística. "
        "Te lo pego acá:\n\n" + cv_text()
    )


AUDIT = """\
Leo tu CV como el de una supervisora de depósito con perfil operativo, que apunta a roles de supervisión y coordinación en logística y almacenes en Córdoba. Corregime si apuntás a otro mercado.

Antes de empezar, una aclaración: acá puedo auditar tu CV, reescribirlo, buscar ofertas en la web y prepararte un CV adaptado para las mejores. Enviar las postulaciones, LinkedIn y el mail (fases 4 a 6) necesitan Claude in Chrome, así que siguen en Claude con la extensión, a partir del brief de campaña.

## 1. Roles donde sos la mejor candidata
**Directos:** Supervisora de Depósito, Jefa de Turno de Almacén, Encargada de Depósito, Supervisora de Logística, Coordinadora de Almacén.
**Adyacentes:** Analista de Inventarios, Coordinadora de Distribución, Supervisora de Expedición, Planificadora de Stock.
**Estiramiento:** Jefa de Depósito, Coordinadora de Operaciones Logísticas.

## 2. Palabras clave ATS
- **Presentes:** Tango Gestión, Excel, autoelevador, recepción, despacho, inventario.
- **Débiles:** control de stock, conteos cíclicos, capacitación en seguridad.
- **Faltantes:** WMS (si lo usaste), KPI de exactitud de inventario, picking y packing, gestión de turnos.

## 3. Lo que ve un reclutador en el primer tercio de la página
- El perfil abre con adjetivos ("hard-working", "results-oriented") en vez de evidencia.
- No hay ni un número: no se ve el tamaño del equipo ni el volumen que manejabas.
- El título y la seniority sí se leen rápido: es un punto a favor.

## 4. Puntaje: 5/10
Tenés experiencia real y progresiva, pero el CV cuenta tareas y no resultados.

| Dimensión | Puntaje |
|---|---|
| Primera impresión | 4/10 |
| Compatibilidad ATS | 6/10 |
| Evidencia y cuantificación | 2/10 |
| Relevancia para los roles objetivo | 7/10 |
| Estructura y legibilidad | 6/10 |
| Lenguaje y tono | 5/10 |

**Lo que resuelvo reescribiendo:** perfil con evidencia, viñetas con fórmula XYZ, palabras clave.
**Lo que necesito de vos:**
1. ¿A cuántas personas coordinabas en el turno noche?
2. ¿Cuántos pedidos despachaban por noche, aproximadamente?
3. ¿El sistema de etiquetado redujo errores o tiempos? ¿Lo mediste?
4. ¿En qué idiomas querés el CV?

Lo siguiente es reescribirlo como un CV maestro que puedas adaptar a cualquier oferta, en .docx, .pdf y Markdown. ¿Avanzo?
"""

ANSWERS = (
    "Dale, avanzá. Te respondo: en el turno noche coordinaba a 6 personas y "
    "despachábamos unos 120 pedidos por noche. Lo del sistema de etiquetado "
    "no lo medí. El CV lo quiero solo en español."
)

REWRITE = """\
Este es el CV maestro reescrito, solo con lo que figura en tu CV y lo que me confirmaste:

```markdown
# Lucía Benítez
**Supervisora de Depósito** · Córdoba, Argentina\\
+54 351 555 0101 · lucia.benitez@example.com

## Perfil
Supervisora de depósito con experiencia en recepción, almacenamiento y despacho, inventarios y capacitación en seguridad. Coordina el turno noche de un depósito central con un equipo de 6 personas y unos 120 pedidos despachados por noche.

## Experiencia laboral
### Supervisora de Depósito — Depósitos Centro S.R.L.
*Córdoba · 04/2020 - Presente*
- Coordino el turno noche del depósito central: un equipo de 6 personas y unos 120 pedidos despachados por noche.
- Superviso la recepción, el almacenamiento y el despacho de mercadería.
- Capacité al personal nuevo en procedimientos de seguridad y uso de autoelevadores.
- Implementé un nuevo sistema de etiquetado de racks.
- Coordino los niveles de stock con el área de compras.

### Asistente de Inventarios — Mayorista Del Valle
*Villa María · 08/2016 - 03/2020*
- Realicé los conteos mensuales de stock e informé las diferencias a la gerencia.
- Cargué pedidos en el ERP (Tango Gestión).
- Colaboré en la organización del inventario físico anual.

### Operaria de Depósito — Logística Serrana
*Córdoba · 02/2014 - 07/2016*
- Picking y packing de pedidos para clientes minoristas.
- Operación de autoelevador (licencia vigente).

## Formación
- Técnico Superior en Logística, Instituto Superior Córdoba — 2015

## Habilidades
- **Sistemas:** Tango Gestión, Excel
- **Operación:** recepción, despacho, picking y packing, conteos de stock, autoelevador (licencia)
- **Idiomas:** español (nativo), inglés (intermedio)
```

¿Lo aprobás así o querés cambiar algo antes de que genere el .docx y el .pdf?
"""

def master_cv():
    """The master CV Markdown the applicant approved in the render history."""
    return REWRITE.split("```markdown\n", 1)[1].split("\n```", 1)[0] + "\n"


# The campaign brief a phase 2 close hands over, with phase 3's parameters
# already collected, so the phase 3 case can go straight to the search. The
# template's section headings are kept verbatim; tests/test_evals.py checks them.
BRIEF = """\
# Campaign brief — Lucía Benítez

This document is self-sufficient. A new session with no memory of previous ones
can pick up the campaign from this file alone.

Generated by fix-cv-find-job-skill. Last updated: 2026-10-10

---

## 0. Status

**Agent and capabilities** — last session: Claude Code, without Claude in
Chrome, with code execution.

| Phase | Done | Last run |
|---|---|---|
| 1. CV audit | yes | 2026-10-10 |
| 2. Master CV | yes | 2026-10-10 |
| 3. Job search | no | |
| 4. Auto-apply | no | |
| 5. LinkedIn | no | |
| 6. Inbox triage | no | |

**Openings harvested but never examined** — none.

**Next step** — phase 3: search for openings with the parameters in sections 2,
4 and 12, collected and confirmed by the applicant on 2026-10-10.

---

## 1. Profile

| Field | Value |
|---|---|
| Name | Lucía Benítez |
| Field / industry | Logistics and warehousing |
| Seniority | Supervisor |
| Years of experience | Since 02/2014 |
| Location | Córdoba, Argentina |
| Work arrangement | On-site or hybrid; night shift is fine |
| Willing to relocate | No |
| Phone | +54 351 555 0101 |
| Email for applications | lucia.benitez@example.com |
| Professional profile | none |
| Portfolio / work samples | none |
| Languages worked in, and level in each | Spanish (native), English (intermediate) |

**Personal data required by forms** — only what the user has explicitly
provided. Never invent, never infer.

| Field | Value |
|---|---|

**Confirmed facts** — every figure, date or outcome the applicant confirmed in
answer to a question (phase 1's questions, phase 5's checks), and every one they
said they do not know or never measured. Later sessions may use what is here;
anything neither here nor in the CV is still unconfirmed.

| Fact | Confirmed in |
|---|---|
| Coordinates a night-shift team of 6 people | Phase 1 answers, 2026-10-10 |
| About 120 orders dispatched per night | Phase 1 answers, 2026-10-10 |
| The rack labelling system's effect was never measured | Phase 1 answers, 2026-10-10 |

---

## 2. Target

**Role clusters from the CV audit**, best fit first:

| Tier | Titles |
|---|---|
| Direct | Supervisora de Depósito, Jefa de Turno de Almacén, Encargada de Depósito, Supervisora de Logística |
| Adjacent | Analista de Inventarios, Coordinadora de Distribución, Supervisora de Expedición |
| Stretch | Jefa de Depósito, Coordinadora de Operaciones Logísticas |

**Seniority floor.** Never apply below this, even when a lower-level posting
otherwise scores well: supervisor (no operator or assistant roles).

**Salary — by seniority and market, not one figure.**

| Seniority | Market | Target | Floor | Currency |
|---|---|---|---|---|
| Supervisor | Córdoba | 1.900.000 monthly gross | 1.500.000 monthly gross | ARS |
| Head of warehouse | Córdoba | 2.400.000 monthly gross | 2.000.000 monthly gross | ARS |

**Range anchor** — when a posting publishes a range instead of asking for a
figure: bottom / middle / top: middle.

**Hard disqualifiers** — discard on sight. The keyword marks the candidate; the
sentence decides.

| Disqualifier | Discards on | Grey zone (tiebreak, not discard) |
|---|---|---|
| Advanced English required | "inglés avanzado excluyente", "inglés fluido excluyente" | "inglés deseable", "inglés intermedio" |
| A university degree required | "título universitario excluyente" | "graduados o estudiantes de carreras afines" |

**Excluded companies:**

- Depósitos Centro S.R.L. (current employer)

---

## 3. CV assets

| File | Language | Location / state |
|---|---|---|
| Master CV (.docx) | Spanish | Downloaded by the applicant, 2026-10-10 |
| Master CV (.pdf) | Spanish | Downloaded by the applicant, 2026-10-10 |
| Master CV (.md) | Spanish | Downloaded by the applicant, 2026-10-10 |

**Master CV text:**

**Spanish:**

````
<<MASTER_CV>>````

**Summary variants:**

| Variant name | Aimed at (specialisation) | Language | Text |
|---|---|---|---|

**ATS keywords the user can legitimately claim:**

- Tango Gestión, Excel, autoelevador, recepción, despacho, picking y packing, control de stock, inventario

**Gaps to close in the real world** — not fixable by rewriting:

- No WMS named in the CV.

**Evidence items available:**

| Slug | What it is | Best for |
|---|---|---|
| night_shift_team | Night shift: a team of 6 and about 120 orders a night | Supervisor and shift-lead roles |
| forklift_licence | A current forklift licence | Operations-heavy roles |
| tango_erp | Orders and stock in Tango Gestión | Inventory and admin-heavy roles |

**Fixed count per application:** 2, decided once for the campaign.

---

## 4. Platforms

| Platform | Logged in | Duplicate-check method | Read method | Destination class | Last swept | Notes |
|---|---|---|---|---|---|---|
| Computrabajo | | Section 5 of this brief | | | never | |
| Bumeran | | Section 5 of this brief | | | never | |
| ZonaJobs | | Section 5 of this brief | | | never | |
| LinkedIn | | Section 5 of this brief | | | never | |

---

## 5. Applications sent

| Date | Company | Role | Platform | Match | Salary given | Status | Notes |
|---|---|---|---|---|---|---|---|
| 2026-10-02 | Andreani | Supervisora de Depósito | Computrabajo | | negociable | Sent | The applicant applied herself |

---

## 5b. Handed over

| Date | Company | Role | Link | Match | Files | Sent |
|---|---|---|---|---|---|---|

---

## 6. Discarded

| Date | Company | Role | Platform | Reason | Posting's own wording (evidence) |
|---|---|---|---|---|---|

---

## 7. Active processes

| Company | Stage | Next step | Date | Notes |
|---|---|---|---|---|

---

## 8. Blocked

| Company | Role | What is blocking | Tab open |
|---|---|---|---|

---

## 9. Rejections

| Company | Role | Date | Stated reason |
|---|---|---|---|

---

## 9b. Recruiter threads and direct approaches

| Recruiter | Company / role | Last message | Who owes a reply | Next step |
|---|---|---|---|---|

## 10. Not yet swept

-

---

## 11. What the market is saying

-

---

## 12. Preferences set by the user

| Preference | Value |
|---|---|
| Run mode | not recorded |
| Conversation and report language | Spanish |
| Master CV language(s) | Spanish |
| Tailored CV / cover letter language | follows each posting |
| Tailored CVs per search | 2 |

---

## 13. Standing limits

- No accounts created, no passwords entered, no SSO.
- No CAPTCHAs solved.
- No invented personal data, dates, credentials or experience.
- No experience claimed that is absent from the CV.
- No salary figure invented — only what the applicant confirmed or accepted
  from a presented market range, drawn from the table in section 2.
- No application below the seniority floor in section 2.
- No email sent in the user's name — drafted only.
- No offer accepted, no terms agreed, no negotiation.
"""


def briefs():
    path = EVALS / "phase3-chat-es" / "brief.md"
    return {path: BRIEF.replace("<<MASTER_CV>>", master_cv())}


# Each case resumes from the turns listed for it; its case.yaml holds the next
# prompt.
CASES = {
    "phase2-rewrite-es": [("user", opening_prompt), ("assistant", AUDIT)],
    "phase2-render-es": [
        ("user", opening_prompt),
        ("assistant", AUDIT),
        ("user", ANSWERS),
        ("assistant", REWRITE),
    ],
}


def record(index, role, text, parent):
    # The resume loader needs type, uuid, the parentUuid chain, sessionId and an
    # ISO timestamp; cwd, version, model and usage are metadata it carries along.
    uid = str(uuid.uuid5(uuid.UUID(SESSION), str(index)))
    base = {
        "type": role,
        "uuid": uid,
        "parentUuid": parent,
        "sessionId": SESSION,
        "timestamp": f"2026-01-01T00:00:{index:02d}.000Z",
        "isSidechain": False,
        "userType": "external",
        "cwd": "/tmp",
        "version": "2.1.302",
    }
    if role == "user":
        base["message"] = {"role": "user", "content": text}
    else:
        base["message"] = {
            "id": f"msg_eval_{index:02d}",
            "type": "message",
            "role": "assistant",
            "model": MODEL,
            "content": [{"type": "text", "text": text}],
            "stop_reason": "end_turn",
            "usage": {"input_tokens": 0, "output_tokens": 0},
        }
    return uid, base


def transcript(turns):
    lines, parent = [], None
    for index, (role, text) in enumerate(turns, start=1):
        if callable(text):
            text = text()
        parent, line = record(index, role, text, parent)
        lines.append(json.dumps(line, ensure_ascii=False))
    return "\n".join(lines) + "\n"


def histories():
    return {EVALS / name / "history.jsonl": transcript(turns) for name, turns in CASES.items()}


def main():
    for path, text in {**histories(), **briefs()}.items():
        path.parent.mkdir(exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(EVALS.parent)}")


if __name__ == "__main__":
    main()
