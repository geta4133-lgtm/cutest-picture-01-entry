"""Cutest Picture Entry: Sleepy Baby Kitten Hugging a Glowing Star on a Fluffy Cloud.

Deterministic entry script that exports the bundled 1024x1024 PNG artwork
to the configured output directory (/output/entry.png by default).
"""

import hashlib
import os
from pathlib import Path
from PIL import Image


DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.png"
EXPECTED_SIZE = (1024, 1024)


def get_output_dir() -> Path:
    """Resolve and create the target output directory."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def verify_image(path: Path) -> None:
    """Verify the bundled entry image exists and has the expected dimensions."""
    if not path.is_file():
        raise FileNotFoundError(f"Missing bundled entry image: {path}")
    with Image.open(path) as img:
        if img.size != EXPECTED_SIZE:
            raise ValueError(f"Unexpected image size {img.size}, expected {EXPECTED_SIZE}")


def export_entry(src: Path, dst: Path) -> str:
    """Verify and deterministically write the entry image bytes from src to dst."""
    verify_image(src)
    data = src.read_bytes()
    dst.write_bytes(data)
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    src = repo_root / ENTRY_FILENAME
    out_dir = get_output_dir()
    dst = out_dir / ENTRY_FILENAME
    digest = export_entry(src, dst)
    print(f"Wrote {dst} (sha256={digest})")


if __name__ == "__main__":
    main()
