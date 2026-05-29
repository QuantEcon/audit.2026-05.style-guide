# BCG_incomplete_mkts

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/BCG_incomplete_mkts.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.6 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | Sentence-case headings; some long paragraphs; trailing colons in subheadings. |
| Math         | 6/10  | Bare `E[...]` in code comments and `{\mathcal N}` for Normal. |
| Code         | 7/10  | `alpha`, `beta` spelled out; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | Two `figsize=` settings; no `:name:` fields. |
| References   | 8/10  | `{cite}` used; `{cite:t}` never used despite some narrative author references. |
| Links        | 8/10  | Cross-series references use `{doc}`; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-010 (proposed)]** — Bare `E[...]` in code comments. *Example:* `lectures/BCG_incomplete_mkts.md:885`, `:915`, `:1450`, `:1472`, `:1502`. *Count:* 5 occurrences.
- **[qe-math-011 (proposed)]** — `{\mathcal N}` used as Normal distribution. *Example:* `lectures/BCG_incomplete_mkts.md:201`, `:207`. *Count:* 2 occurrences.
- **[qe-code-002]** — `alpha`, `beta` spelled out in code instead of unicode (`α`, `β`). *Count:* ~4 parameter assignments.

### Low severity
- **[qe-writing-006]** — Trailing colons in subheadings: `### Feasibility:` (L182), `### Preferences:` (L212).
- **[qe-writing-001]** — Some compound paragraphs near equilibrium discussion.
- **[qe-fig-001]** — `figsize=` set without justification (2 occurrences).
- **[qe-fig-005]** — Figures lack `:name:` fields.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case overall (qe-writing-006).
- `\begin{bmatrix}` used throughout.
- Many primes are derivatives (`u'`, `f'`) — no qe-math-002 violation.
- Cross-series references all use `{doc}\`intermediate:...\`` (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace `{\mathcal N}` with `N` (qe-math-011, proposed).
2. Use `\mathbb{E}` in code comments and prose (qe-math-010, proposed).
3. Switch spelled Greek parameter names to unicode (qe-code-002).
4. Remove trailing colons in subheadings (qe-writing-006).
5. Add `:name: fig-...` to figure-producing cells (qe-fig-005).
