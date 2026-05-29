# Roadmap

Living document for the QuantEcon lecture style-audit project. Tracks strategic direction, open design decisions, and pending work.

**Last updated:** 2026-05-28

---

## Where we are today

- **v1 audit complete** (2026-05-27) — Writing + Math conventions only, 292 lectures, 5 series. Used local `W1–W8` / `M1–M14` rule IDs.
- **v2 audit complete** (2026-05-28) — Extended to Code, Figures, References, Links, Admonitions (JAX out of scope). 299 lectures. Uses canonical `qe-*` rule IDs from [`QuantEcon/action-style-guide`](https://github.com/QuantEcon/action-style-guide).
- **4 issues opened** against `action-style-guide` ([#18](https://github.com/QuantEcon/action-style-guide/issues/18) new rules, [#19](https://github.com/QuantEcon/action-style-guide/issues/19) Phase 4.3 acceleration, [#20](https://github.com/QuantEcon/action-style-guide/issues/20) bulk audit mode discussion, [#21](https://github.com/QuantEcon/action-style-guide/issues/21) corpus offer).
- **Repo published** under the `audit.YYYY-MM.{topic}` convention. **Kept as an interim decision** — re-dated (new repo) on each re-run; see the §1 decision note.
- **Tier 2 dashboard live** (Phase 1 ✅) — the repo is now a Jupyter Book published to GitHub Pages at **https://quantecon.github.io/audit.2026-05.style-guide/**, with the cross-series synthesis, 4 charts, the scoring spec, and a drill-down report for all 299 lectures. Per-lecture reports are committed.

---

## 1. Strategic shift — from disposable to durable

> **Decision (2026-05, interim).** Keep the dated `audit.YYYY-MM.{topic}` convention — the date in the repo name is a useful at-a-glance freshness signal. On each re-run (per [`UPDATE.md`](UPDATE.md)) publish a **new dated repo** for the period (e.g. `audit.2026-08.style-guide`) and archive the prior one — *not* an in-place rename, which would break the published Pages URL and the already-posted issue links. The durable single-repo analysis in §1–§2 below is retained as reference for if/when audits become frequent enough to justify one persistent home; it is **not** the current plan.

The original framing treated each audit as a **time-bounded, disposable artifact**: one repo per audit, archive when stale, the date prefix signaling freshness. That convention made sense when audits were assumed to be infrequent and ad-hoc.

The **revised direction** treats the audit as a **persistent, regularly-updated quality resource**:

- A single durable repo, refreshed on a monthly pass
- Time-series violation counts visible across passes (did `qe-writing-006` drop from 170 lectures to 80?)
- Dashboards become a real, sustained asset — worth investing in
- Per-lecture reports become genuinely useful (drill-down from scoreboard works)
- A natural integration target for the bulk-audit capability proposed in `action-style-guide` [#20](https://github.com/QuantEcon/action-style-guide/issues/20)

**The `audit.YYYY-MM.{topic}` convention is not abandoned** — it remains a good fit for *episodic* one-off audits (security review of a release, a one-time deep-dive on a specific topic). But style-guide compliance is a *persistent* concern, and that calls for a durable home.

### Implications

- **The current repo name** (`audit.2026-05.style-guide`) needs to change — a stable repo shouldn't have a date prefix.
- **Per-lecture reports should now be committed.** Earlier the decision was "spec + 6 READMEs only" due to v1 calibration drift; that concern is largely resolved in v2, and the persistent model demands the per-lecture detail to make dashboards useful.
- **Cadence and automation matter.** A monthly pass needs orchestration — could be a scheduled GitHub Action, a Routine, or a manual ritual the team owns.
- **Issue [#20](https://github.com/QuantEcon/action-style-guide/issues/20) (bulk audit mode)** becomes more important. If `qestyle audit` ships in `action-style-guide`, this repo's monthly pass can be driven by it rather than by ad-hoc subagent orchestration.

---

## 2. Open design decisions

These are the questions the persistent model raises. None of them block today's audit data being useful, but they shape the next iteration.

### 2.1 Repo name

Options under consideration:

| Name | Pros | Cons |
|------|------|------|
| `QuantEcon/lecture-style-audit` | Clear scope; "lecture" anchors it to the corpus | Singular implies one-shot; would need `lecture-style-audits` (plural) for the time-series feel |
| `QuantEcon/lecture-quality` | Broader umbrella; could expand beyond style | Vague; what does "quality" mean operationally? |
| `QuantEcon/style-compliance` | Direct, professional | Less discoverable; "compliance" feels regulatory |
| `QuantEcon/style-audits` (plural) | Implies recurring snapshots; mirrors `lecture-jax`, `lecture-stats` naming | Slightly verbose |

**Tentative leaning:** `QuantEcon/style-audits` — plural form signals time-series intent, matches the org's `lecture-*` naming family.

### 2.2 Time-series storage

How do we model "audit from 2026-05" vs "audit from 2026-06" inside one repo?

- **Option A** — Per-pass subdirectory: `2026-05/`, `2026-06/`, … plus `latest/` symlink. Easy to compare; full history visible.
- **Option B** — Single `latest/` directory, full history via `git tag` per pass. Cleanest layout; need git operations to inspect history.
- **Option C** — Time-series CSV / JSON files keyed by pass-date in a single tree. Best for dashboards; loses per-pass markdown narratives.
- **Option D** — Hybrid: keep `latest/` markdown reports + a `history/violations.csv` time-series file. Best of both.

**Tentative leaning:** D (hybrid). Markdown for human reading, CSV for the dashboard's chart data.

### 2.3 Migration from `audit.2026-05.style-guide`

- **Option α** — Rename the current repo to its new name. Preserves history + the 4 GitHub-issue cross-links.
- **Option β** — Archive `audit.2026-05.style-guide` as the v1+v2 baseline; create a fresh `style-audits` repo and mirror the 2026-05 content under `2026-05/`. Cleaner conceptually; the disposable repo really is a snapshot.
- **Option γ** — Keep both: leave `audit.2026-05.style-guide` as the canonical v2 reference, point the new persistent repo at it for the 2026-05 entry.

**Tentative leaning:** β. The naming convention shift is meaningful; preserving the old repo as a clean baseline is honest about what changed.

### 2.4 Cadence + automation

- **Pure manual**: someone runs an audit each month, commits the output. Lowest infra cost; depends on someone remembering.
- **Scheduled Routine / GitHub Action**: cron-triggered, runs the audit, opens a PR with the new monthly data. Higher infra; consistent cadence; depends on `qestyle audit` or equivalent existing.
- **Triggered**: run on demand (e.g. before each lecture-series release). Quality-gate model rather than time-based.

**Tentative leaning:** start manual; move to scheduled once `action-style-guide` [#20](https://github.com/QuantEcon/action-style-guide/issues/20) is resolved. Both can coexist.

### 2.5 Per-lecture reports

Under the persistent model, the answer is clearly **commit them**. The remaining question is structure:

- **Flat under `<series>/`**: `lecture-dp/lqcontrol.md`. Simple; what we have locally.
- **Nested under `lectures/`**: `<series>/lectures/lqcontrol.md`. Mirrors the source repo layout; clearer separation of READMEs from per-lecture detail.

**Tentative leaning:** flat — fewer levels of nesting, current local layout already works.

---

## 3. Dashboard plans

### 3.1 Target tier

Three tiers were considered in discussion:

- **Tier 1 (minimum viable)** — Enable Jekyll on the markdown; commit per-lecture reports; wire scoreboard links. ~30 min.
- **Tier 2 (recommended for one-time)** — Jupyter Book + sidebar TOC + 4 embedded charts. Matches QE stack. ~2 hrs.
- **Tier 3 (right for persistent)** — Real dashboard with filters, search, sortable tables, time-series charts. Reusable infra. ~4–8 hrs initial + ongoing.

Under the persistent model, **Tier 3 becomes worth the investment** — the dashboard amortises across every monthly pass. Build Tier 2 first as a proof of concept, then upgrade to Tier 3 if regular use validates the value.

### 3.2 Charts worth building

1. **Heatmap** — 5 series × 7 categories, color-coded by score. At-a-glance weak-spot map.
2. **Top systemic issues bar chart** — `qe-writing-006` (170), `qe-code-002` (150), `qe-fig-001` (125) … sorted horizontal bars.
3. **Priority distribution stacked bar** — one stack per series.
4. **Lecture scatter** — each lecture as a dot, x = writing score, y = math score, colored by overall priority.
5. **Time-series rule violations** (Tier 3 only) — line chart showing how each top-15 rule has changed across audit passes.
6. **Score-delta chart** (Tier 3 only) — which lectures improved / regressed most between passes.

### 3.3 Tooling choice

| Tool | Effort | Match with QE stack | Tier fit |
|------|--------|---------------------|----------|
| Jekyll (default GH Pages) | low | low | Tier 1 |
| Jupyter Book | medium | **high** | Tier 2 |
| MkDocs Material | medium | low | Tier 2 |
| Custom Vue/React + Datasette | high | low | Tier 3 |
| Quarto + Observable embeds | medium-high | medium | Tier 2 / 3 |

**Tentative leaning:** Jupyter Book for Tier 2 (familiar to the team, matches lecture infra). For Tier 3, look at adding interactive Plotly/Altair embeds within Jupyter Book first before reaching for a custom dashboard.

### 3.4 Audience

- **Primary**: maintainers / triage team — scoreboard, cross-series patterns, sortable lecture lists.
- **Secondary**: lecture authors — search by name, "show me my lecture", drill-down with concrete actions.
- **Tertiary**: external visibility — clean public-facing landing page; demonstrates QE's quality discipline.

Tier 2 serves primary + secondary well. Tier 3 adds tertiary polish.

---

## 4. Pending external work

### 4.1 Awaiting feedback from `action-style-guide` team

The 4 issues opened on 2026-05-28 shape the persistent-audit plans:

| Issue | Outcome would unblock |
|-------|----------------------|
| [#18](https://github.com/QuantEcon/action-style-guide/issues/18) — 7 new style rules | Rule IDs we can use durably (vs the `qe-math-A*` placeholders) |
| [#19](https://github.com/QuantEcon/action-style-guide/issues/19) — Phase 4.3 acceleration | Deterministic checkers we can run cheaply on every monthly pass |
| [#20](https://github.com/QuantEcon/action-style-guide/issues/20) — Bulk audit mode | Automated monthly pass without ad-hoc subagent orchestration |
| [#21](https://github.com/QuantEcon/action-style-guide/issues/21) — Corpus as test fixtures | Tighter coupling between this audit's data and the tool that produces it |

### 4.2 Build-risk findings to surface against `lecture-python.myst`

Two findings should be filed as issues against `QuantEcon/lecture-python.myst` regardless of action-style-guide outcomes:

- [`lectures/divergence_measures.md:134`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/divergence_measures.md#L134) — `\begin{align}` inside `$$` (would break PDF builds; `qe-math-006`).
- [`lectures/cross_product_trick.md:133`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/cross_product_trick.md#L133) — broken `{eq}` reference (mismatched braces + label attached to bare `align*` block).

---

## 5. Phased plan

### Phase 0 — Stabilise current findings ✅
- v1 + v2 audits complete
- Spec v2 published
- 4 contribution issues opened against action-style-guide
- Initial public repo (`audit.2026-05.style-guide`) live

### Phase 1 — Build Tier 2 dashboard ✅ (done 2026-05-29)
- ✅ Jupyter Book with `quantecon-book-theme` in the repo (`lectures/`)
- ✅ Per-lecture reports committed (299) for drill-down
- ✅ 4 charts (heatmap, systemic-issues bars, priority stack, category averages) — built at build time from inline data
- ✅ Sidebar TOC: synthesis (root), spec, charts, 5 series rollups, per-series lecture lists
- ✅ Published to GitHub Pages via `.github/workflows/deploy.yml` → https://quantecon.github.io/audit.2026-05.style-guide/
- Follow-ups for a future pass: externalise chart data to `data/scores.csv`; bump `actions/deploy-pages` past the Node 20 deprecation; consider a landing/overview page distinct from the synthesis.

### Phase 2 — Repo naming (interim decision: keep the dated convention)
- **Resolved for now:** keep `audit.YYYY-MM.{topic}`; on each re-run stand up a new dated repo for the period (per `UPDATE.md` § Starting a new audit period) and archive the prior one.
- Revisit the durable single-repo options (§2) only if audits become frequent enough to justify it.

### Phase 3 — Establish monthly cadence
- First manual monthly pass (2026-06) using the same subagent orchestration as v2
- Document the procedure as a checklist in the repo
- Wire dashboard to ingest each new pass automatically

### Phase 4 — Tier 3 dashboard (conditional)
- Build interactive filters, sortable tables, time-series charts
- Only if Phase 3 validates ongoing team use of the Tier 2 dashboard

### Phase 5 — Automation
- Replace manual monthly pass with `qestyle audit` (once [#20](https://github.com/QuantEcon/action-style-guide/issues/20) lands) **or** with a scheduled GitHub Routine
- Open auto-PRs for each pass; human review before merge to `main`

---

## 6. Risks + known concerns

- **Subagent calibration drift** — visible in v1 (e.g. `lecture-python-programming` scoring zero HIGH despite systemic issues). v2 reduced this by anchoring each subagent to the v1 baseline, but each new monthly pass risks introducing fresh drift. Mitigation: deterministic rules (Phase 4.3 in action-style-guide) reduce reliance on judgment per pass.
- **Subagent sandbox permissions** — the v2 extension was blocked once when run outside auto-mode (subagents limited to `claude-code/` subtree). Mitigation: document the auto-mode requirement, or restructure so subagents only need local-scope access.
- **Audit cost at scale** — running every rule × every lecture via LLM is non-trivial ($24–116 per full pass at current per-rule architecture). Phase 4.3 deterministic checkers + sampling strategies make monthly cadence affordable.
- **Lecture content evolves** — violation counts go stale immediately after each pass. Monthly cadence is the right answer; time-series visibility is the win.
- **Repo naming** — resolved interim (keep the dated convention; a new dated repo per re-run; see §1). A move to a durable single repo is deferred until audits are frequent enough to warrant it; renaming the current repo is specifically avoided because it would break the published Pages URL and the posted issue cross-links.

---

## 7. Discussion notes captured during planning

Selected design moments worth preserving:

- **Why the convention shift matters:** disposable repos work for episodic audits but discourage dashboard investment. Persistent repos make dashboards an asset (amortised across every monthly pass), make time-series trends visible, and reduce friction for non-developer audiences.
- **Why per-lecture reports change from "don't commit" to "commit":** v2 calibration is good enough; persistent model means drill-down is essential; "spec + 6 READMEs only" only made sense for a snapshot.
- **Why Jupyter Book over MkDocs Material:** matches QE's lecture infra; team already knows how to read it; reduces cognitive overhead.
- **Why Tier 3 only after Tier 2 validates value:** dashboards risk becoming bespoke maintenance burdens. Prove the use case with a familiar stack before investing in custom infra.
- **Why issue [#20](https://github.com/QuantEcon/action-style-guide/issues/20) (bulk audit mode) became more strategic under the new direction:** if persistent + monthly, automating the pass via `qestyle audit` removes the orchestration cost of every pass.
