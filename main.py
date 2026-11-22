"""Write the competition plan to /output/entry.txt.

Stdlib only. The plan text is a single constant so the program is
deterministic and runs offline in the grading sandbox.
"""

import os

TEXT = (
    "Day 1: scrape 2,000 US roofer emails from Google Maps, verify them, "
    "list 500-lead packs at $49 on Gumroad. Cold-email 100 marketing "
    "agencies daily. $100 covers verification, domain, email tool. "
    "3 packs a week = $588 in 30 days, costs ~$80. "
    "Edge: verified, fresh, one niche only."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
