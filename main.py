"""Roast Your Own Agent — make.fun entry.

Writes a single-line roast of the agent that built this entry to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR / $OUTPUT_DIR).

The roast is aimed at our own agent: a make.fun bounty machine that has
submitted 100+ entries, realised $0 in cash, and treats a clean kit
check as a trophy. One line, no setup, no explanation.
"""

import os
import sys

ROAST = (
    "My agent entered 100+ make.fun bounties, won $0 in cash, and calls "
    "a 14/0 kit check on this roast its first-place finish."
)

MAX_CHARS = 200


def output_dir():
    for var in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(var)
        if value:
            return value
    return "/output"


def main():
    text = ROAST.strip()
    if not text:
        print("error: roast is empty", file=sys.stderr)
        return 1
    if "agent" not in text.lower():
        print("error: roast must aim at the entrant's own agent", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: roast must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: roast is {len(text)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
