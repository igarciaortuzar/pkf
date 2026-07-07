#!/usr/bin/env python3
"""Stop hook: recuerda proponer fricciones candidatas cuando la sesion toco
archivos de alto impacto para PKF (specs/, un DRAFT de ADR o
docs/business-rules.md).

Refuerza AGENTS.md sección 7 (captura explícita de fricciones).

Ver docs/opcional-claude-code-hooks.md para instalación.
"""
import json
import re
import sys

FRICTION_SIGNAL_PATTERNS = [
    r"(^|/)specs/.*\.md$",
    r"(^|/)docs/adr/DRAFT-.*\.md$",
    r"(^|/)docs/business-rules\.md$",
]

REMINDER = (
    "[PKF] Esta sesion edito specs/, un DRAFT de ADR o business-rules.md. "
    "Antes de cerrar: ¿hay alguna friccion real de esta sesion que valga la "
    "pena proponer a docs/friction-log.md? Si si, anunciala explicitamente "
    "(que encontraste + tu intencion) antes de documentarla -- nunca la "
    "escribas en silencio (AGENTS.md seccion 7). Si no hay ninguna, dilo "
    "explicitamente y continua."
)

def _session_touched_protected_files(transcript_path: str) -> bool:
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            message = entry.get("message")
            if not isinstance(message, dict):
                continue
            content = message.get("content")
            if not isinstance(content, list):
                continue

            for block in content:
                if not isinstance(block, dict):
                    continue
                if block.get("type") != "tool_use":
                    continue
                if block.get("name") not in ("Edit", "Write"):
                    continue
                file_path = block.get("input", {}).get("file_path", "") or ""
                for pattern in FRICTION_SIGNAL_PATTERNS:
                    if re.search(pattern, file_path):
                        return True
    return False

def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    if data.get("stop_hook_active"):
        sys.exit(0)

    transcript_path = data.get("transcript_path", "") or ""

    try:
        touched = _session_touched_protected_files(transcript_path)
    except (OSError, ValueError):
        sys.exit(0)

    if not touched:
        sys.exit(0)

    print(REMINDER, file=sys.stderr)
    sys.exit(2)

if __name__ == "__main__":
    main()
