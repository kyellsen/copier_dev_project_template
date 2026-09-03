# Commit Message Guidelines

> **Status:** Normative (Mandatory) · **Scope:** All Contributors & AI Agents

This project uses [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
to maintain a clean, readable `git log`.

## 1. Commit Message Structure

```text
<type>(<optional scope>): <subject starting with lowercase>

<optional body>
- Use bullet points for structural readability
- Explain what was changed and why
```

## 2. Types

| Type | Purpose |
|---|---|
| `feat` | A new feature or capability |
| `fix` | A bug fix |
| `docs` | Documentation only changes |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `chore` | Tooling, pipeline, config, or dependency changes |
| `test` | Adding or updating tests |
| `build` | Build system, packaging, dependencies |
| `ci` | CI configuration and workflows |
| `perf` | A change made to improve performance |
| `release` | Version bump commits |

## 3. Breaking Changes

The `!` goes **after** the closing parenthesis, never before it:

```text
refactor(config)!: rename the schema module   ✅
refactor!(config): rename the schema module   ❌
```

Both forms look right, and only the first one is. Every changelog parser reads
the marker in that position; in the wrong place the commit parses as an ordinary
`refactor` and the breaking change disappears without an error. This is enforced
by the hook precisely because it fails silently otherwise.

## 4. Subject Line Rules

- ≤ 72 characters
- Lowercase start, no period at end
- Imperative mood: "add X" not "added X"

## 5. Body (optional)

- One blank line between subject and body
- Use `-` bullet points
- Reference related issues: `Fixes #12`

## 6. Examples

**Simple:**
```text
fix: handle missing .env file gracefully in check_env
```

**With scope and body:**
```text
feat(pipeline): add timestamp-based cache decorator

- Skip re-computation when output parquet is newer than input CSV
- Decorator can be applied to any load/analyze function
```

**Breaking change:**
```text
refactor(publication)!: rename thesis/ to publication/

All Typst files moved from thesis/ to publication/.
Update any scripts referencing the old path.
```

## 7. What enforces this

`scripts/git-hooks/commit-msg` — a `commit-msg` hook wired in by
`just install-hooks`, the same `core.hooksPath` that carries the `pre-commit`
gate. It checks the type, the length, the `!` position, the full stop, the
lowercase start and the blank line before the body. It runs in milliseconds and
never inspects your files.

**The hook and this document are one rule in two forms.** Change one and change
the other in the same commit — a convention that lives only in prose has nothing
keeping it honest, and the stale half is the one the next reader believes.

If the hook rejects a message, your text is not lost:

```sh
git commit -e -F .git/COMMIT_EDITMSG
```
