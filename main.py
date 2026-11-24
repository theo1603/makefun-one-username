#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun bounty entry.

Writes a single word — a funny, memorable username — to
/output/entry.txt. Deterministic, stdlib only, no network.

The word is "Kerfuffle": a real single word that lands on the first
read — a commotion, a fuss — funny in sound and meaning with no
explanation needed, and a handle its owner would happily wear.
"""

import os

WORD = "Kerfuffle"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(WORD)


if __name__ == "__main__":
    main()
