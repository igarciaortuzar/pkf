#!/usr/bin/env python3
"""
export_business_rules.py — Exporta docs/business-rules.md a JSON (ADR-002).

docs/business-rules.md sigue siendo la única fuente de verdad. Este script
genera docs/business-rules.json como artefacto derivado para que herramientas
que no leen Markdown (ej. Power BI vía Web.Contents) puedan consumir las
reglas. El JSON no se edita a mano; se regenera corriendo este script.

Uso:  python tools/export_business_rules.py   (desde la raíz del repo)
"""

import json
import re
import sys
from pathlib import Path

if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "business-rules.md"
OUT = ROOT / "docs" / "business-rules.json"

RULE_RE = re.compile(
    r"^###\s+(RN-\d{3})\s+—\s+(.+?)\s*\n\n"
    r"\*\*Estado:\*\*\s*(.+?)\s*\n"
    r"\*\*Regla:\*\*\s*(.+?)\s*\n"
    r"\*\*Origen:\*\*\s*(.+?)\s*\n"
    r"\*\*Historial:\*\*\s*\n((?:-\s.+\n?)+)",
    re.MULTILINE,
)


def parse_historial(block: str) -> list[str]:
    return [line.lstrip("- ").strip() for line in block.strip().splitlines()]


def main() -> int:
    if not SRC.exists():
        print(f"ERROR: no existe {SRC}")
        return 1

    content = SRC.read_text(encoding="utf-8")
    reglas = []
    for m in RULE_RE.finditer(content):
        rn_id, titulo, estado, regla, origen, historial_block = m.groups()
        reglas.append(
            {
                "id": rn_id,
                "titulo": titulo.strip(),
                "estado": estado.strip(),
                "regla": regla.strip(),
                "origen": origen.strip(),
                "historial": parse_historial(historial_block),
            }
        )

    OUT.write_text(
        json.dumps({"reglas": reglas}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"OK — {len(reglas)} regla(s) exportada(s) a {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
