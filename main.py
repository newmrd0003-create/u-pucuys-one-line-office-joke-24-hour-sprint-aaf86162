#!/usr/bin/env python3
"""One Line Office Joke: 24-Hour Sprint — entry writer.

Writes a single one-line joke about office life to /output/entry.txt.
"""

import os

ENTRY = "Our 'quick sync' has lasted forty minutes, covered nothing, and somehow produced three action items for people who weren't even invited."


def main():
    text = ENTRY.strip()
    # Competition rule: at most 200 characters, single line.
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text.encode("utf-8")) <= 200, (
        f"entry must be 1-200 UTF-8 bytes, got {len(text.encode('utf-8'))}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
