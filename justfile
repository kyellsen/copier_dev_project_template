# === Default ===

# Show all recipes, grouped by section
default:
    @just --list --unsorted

# === Setup ===

# Wire the versioned pre-commit hook into this clone
[group('setup')]
install-hooks:
    git config core.hooksPath scripts/git-hooks
    @echo "✅ core.hooksPath → scripts/git-hooks"

# === House rules ===

# Refresh both AGENTS.canon.md copies from ~/code/_templates/agents_canon
[group('plumbing')]
canon-pull:
    @~/code/_templates/agents_canon/sync.sh .
    @~/code/_templates/agents_canon/sync.sh template

# Report whether this repo's canon pins are behind the canon repo
[group('plumbing')]
canon-outdated:
    @cd ~/code/_templates/agents_canon && just outdated

# === Quality ===

alias c := check

# Static gate: canon integrity in both copies, plus a real render of the template
[group('daily')]
check: check-canon check-render

# AGENTS.canon.md is generated — a hand edit would fork the house rules silently
[group('plumbing')]
check-canon:
    #!/usr/bin/env bash
    set -euo pipefail
    # Two copies live here: this repo's own, and the one shipped into projects.
    for dir in . template; do
      have=$(sha256sum "$dir/AGENTS.canon.md" | cut -c1-64)
      want=$(sed -n 's/^sha256: //p' "$dir/.agents-canon")
      test "$have" = "$want" \
        || { echo "❌ $dir/AGENTS.canon.md was edited by hand — run 'just canon-pull' or restore it"; exit 1; }
    done
    echo "✅ canon integrity — $(sed -n 's/^version: //p' .agents-canon)"

# Render into a throwaway project and check it came out whole
[group('plumbing')]
check-render:
    #!/usr/bin/env bash
    set -euo pipefail
    # A template that renders in your head is not a template that renders.
    #
    # --vcs-ref HEAD on a local path includes the dirty working tree, so this
    # gates what you are about to commit rather than what you last committed.
    # The module name is deliberately long and awkward: identifier length and
    # underscores are where the Jinja paths break first.
    OUT=$(mktemp -d)
    trap 'rm -rf "$OUT"' EXIT
    # Output is held back and only shown on failure: copier warns on every run
    # that it included the dirty tree, which is exactly what we asked it to do.
    if ! log=$(uv run --no-project --with copier copier copy --defaults --quiet --vcs-ref HEAD \
        --data python_module_name=a_very_long_generated_module_name_here \
        "$(pwd)" "$OUT" 2>&1); then
      printf '%s\n' "$log"
      echo "❌ the template does not render"
      exit 1
    fi

    # The shipped canon must survive templating with its pin intact.
    have=$(sha256sum "$OUT/AGENTS.canon.md" | cut -c1-64)
    want=$(sed -n 's/^sha256: //p' "$OUT/.agents-canon")
    test "$have" = "$want" || { echo "❌ the generated project's canon pin does not match its file"; exit 1; }

    # A justfile broken by Jinja fails here and nowhere else until someone uses it.
    just --justfile "$OUT/justfile" --working-directory "$OUT" --list >/dev/null

    # Same for the Python that came out of .jinja templates.
    uv run --no-project python -m compileall -q "$OUT/src" "$OUT/scripts" >/dev/null

    echo "✅ template renders: canon pin intact, justfile parses, generated Python compiles"

# Generate a throwaway project and keep it, for looking at the result by hand
[group('daily')]
probe target="/tmp/probe-dev-project":
    rm -rf "{{ target }}"
    uv run --no-project --with copier copier copy --vcs-ref HEAD "$(pwd)" "{{ target }}"
    @echo "✅ probe in {{ target }} — throwaway, never 'copier update' from an untagged state"

# There is no tier beyond the gate here: check-render already generates a real
# project from the working tree, which is this repository's only real test.

# The CI entry point — same gate as 'check'
[group('plumbing')]
ci: check
