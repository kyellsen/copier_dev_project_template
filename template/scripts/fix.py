"""Auto-format and auto-fix what the gate complains about. Called by: just fix

With --check nothing is written: that is `just check-typst`, the fast subset for
a sitting that only touched a .typ file.

Both recipes live here rather than in the justfile so the Typst file list has
one owner. The gate checks TYPST_HANDWRITTEN; a recipe that formatted
`publication/` instead would reach the tables a freeze step generates and the
packages an overlay vendors into publication/lib -- work that is undone on the
next generate, or that edits what is not ours.
"""

import shutil
import sys

from check import TYPST_HANDWRITTEN

from common import PROJECT_ROOT, print_error, print_header, print_step, print_success, run_command


def typst_targets() -> list[str]:
    """The hand-written Typst files that exist, or an empty list.

    typstyle is a standalone binary, not a uv dependency, so a missing one is an
    environment problem rather than a formatting failure -- the same reasoning
    the gate applies. On a machine where Homebrew is not on the PATH, prepend it:
    PATH=/home/linuxbrew/.linuxbrew/bin:$PATH.
    """
    targets = [str(p) for p in TYPST_HANDWRITTEN if p.exists()]
    if targets and shutil.which("typstyle") is None:
        print_error("typstyle not on PATH -- cannot format Typst")
        print("  install: brew install typstyle")
        sys.exit(1)
    return targets


def main() -> None:
    check_only = "--check" in sys.argv
    targets = typst_targets()

    if check_only:
        print_header("Checking Typst Formatting")
        if not targets:
            print_success("No hand-written Typst files")
            return
        result = run_command(["typstyle", "--check", *targets], cwd=PROJECT_ROOT, check=False)
        if result.returncode != 0:
            print("  fix: just fix")
            sys.exit(1)
        print_success("Typst formatting is clean")
        return

    print_header("Auto-fixing Code Quality Issues")

    # ruff exits non-zero when findings remain after fixing. An unfixable one
    # used to abort the recipe and silently skip every step below it, so both
    # ruff calls report and carry on -- `check` still fails on the leftovers.
    print_step("Ruff format")
    run_command(["uv", "run", "ruff", "format", "."], cwd=PROJECT_ROOT, check=False)

    print_step("Ruff lint --fix")
    run_command(["uv", "run", "ruff", "check", "--fix", "."], cwd=PROJECT_ROOT, check=False)

    if targets:
        print_step("typstyle (hand-written Typst)")
        run_command(["typstyle", "-i", *targets], cwd=PROJECT_ROOT, check=False)

    print_success("Fix complete")


if __name__ == "__main__":
    main()
