"""
Cutest Picture Entry: Sleepy Baby Kitten Hugging a Glowing Star on a Fluffy Cloud.
Deterministic: copies the bundled 1024x1024 PNG image to /output/entry.png.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
