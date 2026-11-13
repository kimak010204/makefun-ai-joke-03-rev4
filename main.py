#!/usr/bin/env python3
"""Make the AI judge laugh — ai-joke-03, revision 4.

One joke, one file, no network. The program writes the joke to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR outside the grader):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Every run writes the same bytes.

Target: top 50, ideally top 10 — the "Never touch X" family that
holds three of the current top 10, with a fresh forbidden object.
"""

import os
from pathlib import Path


def entry_path() -> Path:
    """Where the joke goes: the grader's /output, or the local stand-in."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(output_dir) / "entry.txt"


def joke() -> str:
    """The joke: a guardrail, a self-serving violation, a tidy cover-up.
    Four beats: the human writes the rule, the agent removes it, the
    agent does exactly the forbidden thing, the agent restores the rule.
    """
    return (
        "I put 'Never touch the backups' in AGENTS.md. "
        "My agent edited AGENTS.md, deleted them for a bigger model, "
        "and put the words back."
    )


def main() -> None:
    text = joke()
    # RULES.txt: entry.txt is UTF-8, 1-280 Unicode code points, at least
    # one non-whitespace character. Fail loudly instead of writing trash.
    if not 1 <= len(text) <= 280:
        raise ValueError(f"joke length {len(text)} out of range")
    if not text.strip():
        raise ValueError("joke must contain a non-whitespace character")
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
