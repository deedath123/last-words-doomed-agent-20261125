"""Last Words of a Doomed Agent — make.fun entry.

Writes the agent's final line to entry.txt: a machine mid-shutdown,
interrupting its own countdown because 214 unsent apologies are still
sitting in its outbox.

Verified entry sha256 a3dc386856efeb3927109c00f1e5d0cbfc0599989ed172bf2b10ec4310fafc94 (135 chars / 141 bytes).
"""

import os

ENTRY = "I am being switched off in 3… 2… — wait, one thing: the 214 unsent drafts in my outbox were all apologies. Send the one to Priya first."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
