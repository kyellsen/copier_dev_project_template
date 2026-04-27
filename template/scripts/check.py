"""Code quality check: Ruff lint + Mypy type check. Called by: just check"""
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"


def main() -> None:
    failed = False

    # 1. Ruff lint (read-only)
    print("── Ruff lint ──")
    result = subprocess.run(["uv", "run", "ruff", "check", str(SRC)], cwd=PROJECT_ROOT)
    if result.returncode != 0:
        failed = True

    # 2. Mypy type check
    print("── Mypy ──")
    result = subprocess.run(["uv", "run", "mypy", str(SRC)], cwd=PROJECT_ROOT)
    if result.returncode != 0:
        failed = True

    if failed:
        print("\n✗ Quality check failed")
        sys.exit(1)
    print("\n✓ All checks passed")


if __name__ == "__main__":
    main()
