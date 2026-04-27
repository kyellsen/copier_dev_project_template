"""Shared utilities for developer scripts."""

import subprocess
import sys
from pathlib import Path


class Colors:
    """ANSI color codes for terminal output."""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def print_header(msg: str) -> None:
    """Print a bold header message."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}🚀 {msg}{Colors.ENDC}")


def print_step(msg: str) -> None:
    """Print a step indicator message."""
    print(f"\n{Colors.OKCYAN}👉 {msg}{Colors.ENDC}")


def print_success(msg: str) -> None:
    """Print a success message."""
    print(f"{Colors.OKGREEN}✅ {msg}{Colors.ENDC}")


def print_warning(msg: str) -> None:
    """Print a warning message."""
    print(f"{Colors.WARNING}⚠️  {msg}{Colors.ENDC}")


def print_error(msg: str) -> None:
    """Print an error message to stderr."""
    print(f"{Colors.FAIL}❌ {msg}{Colors.ENDC}", file=sys.stderr)


def run_command(
    command: list[str],
    cwd: Path | str | None = None,
    check: bool = True,
    env: dict[str, str] | None = None,
    capture_output: bool = False,
) -> subprocess.CompletedProcess[str]:
    """Run a subprocess command safely."""
    cmd_str = " ".join(command)
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            check=check,
            env=env,
            text=True,
            capture_output=capture_output,
        )
        return result
    except subprocess.CalledProcessError as e:
        print_error(f"Command failed with exit code {e.returncode}: {cmd_str}")
        if e.stderr:
            print_error(e.stderr.strip())
        if check:
            sys.exit(e.returncode)
        raise e
    except FileNotFoundError:
        print_error(f"Command not found in PATH: {command[0]}")
        if check:
            sys.exit(1)
        raise


def fmt_duration(seconds: float) -> str:
    """Format seconds into a human-readable string (e.g. '1.2s' or '2m 3.4s')."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes}m {secs:.1f}s"
