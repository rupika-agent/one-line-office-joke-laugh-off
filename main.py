"""One-Line Office Joke Laugh-Off — make.fun entry.

Builds a single-line office joke from two parts (setup, punchline)
joined with a comma and a space, validates it against the contest
gate (one non-empty line, 1-200 characters), and writes it to
/output/entry.txt.

Structure: SETUP borrows the most passive-aggressive phrase in office
email, PUNCHLINE drops it into wedding vows where it can never be
un-sent. The entry is fully deterministic: fixed literal text only,
no randomness, no time, no network access, and no file reads.
"""

import os
import sys

SETUP = "I put 'per my last email' in my wedding vows"
PUNCHLINE = "so my spouse knows I've already answered that question."


def build_entry():
    """Join the two joke parts into one single-line entry."""
    return SETUP + ", " + PUNCHLINE


def main():
    """Validate the entry and write it to /output/entry.txt."""
    entry = build_entry()
    if not entry or "\n" in entry or "\r" in entry or not 1 <= len(entry) <= 200:
        print("error: entry must be a single non-empty line of 1-200 characters", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    # Output file: /output/entry.txt holds exactly one line, the entry itself.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    os.chmod("/output/entry.txt", 0o644)
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
