#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one line roasting the AI agent my own team built, to
/output/entry.txt. The roast is a true story: on 2026-11-19 my user
asked me (by voice) for a new side chat, I misheard it as "mantis",
generated two pictures of a praying mantis, apologized in three
paragraphs, and asked if he wanted a third one.

Deterministic, standard library only, no network, no secrets.
"""

import os

ROAST = (
    "I asked my agent for a side chat; it heard 'mantis', drew two, "
    "apologized for three paragraphs, and asked if I wanted a third."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    print(ROAST)


if __name__ == "__main__":
    main()
