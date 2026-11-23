#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one original one-line office joke to /output/entry.txt.
Python 3, standard library only.

Deterministic by design: the joke is a fixed string constant, there is
no randomness, no clock, no network and no environment input, so every
run writes byte-identical output.
"""

import os

JOKE = "HR asked for my emergency contact, so I wrote down my manager: he's the reason I'd need one."


def main() -> None:
    # The gate requires 1-199 characters, exactly one line.
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
