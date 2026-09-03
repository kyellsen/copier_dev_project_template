---
description: Audit documentation structure and DRY compliance against docs/STRUCTURE.md
---

1. Ensure the user has provided a target scope (e.g., `/structure-audit root`, `/structure-audit docs/`). If not, default to the entire repository.
2. Read the documentation boundaries defined in `docs/STRUCTURE.md`. Pay close attention to the DRY rules and file ownership boundaries. In a workspace, read each package's own `docs/STRUCTURE.md` too, and note the scope separation between them.
3. Read `docs/index.md` (and each package's `docs/index.md`) to see what is meant to exist.
4. Use file tools to locate all `.md` files in the target scope. **Exclude** unversioned directories (`.venv/`, `.git/`, `__pycache__/`, `_workspace/`, `.tmp/`).
5. Read the discovered `.md` files.
6. **No Code/File Changes!** Your task is strictly an audit. Do not modify any files.
7. Evaluate the documentation against the `STRUCTURE.md` rules. Check for:
   - **File location:** Is each file where it belongs according to `STRUCTURE.md`?
   - **Content bounds:** Does any documentation paraphrase source code instead of linking to it?
   - **DRY violations:** Is information duplicated across multiple files instead of linked?
   - **One owner per topic:** Are there two files describing the same concept?
   - **Dead notes:** Are there obsolete or scrap notes that should be in `.tmp/` or deleted?
   - **index.md completeness:** Is every file listed in the appropriate `index.md`?
8. Present your findings directly in your chat response using markdown. **CRITICAL:** Do NOT write report files to the repository.
9. Ask the user if they'd like you to start fixing the identified issues.
