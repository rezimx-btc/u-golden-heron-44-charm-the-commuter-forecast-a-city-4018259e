#!/usr/bin/env python3
"""One-line weather forecast for a city that does not exist.

Entry for u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e:
a single forecast line (<=140 characters) for the invented city of
Quibberton, written to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = (
    "In Quibberton, rain is due at nine, but it clocks in at 8:59 "
    "\u2014 early, like you, and the platform finally agrees."
)


def main():
    # The brief caps the entry at 140 characters; fail loudly if it ever drifts.
    assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, over the 140 limit"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    out_path = out_dir if out_dir.endswith(".txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
