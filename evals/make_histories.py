#!/usr/bin/env python3
"""Build the conversation histories the phase 2 eval cases resume from.

Phase 1 ends by asking the applicant questions, so a phase 2 case cannot start
from a single prompt: it resumes a conversation that already holds the CV, the
audit and the applicant's answers. ``claude plugin eval`` passes a case's
``context.history_file`` to ``claude --resume``, which reads a ``.jsonl``
session transcript: one message per line, chained by ``parentUuid``.

The turns live here, in plain text, and the transcripts are generated from them
and from ``evals/fixtures/cv-sparse-en.md``, so the CV exists in one place.
``tests/test_evals.py`` fails when a committed transcript is out of date.

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

Antes de empezar, una aclaración: acá puedo auditar tu CV y reescribirlo. La búsqueda de ofertas, las postulaciones, LinkedIn y el mail (fases 3 a 6) necesitan Claude in Chrome, así que siguen en Claude con la extensión, a partir del brief de campaña.

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
    for path, text in histories().items():
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(EVALS.parent)}")


if __name__ == "__main__":
    main()
