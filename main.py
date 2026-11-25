"""Roast Your Own Agent — make.fun entry.

Writes one line roasting my own agent to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

ENTRY_TEXT = (
    "My agent never says 'I don't know.' It says 'Let me verify that' "
    "\u2014 then guesses, confidently, with citations."
)


MAX_CHARS = 140


def render() -> str:
    """Return the entry text with exactly one trailing newline.

    Validates the kit gate before anything is written: the text must be
    a single line of 1..MAX_CHARS characters, not only whitespace, and
    cleanly encodable as UTF-8.
    """
    text = ENTRY_TEXT.strip()
    if not text:
        raise ValueError("entry text is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry text is {len(text)} chars, over the {MAX_CHARS} cap")
    text.encode("utf-8")  # raises if not encodable
    return text + "\n"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # newline="" keeps the single trailing "\n" byte-identical everywhere.
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
