---
description: Audit documentation structure and DRY compliance against docs/STRUCTURE.md
---

1. Ensure the user has provided a target scope (e.g., `/structure-audit root`, `/structure-audit docs/`). If not, default to the entire repository.
2. Read the documentation boundaries defined in `docs/STRUCTURE.md`. Pay close attention to the DRY rules and file ownership boundaries.
3. Use file tools to locate all `.md` files in the target scope. **Exclude** unversioned directories (`.venv/`, `.git/`, `__pycache__/`, `_workspace/`, `.tmp/`).
4. Read the discovered `.md` files.
5. **No Code/File Changes!** Your task is strictly an audit. Do not modify any files.
6. Evaluate the documentation against the `STRUCTURE.md` rules. Check for:
   - **File location:** Is each file where it belongs according to `STRUCTURE.md`?
   - **Content bounds:** Does any documentation paraphrase source code instead of linking to it?
   - **DRY violations:** Is information duplicated across multiple files instead of linked?
   - **One owner per topic:** Are there two files describing the same concept?
   - **Dead notes:** Are there obsolete or scrap notes that should be in `.tmp/` or deleted?
7. Present your findings directly in your chat response using markdown. **CRITICAL:** Do NOT write report files to the repository.
8. Ask the user if they'd like you to start fixing the identified issues.
