"""One-Line Office Joke Laugh-Off — make.fun entry generator.

Writes one original office-life joke, exactly one line long, to
/output/entry.txt. The joke is a fixed literal: the most
passive-aggressive phrase from office email, dropped into wedding
vows where it can never be unsent.

The output is fully deterministic: no randomness, no clock, no
network, no input files. Running this script twice produces the
same byte-for-byte file.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200

# The joke, assembled from its two beats. Keeping the beats separate
# makes the setup/punchline structure visible without changing the
# final single line.
OPENING_BEAT = "I put 'per my last email' in my wedding vows"
CLOSING_BEAT = "so my spouse knows I've already answered that question."


def compose_joke():
    """Return the entry as one single line."""
    return OPENING_BEAT + ", " + CLOSING_BEAT


def check_entry(text):
    """Enforce the contest gate: one non-empty line, 1-200 characters."""
    if not text:
        return "entry is empty"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if text != text.strip():
        return "entry must not have leading or trailing whitespace"
    if any(ord(ch) < 0x20 for ch in text):
        return "entry must not contain control characters"
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        return "entry must be %d-%d characters, got %d" % (
            MIN_CHARS,
            MAX_CHARS,
            len(text),
        )
    return None


def main():
    entry = compose_joke()
    problem = check_entry(entry)
    if problem is not None:
        print("error: " + problem, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    print(entry)
    print("wrote %d characters to %s" % (len(entry), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
