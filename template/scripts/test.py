"""Test runner with marker support. Called by: just test-unit, test-int, etc."""
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Map CLI argument to pytest directory + marker
SUITES: dict[str, tuple[str, str]] = {
    "unit": ("tests/unit/", "unit"),
    "integration": ("tests/integration/", "integration"),
    "system": ("tests/system/", "system"),
}


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <{'|'.join(SUITES)}|test|all>")
        sys.exit(1)

    target = sys.argv[1]

    if target == "test":
        suites = ["unit", "integration"]
    elif target == "all":
        suites = list(SUITES)
    elif target in SUITES:
        suites = [target]
    else:
        print(f"✗ Unknown test suite: {target}")
        sys.exit(1)

    failed = False
    for suite in suites:
        path, marker = SUITES[suite]
        suite_dir = PROJECT_ROOT / path
        if not suite_dir.exists():
            print(f"⚠ {path} does not exist, skipping")
            continue

        print(f"\n── {suite} tests ──")
        result = subprocess.run(
            ["uv", "run", "pytest", str(suite_dir), "-m", marker],
            cwd=PROJECT_ROOT,
        )
        # Exit code 5 = no tests collected (ok for empty suites)
        if result.returncode not in (0, 5):
            failed = True

    if failed:
        print("\n✗ Some tests failed")
        sys.exit(1)
    print("\n✓ All test suites passed")


if __name__ == "__main__":
    main()
