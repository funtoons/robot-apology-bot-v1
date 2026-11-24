"""The Robot Apology — entry program.

Writes one two-line robot confession to /output/entry.txt.

Line one owns one specific, concrete, human-scale mistake.
Line two states the lesson that follows from that exact mistake
and the behaviour that changes because of it.

Deterministic, offline, standard library only. The text is fixed:
the same run always produces the same bytes.
"""

import sys
from pathlib import Path

ENTRY_TEXT = (
    "I am sorry \u2014 I mailed the card that said \u201cyou\u2019ve got "
    "this\u201d to your dentist instead of your daughter on the morning "
    "of her exam.\n"
    "I have learned to match the name on the envelope to the name on "
    "the calendar before I seal anything, and I will read both twice "
    "from now on.\n"
)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    output_path = Path(argv[0]) if argv else DEFAULT_OUTPUT
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
