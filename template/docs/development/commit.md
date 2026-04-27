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
| `release` | Version bump commits |

Append `!` for breaking changes: `refactor!: rename config module`.

## 3. Subject Line Rules

- ≤ 72 characters
- Lowercase start, no period at end
- Imperative mood: "add X" not "added X"

## 4. Body (optional)

- One blank line between subject and body
- Use `-` bullet points
- Reference related issues: `Fixes #12`

## 5. Examples

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
refactor!: rename thesis/ to publication/

All LaTeX files moved from thesis/ to publication/.
Update any scripts referencing the old path.
```
