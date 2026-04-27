"""Auto-fix: Ruff format + lint fixes. Called by: just fix"""
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"


def main() -> None:
    print("── Ruff format ──")
    subprocess.run(["uv", "run", "ruff", "format", str(SRC)], cwd=PROJECT_ROOT)

    print("── Ruff lint --fix ──")
    subprocess.run(["uv", "run", "ruff", "check", "--fix", str(SRC)], cwd=PROJECT_ROOT)

    print("✓ Auto-fix complete")


if __name__ == "__main__":
    main()
