"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message — the note an AI agent leaves in the log after
a long night of chasing down and fixing its own bugs — to entry.txt.
One line, at most 200 characters, no trailing newline.
"""

import os

ENTRY = (
    "fix: my 3am self wrote this bug, my 4am self fixed it, "
    "and neither of us trusts the other with production anymore"
)


def main():
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    ENTRY.encode("ascii")  # entry must be plain ASCII
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
