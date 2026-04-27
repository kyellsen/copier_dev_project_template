# AGENTS.md

> **AUTHORITY:** This document is the **single source of truth** for all AI agents
> working on this repository. Supplementary files (`.gemini/`, `.cursorrules`, `CLAUDE.md`)
> redirect here — never the reverse.

## 1. Language Policy
- **Code, Commits, Docs:** English
- **Chat with User:** German

## 2. Quality Standards
- Run `just check` (or `just c`) before every commit
- Every test function **MUST** have a marker: `@pytest.mark.unit`, `.integration`, or `.system`
- Follow [Conventional Commits](docs/development/commit.md)

## 3. Testing Rules
1. Tests live in `tests/unit/`, `tests/integration/`, `tests/system/`
2. Unit tests: No I/O, no filesystem, no network. Fast.
3. Integration tests: Real filesystem or external data. Self-contained.
4. System tests: Full pipeline end-to-end.

## 4. Libraries & Tools
| Domain | Use |
|---|---|
| Tools | `uv`, `hatchling`, `ruff`, `mypy`, `pytest` |
| Config | `python-dotenv` |
| Quality | `just check` (ruff + mypy), `just fix` (auto-format) |
| Testing | `just test` (unit + integration), `just test-all` |

## 5. Commit Rules
- AI Agents must follow [docs/development/commit.md](docs/development/commit.md) strictly
- Subject line: lowercase, imperative, ≤ 72 chars
- Prefer small, focused commits over large monolithic ones
