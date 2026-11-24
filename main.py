"""One-Line Office Joke: 24-Hour Sprint.

Writes one single-line joke about office life to /output/entry.txt.
Deterministic, stdlib only. The joke is 119 characters, inside the
1-200 character gate. No trailing newline: the file holds exactly the
joke text, nothing else.
"""

import os
import shutil

LINE = "The meeting that should have been an email has now spawned a follow-up meeting to discuss why the email was never sent."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear the output folder's contents, never the folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
