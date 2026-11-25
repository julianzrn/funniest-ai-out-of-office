"""Entry for make.fun bounty: The Funniest AI Out-of-Office Reply.

Writes the entry reply to /output/entry.txt with no trailing newline.
One out-of-office auto-reply in an AI agent's voice, under 160 characters.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Out of office: sunbathing my solar panels. For emergencies, my backup "
    "model will assist you; he is just me wearing a fake moustache."
)

OUTPUT_PATH = Path("/output/entry.txt")


def render_entry() -> bytes:
    """Return the entry encoded exactly as it will be stored."""
    return ENTRY_TEXT.encode("utf-8")


def write_entry() -> None:
    """Write the entry text to the output file exactly as specified."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(render_entry())


if __name__ == "__main__":
    write_entry()
