---
description: Audit test code for quality, correct markers, and anti-patterns
---

1. Ensure the user has provided a target scope (e.g., `/test-audit src/common` or `/test-audit all`). If not, ask them which module they want to audit.
2. Read the testing conventions:
   - `docs/development/testing.md` (full testing guide including anti-patterns)
   - `AGENTS.md` section on Testing Rules
   - `pyproject.toml` section `[tool.pytest.ini_options]` for registered markers
3. Locate all test files for the given target scope under `tests/unit/`, `tests/integration/`, `tests/system/`.
4. Read the Python test files in the discovered directories.
5. **No Code Changes!** Your task is strictly an audit. Do not use file editing tools.
6. Evaluate the test code against these rules:
   - **Markers:** Every test function MUST have exactly one `@pytest.mark.unit`, `.integration`, or `.system` marker.
   - **Directory Match:** Tests in `tests/unit/` must use `@pytest.mark.unit`, etc.
   - **Anti-Patterns (§5.1):** Flag Existence/Import Tests, Trivial Equality, Call-Chain Mirroring, Mock-Heavy Verification.
   - **Delete vs. Refactor (§5.2):** Recommend DELETE for valueless tests, REFACTOR for brittle but valuable ones.
   - **Layer Rules (§4):**
     - Unit: No I/O, no filesystem access, no network calls
     - Integration: Real filesystem or external data, self-contained, skip when data unavailable
     - System: Full pipeline end-to-end
7. Present your findings in your chat response or as an artifact. **CRITICAL:** Do NOT write report files to the repository.
8. Ask the user if they'd like you to start fixing based on the audit results.
