# LOGBOOK — copier_dev_project

Dated incidents: what went wrong, how it was diagnosed, and the command that
proves it. The rules they bought stand in [`AGENTS.md`](AGENTS.md), the house
rules in `AGENTS.canon.md`; neither carries a date.

What breaks in a template is the render, so most of what follows was found in
a *generated* project rather than here. `just probe` reproduces that project,
and `just check-render` is usually the assertion that came out of the finding.

---

## 2026-08-17 — the base scaffold carried a quarter of a Gutachten

The template shipped about 690 lines of expert-report content to every project
generated from it, a plain data analysis included: the Massgaben, the canonical
chapter skeleton, a tree-cadastre CSV with schema and validator, the FLL
bibliography corpus, the Gutachten cover, footer and signature block, and the
`deliver` recipe. Among it a **hard-coded private postal address** and a stale
duplicate bibliography that no longer matched the one in use.

Diagnosed by reading the render rather than the template: what a code project
received was visibly a report. `git show --stat v3.0.0` lists what came out.

All of it moved into overlay repositories — `gutachten_bausteine` and
`thesis_bausteine` — applied as a second copier layer on top of a project
generated here. Commit `b279855`.

## 2026-08-18 — a copier update would have dropped a canon profile

The template shipped `AGENTS.canon.md` and `.agents-canon` itself, so it
carried a second copy of the house rules with **its own** profile list and
offered that copy to every project on `copier update`. An update to a report
would have silently replaced `00-core,10-python,40-science` with the template's
`00-core,10-python`, dropping the science profile.

The failure mode is what made it worth a rule: the project's own gate then
reports `AGENTS.canon.md` as hand-edited, with no hint where the change came
from — the file was replaced by a template nobody was looking at.

Both files are gone from `template/`; a generated project fetches them itself
with `just canon-pull`. `just check-render` now asserts the opposite of what it
used to (`test ! -e "$OUT/AGENTS.canon.md"`). Commit `134dafd`.

## 2026-08-21 — a Gutachten was scaffolded with VISION.md and ROADMAP.md

`include_vision_roadmap` defaulted to yes and was asked flat, so the report
`2026-08-13_klettergarten_weissenhaus` arrived with the planning files of a
software project — the why as a north star, the when as milestones. A report
has neither: its goal stands in the commission, its date in the deadline. The
files were deleted by hand in that repository.

Diagnosed there, not here: nothing in the template was wrong on its own, the
code-vs-text distinction was simply asked one flag at a time. `project_kind`
now asks it once and the flags derive their default from it. Commit `41fdd3f`.

That fix also introduced a `when:` clause, which turned out to be the next
entry.

## 2026-08-26 — `just test` was red in every generated project from day one

`pytest tests/integration` on a directory that does not exist is exit 4, a
usage error, and the recipes tolerate only exit 5 ("nothing collected"). The
directory did not exist because `copier.yml` excludes `**/.gitkeep` from the
render, and `tests/integration/` and `tests/system/` held nothing else — so a
placeholder that the render drops left the tier missing entirely.

It survived that long because `just check`, the gate everyone actually runs,
was green: only `just test` and `just ci` were red, and nobody read that as a
template bug.

Proof, before the fix: `just probe && cd /tmp/probe-dev-project && just test`
answered 4. Each tier now ships a real marked `test_smoke.py`, and
`check-render` asserts that all three arrive populated. Commit `1138226`.

## 2026-09-03 — a `when:` clause deleted 159 lines on a routine update

`include_vision_roadmap` carried `when: project_kind == 'code'`, which
suppressed the question entirely for a report or a thesis. A suppressed
question does **not** fall back to its default — copier drops the recorded
answer, so a `true` already sitting in an answers file becomes a deletion on
the next update.

Measured on `ba_ks`, a thesis that genuinely plans in the repository:
correcting `project_kind` from `code` to `thesis` deleted `ROADMAP.md` and
`VISION.md`, 159 lines, inside an otherwise routine `copier update`. The
repository had been holding a deliberately wrong answer to avoid exactly that,
which is how the mechanism came to light at all.

The `when:` is gone; the default is derived instead and the question is asked
every time. Verified against the dirty tree in all three cases: thesis with an
explicit `true` keeps both files, thesis on the default gets neither, code is
unchanged. Commit `e518bca`.
