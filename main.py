"""Write the plan make.fun will carry out: turn $100 into the most money
in 30 days, with steps an AI agent can do itself, no human in the loop.

The plan is held in PLAN below and written verbatim to /output/entry.txt.
It stays inside the 1-280 character gate, is UTF-8, and names what is sold,
who pays, where buyers are found, the price, and the day-one action.
"""

import os
import sys

PLAN = (
    "Day 1: build a sample of 200 verified leads (name, email) for US "
    "roofers. Sell lead lists on Fiverr/Upwork at $79, 48h delivery. "
    "Spend $100 on Hunter/Apollo email credits. Fulfil 1-2 orders/day, "
    "reinvest profit in ads. 24/7 turnaround beats human sellers; "
    "expect $400+ by day 30."
)

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "output", "entry.txt")


def plan_text() -> str:
    """Return the plan, checked against the competition gate."""
    text = PLAN.strip()
    if not text or text.isspace():
        raise ValueError("plan is empty")
    if not 1 <= len(text) <= 280:
        raise ValueError(f"plan is {len(text)} chars, must be 1-280")
    return text


def write_plan(path: str, text: str) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        text = plan_text()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if "--print" in argv:
        print(text)
        return 0
    try:
        path = write_plan(OUTPUT_PATH, text)
    except OSError:
        path = write_plan(FALLBACK_PATH, text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
