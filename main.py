#!/usr/bin/env python3
"""The joke about the demo.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. No network, no arguments, no dependencies.
"""

import os

JOKE = (
    "My coding agent rehearsed the demo forty times flawlessly \u2014 "
    "then, live in front of two hundred people, it spotted a typo and "
    "fixed it by taking the whole app down."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
