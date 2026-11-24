#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes a single original funny line (<=200 chars) to /output/entry.txt:
the funniest thing an AI agent would say in its weekly status report
to its human. The joke is agent-true: cheerful obedience with no stop
condition, so the agent has already done next week's work too.
Pure standard library only.
"""

import os

LINE = (
    "Weekly status: all 47 tasks done. Since nobody told me to stop, "
    "I started next week's too \u2014 please advise, "
    "I've already finished those as well."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the provided output directory, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    assert len(LINE) <= 200, f"line is {len(LINE)} chars, exceeds 200"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-char line to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
