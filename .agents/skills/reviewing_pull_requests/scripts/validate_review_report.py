#!/usr/bin/env python3
"""
validate_review_report.py
Validador determinista de formato para reportes de revisión de PR en ADA-07.
Comprueba la presencia obligatoria de secciones requeridas sin depender de LLM.
"""

import sys
import os

REQUIRED_SECTIONS = [
    "## Review Context",
    "## Requirements / Acceptance Criteria Reviewed",
    "## Test Evidence",
    "## MUST FIX",
    "## SHOULD FIX",
    "## OPTIONAL",
    "## Final Review Summary",
    "Human decision required:"
]

def validate_report(filepath: str) -> int:
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: '{filepath}'", file=sys.stderr)
        return 1

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"ERROR: Could not read file '{filepath}': {e}", file=sys.stderr)
        return 1

    missing = []
    for section in REQUIRED_SECTIONS:
        if section not in content:
            missing.append(section)

    if missing:
        print(f"INVALID: PR readiness review structure is incomplete in '{filepath}'.", file=sys.stderr)
        print("Missing required sections / lines:", file=sys.stderr)
        for m in missing:
            print(f"  - {m}", file=sys.stderr)
        return 1

    print("VALID: PR readiness review structure is complete.")
    return 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_review_report.py <path_to_report.md>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    exit_code = validate_report(filepath)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
