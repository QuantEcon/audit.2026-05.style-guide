## Summary

The [May 2026 lecture style audit](https://github.com/QuantEcon/audit.2026-05.style-guide) produced rule-level violation data for **299 lectures across 5 series, scored against 7 of the 8 action-style-guide rule categories**: Writing, Math, Code, Figures, References, Links, Admonitions (JAX out of scope). This data may be useful to action-style-guide as:

- **Regression-test fixtures** for the planned Phase 4.3 deterministic checkers (covers 22 candidate rules — see [#19 — Phase 4.3 acceleration](https://github.com/QuantEcon/action-style-guide/issues/19))
- **Evaluation data** for prompt changes — does prompt rev N+1 still catch the same violations rev N caught?
- **Baseline measurement** for tracking whether the corpus improves over time

No commitment is being asked for. This issue is to surface the data and let the team decide whether/how to ingest it.

## What's in the audit data

Each of the 5 series has a published **Summary** page with:

- Per-lecture ranking tables showing scores in 7 categories
- Aggregate counts per rule ("N / total lectures") with lists of specific violating files
- Severity-bucketed top systemic issues

Every individual lecture also has its own published report (browsable in the report sidebar) with per-category scores and a severity-bucketed issue list — so the labelled data is directly inspectable, not just aggregated.

For example, from the [lecture-dp summary](https://quantecon.github.io/audit.2026-05.style-guide/lecture-dp/index.html):

> **`qe-math-002`** — Apostrophe `'` (and `^\prime`, `^T`) used as transpose. Appears in 11 / 50 lectures, often as the dominant math-style violation. Hits hardest in the LQ/DP-derivation lectures (`lqcontrol`, `lagrangian_lqdp`, `perm_income_cons`, `smoothing`, `markov_jump_lq`, `dyn_stack`, `lq_inventories`, `calvo_machine_learn`, `cross_product_trick`, `perm_income`, `mccall_q`).

That gives a concrete labelled set: 11 specific lectures known to violate `qe-math-002`. Per-rule labelled sets exist for all 22 deterministic candidates plus most LLM-only rules.

### Top rules by corpus evidence

The audit measured these rule violation counts across the 299-lecture corpus:

| Rule | Lectures affected |
|------|-------------------|
| `qe-writing-006` (Title Case headings) | ~170 |
| `qe-code-002` (Greek spelled out) | ~150 |
| `qe-fig-001` (unnecessary figsize) | ~125 |
| `qe-fig-005` (figures missing `:name:`) | ~120 |
| `qe-fig-003` (embedded titles) | ~90 |
| `qe-math-010` (`\mathbb{E}/P/V`, *proposed*) | ~60 |
| `qe-link-002` (raw cross-series URLs) | ~60 |
| `qe-fig-006` (Title Case axis labels) | ~50 |
| `qe-math-002` (`^\top` for transpose) | ~46 |
| `qe-ref-001` (`{cite}` vs `{cite:t}`) | ~37 + 2 series with zero `{cite:t}` usage |
| `qe-math-011` (distribution naming, *proposed*) | ~30 |
| `qe-writing-009` (IID, *proposed*) | ~30 |
| `qe-fig-007` (removed spines) | ~30 |

## Caveats — read before integrating

These are important and not glossed over:

1. **Calibration.** The audit was produced by parallel per-series subagents working from a shared [scoring spec](https://quantecon.github.io/audit.2026-05.style-guide/spec.html). Calibration is good but not perfect — expect some inter-series variance on borderline scores. Treat the counts as well-grounded estimates rather than exact tallies.

2. **The audit is a point-in-time snapshot.** Lecture content evolves; the violation counts will go stale as lectures get edited. Treat as a May 2026 baseline, not a live dataset.

3. **JAX out of scope.** The audit did not score JAX rules (`qe-jax-001` – `qe-jax-007`). Those are concentrated in `lecture-jax` which was not audited here. The corpus covers 7 of 8 categories.

4. **Two findings already need action regardless of how this issue progresses:**
   - **Build-risk:** [`lecture-python.myst/divergence_measures.md:134`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/divergence_measures.md#L134) — `\begin{align}` inside `$$` (violates `qe-math-006`). Would fail PDF builds.
   - **Broken cross-reference:** [`lecture-python.myst/cross_product_trick.md:133`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/cross_product_trick.md#L133) — `` {eq}`eq:Kalman102} `` has mismatched braces; label is attached to a bare `align*` block on line 121 rather than a numbered equation.

## Integration paths if the team wants the data

### Path 1 — Reference by commit SHA

Tests in action-style-guide reference a specific commit of the audit repo. When the team wants newer data, bump the SHA.

```python
AUDIT_FIXTURE_REF = "QuantEcon/audit.2026-05.style-guide@<commit-or-tag>"  # pin for reproducibility
```

### Path 2 — Vendor into `tests/fixtures/audits/2026-05/`

Copy the 6 rollup pages (the synthesis + 5 series summaries) into action-style-guide's test fixtures. Pros: self-contained. Cons: data duplicated, manual updates.

### Path 3 — Pull-as-needed in CI

CI job fetches the audit repo, runs candidate deterministic regexes against the lecture repos, compares against the audit's expected violations. Reports precision/recall per rule.

### Path 4 — No integration; reference informally

Treat the audit as a one-time external reference. The Phase 4.3 work can manually consult it during development.

## What's being asked

Nothing requiring action. This is an offer + a heads-up:

- If the data would be useful, the audit repo is public and stable.
- If the team prefers to generate its own test fixtures, that's fine — this audit doesn't claim to be authoritative.
- The two specific build-risk findings (`divergence_measures.md`, `cross_product_trick.md`) should be acted on regardless. I can open follow-up issues in [QuantEcon/lecture-python.myst](https://github.com/QuantEcon/lecture-python.myst) if useful.

## References

- **Audit repo:** https://github.com/QuantEcon/audit.2026-05.style-guide
- **Spec:** https://quantecon.github.io/audit.2026-05.style-guide/spec.html
- **Cross-series synthesis (with per-rule corpus counts):** https://quantecon.github.io/audit.2026-05.style-guide/intro.html
