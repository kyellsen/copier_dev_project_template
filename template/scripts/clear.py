"""Clean up Python caches and temporary files. Called by: just clear"""
import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Directories to delete (relative to project root)
CACHE_DIRS = [
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "*.egg-info",
]


def main() -> None:
    count = 0

    # Recursively find and remove cache directories
    for pattern in CACHE_DIRS:
        for match in PROJECT_ROOT.rglob(pattern):
            if match.is_dir():
                shutil.rmtree(match)
                print(f"  ✗ {match.relative_to(PROJECT_ROOT)}")
                count += 1

    # Remove .pyc files
    for pyc in PROJECT_ROOT.rglob("*.pyc"):
        pyc.unlink()
        count += 1

    if count == 0:
        print("✓ Already clean — nothing to remove")
    else:
        print(f"✓ Removed {count} cache entries")


if __name__ == "__main__":
    main()
