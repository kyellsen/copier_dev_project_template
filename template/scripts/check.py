"""Code quality check using the pipeline engine. Called by: just check"""

import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

from pipeline import run_pipeline

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"

ALWAYS_RUN_STAGES: set[str] = {"Ruff Lint", "Mypy"}


def make_cmd_runner(
    cmd: list[str], allowed_codes: set[int] | None = None
) -> Callable[[], None]:
    """Create a runner function for simple subprocess commands."""
    if allowed_codes is None:
        allowed_codes = {0}

    def runner() -> None:
        result = subprocess.run(cmd, cwd=PROJECT_ROOT)
        if result.returncode not in allowed_codes:
            sys.exit(result.returncode)

    return runner


def main() -> None:
    is_ci = "--ci" in sys.argv

    all_stages: list[tuple[str, Callable[[], None | int]]] = [
        ("Lock-File Check", make_cmd_runner(["uv", "lock", "--check"])),
        (
            "Ruff Format Check",
            make_cmd_runner(["uv", "run", "ruff", "format", "--check", "."]),
        ),
        ("Ruff Lint", make_cmd_runner(["uv", "run", "ruff", "check", "."])),
        ("Mypy", make_cmd_runner(["uv", "run", "mypy", str(SRC)])),
    ]

    if is_ci:
        all_stages.extend(
            [
                (
                    "Unit Tests",
                    make_cmd_runner(
                        [
                            "uv",
                            "run",
                            "pytest",
                            "tests/unit",
                            "-m",
                            "unit",
                            "-q",
                            "-rs",
                        ],
                        allowed_codes={0, 5},
                    ),
                ),
                (
                    "Integration Tests",
                    make_cmd_runner(
                        [
                            "uv",
                            "run",
                            "pytest",
                            "tests/integration",
                            "-m",
                            "integration",
                            "-q",
                            "-rs",
                        ],
                        allowed_codes={0, 5},
                    ),
                ),
                (
                    "System Tests",
                    make_cmd_runner(
                        [
                            "uv",
                            "run",
                            "pytest",
                            "tests/system",
                            "-m",
                            "system",
                            "-q",
                            "-rs",
                        ],
                        allowed_codes={0, 5},
                    ),
                ),
            ]
        )

    passed = run_pipeline(
        all_stages=all_stages,
        always_run_stages=ALWAYS_RUN_STAGES,
    )

    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
