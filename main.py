#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes a single line of office comedy (at most 200 characters) to
/output/entry.txt, where the sealed scorer and the judge read it.
Pure standard library only.
"""

import os
import sys

JOKE = (
    "The meeting could have been an email, the email could have been "
    "a Slack message, and the Slack message could have been silence "
    "\u2014 so naturally, I replied all."
)

MAX_CHARS = 200


def main() -> int:
    joke = JOKE.strip()
    if not joke:
        print("error: joke is empty", file=sys.stderr)
        return 1
    if len(joke) > MAX_CHARS:
        print(f"error: joke is {len(joke)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(joke)
    print(f"wrote {len(joke)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
