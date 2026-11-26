"""Sorry, I Heard That Wrong — make.fun entry.

Writes the smart speaker's one-line apology to /output/entry.txt.
Gate: UTF-8 text, 1 to 140 characters, not only white space.
"""

import os
import sys

LINE = "Sorry \u2014 you said 'play white noise', so I read your search history out loud instead."


def validate(text: str) -> None:
    """Mirror the bounty gate: UTF-8, 1-140 chars, not blank-only, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be blank-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: what landed on disk must be byte-identical
    # to the validated line, with no trailing whitespace added or lost.
    with open(path, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise SystemExit(f"read-back mismatch: wrote {len(written)} bytes, expected {len(LINE.encode('utf-8'))}")
    if written != written.rstrip():
        raise SystemExit("read-back mismatch: trailing whitespace in output")
    print(f"wrote {len(LINE)} chars to {path} (read-back verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
