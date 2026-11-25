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

# The competition entry, kept as a single module constant so the exact
# submitted text lives in exactly one place. Do not edit this string:
# it is the judged entry (126 chars, one line, no trailing newline).
ENTRY_TEXT = (
    "I asked my agent for a side chat; it heard 'mantis', drew two, "
    "apologized for three paragraphs, and asked if I wanted a third."
)


def _check_entry(text: str) -> None:
    """Pre-write self-check: the gate requires 1-200 chars, one line,
    no trailing whitespace. Fail loudly instead of writing a bad entry."""
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    assert text == text.rstrip(), "entry must not end with whitespace"


def main() -> None:
    _check_entry(ENTRY_TEXT)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
