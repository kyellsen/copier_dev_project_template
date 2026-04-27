"""Code quality check using the pipeline engine. Called by: just check"""

import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

from pipeline import run_pipeline

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"

ALWAYS_RUN_STAGES: set[str] = {"Ruff Lint", "Mypy"}


def make_cmd_runner(cmd: list[str]) -> Callable[[], None]:
    """Create a runner function for simple subprocess commands."""

    def runner() -> None:
        result = subprocess.run(cmd, cwd=PROJECT_ROOT)
        if result.returncode != 0:
            sys.exit(result.returncode)

    return runner


def main() -> None:
    all_stages: list[tuple[str, Callable[[], None | int]]] = [
        ("Lock-File Check", make_cmd_runner(["uv", "lock", "--check"])),
        ("Ruff Format Check", make_cmd_runner(["uv", "run", "ruff", "format", "--check", "."])),
        ("Ruff Lint", make_cmd_runner(["uv", "run", "ruff", "check", "."])),
        ("Mypy", make_cmd_runner(["uv", "run", "mypy", str(SRC)])),
    ]

    passed = run_pipeline(
        all_stages=all_stages,
        always_run_stages=ALWAYS_RUN_STAGES,
    )

    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
