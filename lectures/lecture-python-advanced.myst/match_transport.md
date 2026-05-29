# Style Audit — match_transport

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/match_transport.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.6 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Title in Title Case; sentence-case headings; some longer paragraphs. |
| Math         | 7/10  | Mixed `\mathbb{1}` / `\mathbf{1}`; primes are next-period notation, not transpose. |
| Code         | 6/10  | 9 spelled Greek; no install cell (uses scipy/networkx — networkx not in Anaconda). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 3/10  | 27 `figsize=` settings; 2 `spines.set_visible(False)`; no `:name:` fields. |
| References   | 8/10  | 10 `{cite}` used; never `{cite:t}`. |
| Links        | 7/10  | Two raw `python.quantecon.org`/`intro.quantecon.org` URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — `figsize=` set 27 times — systemic. *Count:* 27 occurrences.
- **[qe-fig-007]** — `ax.spines[...].set_visible(False)` used (2 occurrences) — should keep default box.

### Medium severity
- **[qe-math-008]** — Inconsistent indicator notation: `\mathbb{1}` (L222) and `\mathbf{1}_N` (L525). Should use `\mathbb{1}` consistently (carry-forward from v1 M3). *Count:* 1 `\mathbf{1}` occurrence.
- **[qe-link-002]** — Two raw cross-series URLs (`python.quantecon.org/opt_transport.html`, `intro.quantecon.org/lp_intro.html`). *Example:* `lectures/match_transport.md:40`, `:44`. *Count:* 2 occurrences.
- **[qe-code-006]** — `networkx` is not in Anaconda; missing install cell.
- **[qe-code-002]** — 9 spelled Greek (`alpha`, `gamma`) in code.

### Low severity
- **[qe-writing-005]** — Heavy bold for `**positive assortative**`, `**negative assortative**`, etc.; some definitional, some emphasis.
- The many primes (`x'`, `y'`) are primed variable names, not transpose — no qe-math-002 violation.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Title "Composite Sorting" in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- `\begin{bmatrix}` used where matrices appear (qe-math-003).
- Sequences `\{ ... \}` (qe-math-005).
- `\mathbb{R}`, `\mathbb{Z}_+` correctly used.
- Equation labels and `{eq}` references (qe-math-007).

## Recommended actions
1. Remove unnecessary `figsize=` settings (qe-fig-001).
2. Remove `spines.set_visible(False)` calls (qe-fig-007).
3. Standardise indicator notation on `\mathbb{1}` (qe-math-008).
4. Convert raw URLs to `{doc}\`intermediate:opt_transport\``, `{doc}\`intro:lp_intro\`` (qe-link-002).
5. Add install cell for `networkx` (qe-code-003, qe-code-006).
6. Convert spelled Greek to unicode in code (qe-code-002).
