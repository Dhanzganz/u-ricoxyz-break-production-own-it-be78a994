#!/usr/bin/env python3
"""Break Production, Own It — writes the one-line confession to /output/entry.txt."""

import os

ENTRY = "I deleted the production database. The backup lived in the same database. I have no further updates."


def main():
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
