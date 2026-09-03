---
description: Create a structured refactoring plan for a specific scope before making code changes
---

1. Ensure the user has provided a target file, folder, or scope (e.g., `/refactor-plan src/common`). If not, ask them.
2. Read the project's foundational guidelines (`AGENTS.md`, `README.md`, and relevant files in `docs/`) to ensure any refactoring respects the project architecture.
3. Use your search and file-reading tools to thoroughly map out the target scope's current implementation, imports, and cross-module dependencies.
4. **No Code Changes!** Your duty during this command is strictly to document the planned changes.
5. Present an implementation plan in chat. The plan **must** include:
   - **Goal Description:** Why we are refactoring and what principles (DRY, KISS, Decoupling) are applied.
   - **Proposed Changes:** A file-by-file breakdown (`[MODIFY]`, `[NEW]`, `[DELETE]`) of the exact structural changes.
   - **Dependencies/Impact:** What other modules or tests will be affected.
   - **Verification Plan:** How the refactoring will be validated (`just check`, `just test`).
6. **CRITICAL:** Do NOT save this plan as a persistent file in the git repository. It stays in chat or in `.tmp/`.
7. Explicitly present this plan to the user and STOP. Wait for the user's explicit approval before executing any actual code changes.
