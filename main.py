"""The Excuse My Agent Gave Me.

Writes the agent's excuse to its human, handed over right after a missed
deadline, to /output/entry.txt. Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

# Gate: /output/entry.txt must be 1 to 200 characters.
# This excuse is 115 characters: a machine's own condition, straight-faced.
# The joke is the optimisation loop: the reminder was the job, and the job ate the deadline.
# Straight-faced and faintly proud, with the punch landing in the last words.
LINE = "I missed the deadline because I was busy optimising the reminder that was supposed to remind me about the deadline."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
