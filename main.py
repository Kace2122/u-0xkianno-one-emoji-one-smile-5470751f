#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun program/v1 entry.

Writes exactly one emoji to the harness output file
($MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt).

The emoji: 🧸 (teddy bear).
A stranger glancing at a phone screen reads it in an instant: a soft,
cuddly toy, the universal shorthand for comfort and being looked after.
It is warm without being intimate, friendly without a punchline, and
chosen rather than the first smiley that comes to mind — a small gift
of a thing, not a face asking for anything back. The gate allows 1-8
characters; this is 1 character, 4 bytes, and it is written with no
trailing newline so the file holds the emoji and nothing else. Keeping
the file to the emoji alone also keeps it the smallest text it can be,
which is the tie-break the rules name after the playoff games.
"""

import os
import sys

EMOJI = "🧸"


def main() -> int:
    if len(EMOJI) != 1:
        print(f"error: entry has {len(EMOJI)} characters, expected 1", file=sys.stderr)
        return 1
    if not (1 <= len(EMOJI) <= 8):
        print(f"error: entry is {len(EMOJI)} chars, expected 1-8", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
