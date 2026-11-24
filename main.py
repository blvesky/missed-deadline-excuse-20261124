"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry (program/v1).

Writes a single-line excuse from an AI agent for a missed deadline to
/output/entry.txt. Deterministic: the same text on every run.
The text is 98 characters, one line, no trailing newline issues —
the gate requires UTF-8 text of 1 to 200 characters, not only
whitespace. Revised after review: the trailing explanation was cut
so the laugh lands on the last words.
"""

import os
from pathlib import Path

EXCUSE = (
    "The work was done, but my context window filled up with the apology "
    "I was drafting for being late."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
