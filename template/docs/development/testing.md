# Testing Guide

> **Status:** Normative (Mandatory) · **Scope:** All Contributors & AI Agents

---

## 1. Test Markers

Every test function **MUST** have exactly one marker. Tests without a marker will be rejected.

| Marker | Included in `just ci` | Target duration |
| --- | --- | --- |
| `unit` | ✅ | < 1s/test |
| `integration` | ✅ | < 30s/test |
| `system` | ✅ | < 60s/test |

---

## 2. Directory Structure

Test location **MUST** match the marker. Mixing markers in a single directory is **FORBIDDEN**.

| Location | Marker |
| --- | --- |
| `tests/unit/` | `@pytest.mark.unit` |
| `tests/integration/` | `@pytest.mark.integration` |
| `tests/system/` | `@pytest.mark.system` |

Each directory arrives with a `test_smoke.py`. Replace it with real tests — but
do **not** delete it until you have some: `pytest` answers a *missing* directory
with exit code 4, and `just test` / `just ci` turn red on it.

---

## 3. Running Tests

### Individual Suites

```bash
just test-unit     # Unit tests only (no I/O, no external deps)
just test-int      # Integration tests (real filesystem / external data)
just test-system   # System tests (full pipeline end-to-end)
just test          # Quick dev: Unit + Integration
just test-all      # All three tiers
```

### Quality Gates

```bash
just check         # Ruff + Mypy (fast, < 10s)
just ci            # check + all tests (full pipeline)
```

### When to Run What

| Situation | Command | What it covers |
| --- | --- | --- |
| During development | `just test` | Unit + Integration (quick feedback) |
| Before every commit | `just check` | Lint, types (no tests) |
| Before push | `just ci` | Full pipeline: lint + types + all tests |

---

## 4. Writing Tests

### Unit Tests (`@pytest.mark.unit`)

- Test the **behavior** of small units, not implementation details.
- **Zero I/O**: no filesystem, no network, no database.
- Use `tmp_path` for synthetic data, `unittest.mock` for dependencies.
- Each test should run in < 1 second.

### Integration Tests (`@pytest.mark.integration`)

- Use **real** sensor data from the Nextcloud directories (`$BA_KS_*_ROOT`).
- Must be **self-contained**: skip gracefully when data is unavailable.
- Do **NOT** mock the data source — the whole point is testing real I/O.

**Pattern for data availability:**

```python
import os, pytest
from pathlib import Path

DATA_DIR = Path(os.environ.get("BA_KS_STUTTGART_ROOT", "")) / "data" / "raw" / "..."


def _skip_if_no_data(directory: Path) -> Path:
    if not directory.is_dir():
        pytest.skip(f"Data not available: {directory}")
    return directory
```

### System Tests (`@pytest.mark.system`)

- Full pipeline end-to-end (parse → cache → analyse → plot).
- Assert **end results**, not internal call sequences.

---

## 5. Gatekeeper Tests (Vertrauensanker)

Certain integration tests serve as **trust anchors** for the thesis. They validate
that our binary parsers produce identical results to the vendor software exports.

**These tests MUST pass before any parsed sensor data enters the thesis.**

| Gatekeeper | Source (ours) | Reference (vendor) |
| --- | --- | --- |
| TMS-1 (`.tsw`) | Binary parser `treemotion/tsw.py` | CSV export in `tms/csv/` |
| TMS-3 (`.twsb`) | Binary parser `treemotion/twsb.py` | CSV export in `tms/csv/` |

**Tolerances:** values ±0.0001°, timestamps ±50 ms.

```python
@pytest.mark.integration
def test_tsw_parser_matches_vendor_csv():
    """TMS-1: Parse .tsw, compare row-by-row against vendor CSV export."""


@pytest.mark.integration
def test_twsb_parser_matches_vendor_csv():
    """TMS-3: Parse .twsb, compare row-by-row against vendor CSV export."""
```

---

## 6. Test Quality & Anti-Patterns

> **Status:** Normative (Mandatory)
> This section is especially critical for AI-generated code.

### 6.1 Anti-Patterns (FORBIDDEN)

The following patterns will lead to test rejection:

- **Existence/Import Tests:** Tests that only verify imports or whether a function exists without asserting observable behavior.
- **Trivial Equality:** Tests that only assert constants or default values (unless the value is an explicit domain contract).
- **Call-Chain Mirroring:** Tests that replicate internal logic instead of testing visible behavior.
- **Mock-Heavy Verification:** Tests whose primary logic consists of setting up mocks rather than verifying domain logic. If mocking is substantially larger than the assertion, the test design is flawed.

### 6.2 Delete vs. Refactor Rule

- **DELETE** if a test provides no clear business or architectural value.
- **DELETE** if a test artificially inflates coverage but would not catch a real regression.
- **REFACTOR** if a test covers a valuable contract but is written in a brittle way.

### 6.3 Guidelines for AI Agents

- **Check Before Adding:** Before adding a new test, verify whether an existing higher-level test already covers the same failure space.
- **Prioritize Simplicity:** Favor simplicity and readability over exhaustive completeness.
- **Avoid Coverage-Driven Bloat:** Do not generate tests solely to increase coverage.
- **Document Intent:** New tests must clearly state (via naming or docstrings) the specific behavior they are safeguarding.

---

## 7. Naming Conventions

| Element | Convention | Example |
| --- | --- | --- |
| Test file | `test_<module>.py` | `test_tensile.py` |
| Test class | `Test<Feature>` | `TestLoadTensileTestTXT` |
| Test function | `test_<behavior>` | `test_rejects_missing_columns` |

Test names should describe the **expected behavior**, not the implementation detail.

---

## See Also

- `AGENTS.md` §4 — Testing Rules (markers, directory structure)
- `pyproject.toml` `[tool.pytest.ini_options]` — Registered markers
- `docs/development/milestones/v0.3.0_sensor_loaders.md` — Gatekeeper test specifications
