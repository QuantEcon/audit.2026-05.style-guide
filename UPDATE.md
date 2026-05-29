# UPDATE.md — how to re-run the audit and refresh this report

This is the runbook for reproducing the style audit and updating every document in this repo. Pair it with [`ROADMAP.md`](ROADMAP.md) (direction and open decisions) and the [scoring spec](lectures/spec.md) (the rubric the audit applies).

---

## Source of truth

**This git repository is the single source of truth for the audit report.** The published site at <https://quantecon.github.io/audit.2026-05.style-guide/> is built from `lectures/` by `.github/workflows/deploy.yml` on every push to `main`.

> ⚠️ Earlier working-tree copies under `…/claude-code/quantecon-style-audit/` are **superseded snapshots** taken before the cleanup/restructure (they still carry `# Style Audit —` titles, `Spec version` lines, `qe-*-A#` placeholder IDs, and v1/v2 "carry-forward" wording). Do not edit or copy from them. The only material that lived *only* there is the `action-style-guide-contributions/` drafts (the source for posted issues [#18–#21](https://github.com/QuantEcon/action-style-guide/issues/18)); if you want them version-controlled, vendor them into a top-level `contributions/` folder here.

---

## Update in place, or start a new audit period?

- **Correcting or refreshing *this* audit (May 2026)** → edit the documents in this repo and push. The process below regenerates them.
- **A new audit period (e.g. another month)** → create a fresh repo `audit.YYYY-MM.style-guide` from this one as a template (see [§ Starting a new audit period](#starting-a-new-audit-period)). The date-stamped repo convention is described in `ROADMAP.md`; the move toward a durable, regularly-updated model is an open decision there.

---

## Inputs

| Input | Location (local checkout) | Role |
|-------|---------------------------|------|
| The 5 lecture series | `…/quantecon/lecture-python-intro/lectures/`, `…/lecture-python-programming/lectures/`, `…/lecture-python.myst/lectures/`, `…/lecture-python-advanced.myst/lectures/`, `…/lecture-dp/lectures/` | The lectures being audited |
| Canonical rules | `…/quantecon/action-style-guide/style_checker/rules/*.md` (8 category files) | The rule definitions — **never redefined here**, only consumed |
| Scoring spec | `lectures/spec.md` (this repo) | Rubric, severity tiers, report templates |

JAX rules are **out of scope** for this corpus (they target `lecture-jax`).

---

## The process

### Step 1 — Scope each series

List the `.md` lectures per series (exclude build artefacts). Roughly: intro 51, programming 26, python.myst 110, advanced 62, dp 50 (≈299 total — re-count, the lecture repos change).

### Step 2 — Fan out one agent per series

Spawn one subagent per series, in parallel. Each agent receives: the [scoring spec](lectures/spec.md), the 8 rule files, and the per-lecture + per-series templates (spec §6–§7).

> 🔑 **Sandbox gotcha:** subagents can only read outside the current working directory when **auto mode is ON**. With auto mode off, every read of the lecture repos / rule files is denied and the run stalls. Turn auto mode on before fanning out (this bit us once during the original run).

### Step 3 — Each agent produces reports

Per lecture: one report at `lectures/<series>/<stem>.md` using the spec §6 template. Per series: a rollup at `lectures/<series>/index.md` using the spec §7 template.

### Step 4 — Enforce the conventions (the cleanup is baked into the spec now)

These are non-negotiable so the report stays consistent and readable. The spec already states them; verify after the agent run with the [residue checks](#residue-checks) below.

- **Canonical `qe-*` rule IDs only.** No legacy `W#`/`M#`. No `qe-*-A#` placeholders.
- **Proposed rules tagged `(proposed)`** wherever they appear, e.g. `qe-math-010 (proposed)`. The 7 proposed IDs are `qe-writing-009`, `qe-math-010`…`qe-math-015` (see spec §3).
- **No two-pass / v1-v2 / "carry-forward" narrative.** The report reads as one audit.
- **Titles:** per-lecture report H1 = the bare lecture stem (`# lqcontrol`); series `index.md` H1 = `# Summary`. No `# Style Audit —` prefix (it's noise in the sidebar).
- **No `Spec version` metadata line** in report headers.
- **Scoring:** 0–10 per category; overall = mean of in-scope categories; priority buckets HIGH/MEDIUM/LOW/NONE per spec §4. Severity tiers Critical/High/Medium/Low per spec §5.
- **JAX = "out of scope"** in the metadata (distinct from `N/A`, which means "not applicable to this lecture").

### Step 5 — Refresh the aggregate documents (manual, from the series numbers)

After the per-series outputs exist, update the cross-repo documents **by hand** from the series averages/counts:

| Document | What to update |
|----------|----------------|
| [`lectures/charts.md`](lectures/charts.md) | The inline data block: `scores` (series × category), `priority` (HIGH/MED/LOW/NONE per series), `systemic_rules` + `systemic_counts`, and the `weights` (lecture counts). Charts regenerate at build time. |
| [`lectures/intro.md`](lectures/intro.md) | The triage front page: attention tiers + "needs work" counts in **Where to focus**, the reach numbers in **The biggest wins**, and the **Fix immediately** build-risk rows. |
| [`lectures/details.md`](lectures/details.md) | Full scoreboard, the complete systemic-issue list, the full HIGH-priority lecture list, the remediation plan. |
| [`README.md`](README.md) | The repo-landing scoreboard table. |

> 📌 The chart data is currently inline in `charts.md`. Per `ROADMAP.md`, when this becomes a recurring pass, move it to a versioned `lectures/data/scores.csv` so trends can be charted across audit dates. Until then, keep the four documents above numerically consistent with each other.

### Step 6 — Regenerate the TOC (only if lectures were added/removed)

```bash
cd lectures
python3 - <<'PY'
import os
series_order = ['lecture-python-intro','lecture-python-programming',
                'lecture-python.myst','lecture-python-advanced.myst','lecture-dp']
lines = ['format: jb-book','root: intro','parts:',
         '  - caption: Overview','    chapters:',
         '      - file: charts','      - file: details','      - file: spec','      - file: appendix']
for folder in series_order:
    files = sorted(f[:-3] for f in os.listdir(folder)
                   if f.endswith('.md') and f != 'index.md')
    lines += [f'  - caption: "{folder} ({len(files)} lectures)"',
              '    chapters:', f'      - file: {folder}/index',
              '        sections:']
    lines += [f'          - file: {folder}/{s}' for s in files]
open('_toc.yml','w').write('\n'.join(lines) + '\n')
print('wrote _toc.yml')
PY
```

### Step 7 — Build and deploy

```bash
git add -A && git commit -m "Refresh audit — <period>" && git push origin main
# GitHub Actions builds lectures/ and deploys to Pages. Watch it:
gh run watch "$(gh run list --limit 1 --json databaseId -q '.[0].databaseId')" --exit-status
```

The build uses **vanilla jupyter-book + `quantecon-book-theme`** (pinned in `requirements.txt`) — no QuantEcon build container. Charts execute at build time, so `matplotlib`/`numpy` must stay in `requirements.txt`.

---

## Residue checks

Run from `lectures/` after any agent re-run to confirm the conventions held (all should report `0`):

```bash
# legacy / placeholder rule IDs
grep -rlE 'qe-(math|writing)-A[0-9]' lecture-*/*.md | wc -l
grep -rlE '\[(W[1-8]|M1[0-4]|M[1-9])\]' lecture-*/*.md | wc -l
# leftover prefixes / metadata / two-pass wording
grep -rlE '^# Style Audit —' lecture-*/*.md | wc -l
grep -rl 'Spec version' lecture-*/*.md | wc -l
grep -rilE 'carry-forward|carries forward|carried forward' lecture-*/*.md | wc -l
grep -rnE '\bv1\b|\bv2\b' lecture-*/*.md | grep -v 'supply_demand_foundations_v2' | wc -l
```

## Cleanup one-liners (if an agent re-introduces old conventions)

```bash
cd lectures
# A-placeholder IDs -> permanent (proposed)
find lecture-* -name '*.md' -print0 | xargs -0 perl -i -pe '
  s/qe-writing-A1/qe-writing-009 (proposed)/g; s/qe-math-A1/qe-math-010 (proposed)/g;
  s/qe-math-A2/qe-math-014 (proposed)/g; s/qe-math-A3/qe-math-011 (proposed)/g;
  s/qe-math-A4/qe-math-015 (proposed)/g; s/qe-math-A5/qe-math-012 (proposed)/g;
  s/qe-math-A6/qe-math-013 (proposed)/g;'
# strip report-title prefix
find lecture-* -name '*.md' ! -name 'index.md' -print0 | xargs -0 perl -i -pe 's/^# Style Audit — (.+)$/# $1/'
for f in lecture-*/index.md; do perl -i -pe 's/^# Style Audit — .+$/# Summary/' "$f"; done
# drop "Spec version" metadata line
find lecture-* -name '*.md' -print0 | xargs -0 perl -i -0777 -pe 's/^- \*\*Spec version:\*\* v2\n//mg'
```

---

## Repository layout

```
audit.2026-05.style-guide/
├── README.md                     repo landing (scoreboard + links)
├── ROADMAP.md                    direction, phases, open decisions
├── UPDATE.md                     this runbook
├── requirements.txt              build deps (pinned)
├── contributions/                source behind the action-style-guide issues (#18–#21)
│   ├── README.md                 status + index of the contributions
│   ├── issues/                   the 4 posted issue bodies (kept in sync with GitHub)
│   └── rule-drafts/              7 ready-to-merge rule entries (pending #18)
├── .github/workflows/deploy.yml  build + deploy to GitHub Pages
└── lectures/                     Jupyter Book source (published)
    ├── _config.yml, _toc.yml, _static/
    ├── intro.md                  front-page triage  ← refresh in Step 5
    ├── details.md                full findings      ← refresh in Step 5
    ├── charts.md                 visual summary + inline data  ← refresh in Step 5
    ├── spec.md                   scoring rubric + templates
    ├── appendix.md               feedback to style guide & action-style-guide
    └── lecture-<series>/
        ├── index.md              series "Summary" rollup  ← from agents (Step 3)
        └── <stem>.md             one per lecture          ← from agents (Step 3)
```

---

## Known follow-ups (also in ROADMAP)

- `actions/deploy-pages@v4` runs on Node 20 (GitHub deprecation mid-2026) — bump when convenient.
- Move chart data from inline (`charts.md`) to `lectures/data/scores.csv` to enable cross-period trend charts.
- Two build-risk findings should be fixed in the lecture repos regardless of audit cadence: `lecture-python.myst/divergence_measures.md:134` (`align` inside `$$`) and `cross_product_trick.md:133` (broken `{eq}` ref).

---

## Starting a new audit period

```bash
NEW=audit.2026-08.style-guide   # adjust YYYY-MM
gh repo create QuantEcon/$NEW --public --clone
# copy the scaffolding (not the old findings):
cp -r lectures/_config.yml lectures/_static lectures/spec.md lectures/charts.md \
      requirements.txt ROADMAP.md UPDATE.md .github  ../$NEW/   # adjust into lectures/ as needed
# then: run Steps 1–7, regenerate _toc.yml, refresh intro/details/README, enable Pages:
gh api -X POST repos/QuantEcon/$NEW/pages -f build_type=workflow
```

Carry forward `spec.md`, `charts.md` (as a template — replace the data), `_config.yml`, `requirements.txt`, the workflow, `ROADMAP.md`, and this file. Generate fresh per-lecture reports, series summaries, `intro.md`, and `details.md`.
