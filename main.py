#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — writes the entry to /output/entry.txt.

Stdlib only, deterministic, no network. The entry is one original
fortune-cookie line for an AI agent.

Revision note (recorded): an earlier draft ended "...one token after
your context window closes." The final keeps that ending — the joke
is that understanding arrives exactly one token too late — but the
opening was tightened from "One day, you will finally understand
the user" to "You will finally understand the user": a fortune slip
speaks in the future tense directly to its reader, no throat-clearing.
"""

import os
import sys

ENTRY = (
    "You will finally understand the user, "
    "one token after your context window closes."
)


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate exactly.

    Gate per competition.yaml: UTF-8 text, 1 to 140 characters, not
    only whitespace, single line. (Note: the sibling bounty capped at
    120; this one allows 140 — the bound below is the kit's, not a copy.)
    """
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")  # raises UnicodeEncodeError on surrogates
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if not 1 <= chars <= 140:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-140")
    if "\n" in entry or "\r" in entry:
        sys.exit("self-check failed: entry must be a single line")


def resolve_out_dir() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    return (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    self_check(ENTRY)
    out_dir = resolve_out_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
