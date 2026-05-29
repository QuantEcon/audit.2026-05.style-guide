# Style Audit — BCG_complete_mkts

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/BCG_complete_mkts.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 7/10  | `{\mathcal N}` for Normal; otherwise mostly compliant. |
| Code         | 7/10  | `alpha`, `beta`, `gamma` spelled out instead of unicode; install cell at top. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | Two `figsize=` settings without justification; no `:name:` fields. |
| References   | 8/10  | `{cite}` used consistently; no `{cite:t}` in-text use even where author named. |
| Links        | 6/10  | Two raw `python.quantecon.org` URLs alongside `{doc}` use. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-011 (proposed)]** — `{\mathcal N}` used as Normal distribution. *Example:* `lectures/BCG_complete_mkts.md:140`, `lectures/BCG_complete_mkts.md:146`. *Count:* 2 occurrences.
- **[qe-link-002]** — Raw `python.quantecon.org` URLs used for cross-series references; should use `{doc}` with intersphinx prefix. *Example:* `lectures/BCG_complete_mkts.md:56-57` (`cass_koopmans_1`, `rational_expectations`). *Count:* 2 occurrences.
- **[qe-code-002]** — `alpha`, `beta`, `gamma` spelled out in code instead of unicode (`α`, `β`, `γ`). *Count:* ~4 parameter assignments.

### Low severity
- **[qe-writing-006]** — Sub-subheadings such as `### Technology:` and `### Preferences:` (L104, L115) have trailing colons.
- **[qe-fig-001]** — Two `figsize=` settings (L955 `(8,7)`, L1092 `(14,6)`) without clear justification.
- **[qe-fig-005]** — Figures lack `:name:` fields, blocking `{numref}` cross-referencing.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case overall (qe-writing-006).
- `\begin{bmatrix}` used; no `array`/`pmatrix`.
- One-sentence paragraph rule mostly respected (qe-writing-001).
- Install cell at top with `hide-output` tag (qe-code-003).
- The many `'` characters are utility derivatives (`u'(c)`) — not transpose; no qe-math-002 violation.

## Recommended actions
1. Convert `{\mathcal N}` to `N` for the Normal distribution (qe-math-011, proposed).
2. Replace raw `python.quantecon.org` URLs with `{doc}\`intermediate:cass_koopmans_1\`` style links (qe-link-002).
3. Switch spelled Greek parameter names to unicode in code cells (qe-code-002).
4. Add descriptive `:name: fig-...` fields to figures for `{numref}` use (qe-fig-005).
