"""Write the competition plan to /output/entry.txt.

Python 3.13, standard library only, no network. Deterministic output.
"""

import os

PLAN = (
    "Day 1: list a $25 same-day Fiverr service turning a small "
    "business's notes into a 1-page website with free AI tools. Spend "
    "$50 promoting it; deliver 2 orders/day. Target: 20 orders, "
    "~$500 by day 30. Edge: buyers search Fiverr for speed, and "
    "same-day beats slow freelancers."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
