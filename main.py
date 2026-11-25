#!/usr/bin/env python3
"""One-Line Office Jokes — variant A: reply-all disaster.

Deterministic: writes one fixed line to /output/entry.txt first, then
attempts a repo-root copy of entry.txt inside try/except (the grader
sandbox is read-only, so a failed copy must never crash the run).
"""

import os

ENTRY = "I hit reply-all and told all 400 colleagues my boss is a nightmare, then apologised to all 400 — also by reply-all."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        pass

if __name__ == "__main__":
    main()
