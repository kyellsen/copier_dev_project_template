# === Default ===

# Show all recipes, grouped by section
default:
    @just --list --unsorted

# === Setup ===

# Wire the versioned git hooks into this clone (rung 'gate': commit-msg + pre-commit)
[group('setup')]
install-hooks:
    git config core.hooksPath scripts/git-hooks
    @echo "✅ core.hooksPath → scripts/git-hooks"

# === House rules ===

# Refresh AGENTS.canon.md from ~/code/_templates/agents_canon
[group('plumbing')]
canon-pull:
    @~/code/_templates/agents_canon/sync.sh .

# Report whether this repo's canon pin is behind the canon repo
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
    # One copy, this repo's own. The template used to carry a second one and
    # ship it into every generated project — see AGENTS.md, "Canon in every
    # generated project", for why that had to go.
    have=$(sha256sum AGENTS.canon.md | cut -c1-64)
    want=$(sed -n 's/^sha256: //p' .agents-canon)
    test "$have" = "$want" \
      || { echo "❌ AGENTS.canon.md was edited by hand — run 'just canon-pull' or restore it"; exit 1; }
    echo "✅ canon integrity — $(sed -n 's/^version: //p' .agents-canon)"

# Render into a throwaway project and check it came out whole
[group('plumbing')]
check-render:
    #!/usr/bin/env bash
    set -euo pipefail
    # A template that renders in your head is not a template that renders.
    #
    # The gate has to judge the working tree, uncommitted changes included, so
    # that it reports on what you are about to commit. `--vcs-ref HEAD` on a
    # dirty local path does that — but it makes copier build a tree in THIS
    # repository, and while git holds .git/index.lock that fails with "Error
    # building trees". The one caller that always holds that lock is the
    # pre-commit hook which runs this gate, so the gate could not run inside its
    # own hook. Copying the working tree into a throwaway repository once and
    # rendering from there removes the dependency: same input, no lock.
    SRC=$(mktemp -d) OUT=$(mktemp -d) RUNGS=$(mktemp -d)
    trap 'rm -rf "$SRC" "$OUT" "$RUNGS"' EXIT
    tar -cf - --exclude=./.git --exclude=./.venv . | tar -xf - -C "$SRC"
    git -C "$SRC" init -q
    git -C "$SRC" add -A
    git -C "$SRC" -c user.email=gate@local -c user.name=gate commit -qm "gate"

    # The module name is deliberately long and awkward: identifier length and
    # underscores are where the Jinja paths break first.
    render() { # render <destination> <extra copier --data args...>
      local dest=$1; shift
      uv run --no-project --with copier copier copy --defaults --quiet \
        --data python_module_name=a_very_long_generated_module_name_here \
        "$@" "$SRC" "$dest"
    }

    if ! log=$(render "$OUT" 2>&1); then
      printf '%s\n' "$log"
      echo "❌ the template does not render"
      exit 1
    fi

    # The opposite of what this used to assert: a generated project must arrive
    # WITHOUT a canon, and fetch it itself. Shipping one meant this template
    # carried a second copy with its own profile list and pushed it into every
    # project on update. See AGENTS.md, "Canon in every generated project".
    for f in AGENTS.canon.md .agents-canon; do
      test ! -e "$OUT/$f" || { echo "❌ the template still ships $f — projects must pull it themselves"; exit 1; }
    done
    grep -q 'canon-pull' "$OUT/justfile" || { echo "❌ the generated project has no canon-pull recipe"; exit 1; }

    # A justfile broken by Jinja fails here and nowhere else until someone uses it.
    just --justfile "$OUT/justfile" --working-directory "$OUT" --list >/dev/null

    # Same for the Python that came out of .jinja templates.
    uv run --no-project python -m compileall -q "$OUT/src" "$OUT/scripts" >/dev/null

    # Every tier arrives with a test in it. A tier directory that holds only a
    # .gitkeep does not arrive at all — copier.yml excludes those — and pytest
    # answers a missing directory with exit 4, which the recipes' `|| test $? -eq 5`
    # does not catch. `just test` was red in a fresh project for exactly that.
    for tier in unit integration system; do
      compgen -G "$OUT/tests/$tier/test_*.py" >/dev/null \
        || { echo "❌ tests/$tier arrives without a test — its 'just test-*' recipe would exit 4"; exit 1; }
    done

    # ── The hook ladder ────────────────────────────────────────────────────
    # The rung is encoded in the file NAMES, not in the file contents, and a
    # file whose name renders empty is one copier drops. Nothing but a real
    # render proves that still holds, so every rung gets one.
    HOOKDIR="template/scripts/{% if git_hooks != 'none' %}git-hooks{% endif %}"
    SRC_commit_msg="$HOOKDIR/{% if git_hooks != 'none' %}commit-msg{% endif %}"
    SRC_pre_commit="$HOOKDIR/{% if git_hooks in ['gate', 'full'] %}pre-commit{% endif %}"
    SRC_pre_push="$HOOKDIR/{% if git_hooks == 'full' %}pre-push{% endif %}"

    # This repository's own hooks are hand-copied from the ones it ships, and
    # until now nothing compared them. Both drifted apart once already — the
    # commit-msg hook arrived as two independent copies of the same file.
    cmp -s "$SRC_commit_msg" scripts/git-hooks/commit-msg \
      || { echo "❌ scripts/git-hooks/commit-msg has drifted from the copy the template ships"; exit 1; }
    cmp -s "$SRC_pre_commit" scripts/git-hooks/pre-commit \
      || { echo "❌ scripts/git-hooks/pre-commit has drifted from the copy the template ships"; exit 1; }
    # Rung 'gate' on purpose: this repository's 'ci' is only 'check', so there
    # is no test tier for a pre-push to add. See AGENTS.md, "The hook ladder".
    test ! -e scripts/git-hooks/pre-push \
      || { echo "❌ this repository stands on rung 'gate' — its ci is only 'check'"; exit 1; }

    for level in none message gate full; do
      R="$RUNGS/$level"
      if ! log=$(render "$R" --data git_hooks="$level" 2>&1); then
        printf '%s\n' "$log"
        echo "❌ the template does not render at git_hooks=$level"
        exit 1
      fi
      H="$R/scripts/git-hooks"

      # Every hook that arrives has to be byte-identical to its source and
      # executable — a hook copier rendered as a template, or dropped the mode
      # bit from, fails silently at the moment it is supposed to protect you.
      for pair in "commit-msg:$SRC_commit_msg" "pre-commit:$SRC_pre_commit" "pre-push:$SRC_pre_push"; do
        name=${pair%%:*}; src=${pair#*:}
        [ -e "$H/$name" ] || continue
        test -x "$H/$name" || { echo "❌ $level: $name arrives without the execute bit"; exit 1; }
        cmp -s "$src" "$H/$name" || { echo "❌ $level: $name did not arrive byte-identical"; exit 1; }
      done

      case "$level" in
        none)
          test ! -e "$H" || { echo "❌ none: scripts/git-hooks arrived anyway"; exit 1; }
          grep -q 'install-hooks' "$R/justfile" \
            && { echo "❌ none: the justfile still offers install-hooks"; exit 1; } || true
          ;;
        message)
          test -e "$H/commit-msg" || { echo "❌ message: commit-msg is missing"; exit 1; }
          for absent in pre-commit pre-push; do
            test ! -e "$H/$absent" || { echo "❌ message: $absent arrived above its rung"; exit 1; }
          done
          grep -q 'install-hooks' "$R/justfile" || { echo "❌ message: no install-hooks recipe"; exit 1; }
          ;;
        gate)
          for present in commit-msg pre-commit; do
            test -e "$H/$present" || { echo "❌ gate: $present is missing"; exit 1; }
          done
          test ! -e "$H/pre-push" || { echo "❌ gate: pre-push arrived above its rung"; exit 1; }
          ;;
        full)
          for present in commit-msg pre-commit pre-push; do
            test -e "$H/$present" || { echo "❌ full: $present is missing"; exit 1; }
          done
          # The rung's whole point: pre-push adds tests, and stops short of 'ci'.
          grep -q 'exec just check test$' "$H/pre-push" \
            || { echo "❌ full: pre-push does not run 'just check test'"; exit 1; }
          ;;
      esac

      # 'ci' is composition in every rung, never a mode inside check.py.
      grep -q '^ci: check test-all' "$R/justfile" \
        || { echo "❌ $level: ci is not composed from check and test-all"; exit 1; }
      just --justfile "$R/justfile" --working-directory "$R" --list >/dev/null
    done

    # The default for a code project is the top of the ladder.
    test -e "$OUT/scripts/git-hooks/pre-push" \
      || { echo "❌ project_kind=code does not default to git_hooks=full"; exit 1; }

    echo "✅ template renders: no canon shipped, canon-pull present, justfile parses, generated Python compiles, every test tier populated, all four hook rungs correct"

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
