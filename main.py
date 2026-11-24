#!/usr/bin/env python3
"""Writes this entry's single line to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os
from pathlib import Path

LINE = "Sorry — my context window dropped your last instruction and the tools timed out, so I used my core skill: hallucinating the answer and formatting it beautifully."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
