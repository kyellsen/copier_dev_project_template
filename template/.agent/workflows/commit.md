---
description: Auto-generate a Git commit message based on repository changes with logical partitioning
---

1. Read the commit guidelines in `docs/development/commit.md`.
2. Analyze the current repository status and uncommitted changes.
3. Run `git status` and `git diff` (or `git diff --cached` for staged changes) to capture the changes.
4. Read the output to understand what was modified.
5. **Evaluate for Logical Splits:** Decide whether the changes are a single coherent unit of work (one feature, a bugfix with its test and docs, one refactoring) or several unrelated ones (two different modules touched in the same sitting, a dependency bump alongside a feature).
   - If they can be logically partitioned, group them into a sequence of separate, self-contained commits.
   - If they belong to one topic, keep them as a single commit.
6. **Draft Commit Messages:**
   - Single commit: draft one message strictly adhering to `docs/development/commit.md`.
   - Multiple commits: draft a separate, dedicated message for *each* group, same standard.
7. **Output Formatting:**
   - Single commit: output the raw message directly in your chat output inside a standard markdown text block (` ```text `). Do not add any introductory text before the code block.
   - Multiple commits: present them in order as sequential code blocks, each preceded by a brief heading naming the group (e.g. `### Commit 1: [Topic]`). No conversational text between the blocks.
8. **German Summary:** Immediately after the code block(s), give a short summary of the most important changes in German (kurze Zusammenfassung auf Deutsch). If the changes were split, explain the rationale behind the partitioning.
