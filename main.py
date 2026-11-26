#!/usr/bin/env python3
"""news-image-20261125: write the entry image to /output/entry.png.

The entry image is the newspaper front page held in this repository as
base64 text (entry.png.b64), so the repository stays plain text. Decoding
is deterministic: two runs write identical bytes.
"""
import base64
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png.b64"
OUT = Path("/output/entry.png")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(base64.b64decode(SRC.read_text().strip()))


if __name__ == "__main__":
    main()
