# Style Audit — mccall_model_with_separation

- **Series:** lecture-dp
- **File:** `lectures/mccall_model_with_separation.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Sentence-case headings throughout. |
| Math         | 8/10  | `{\mathbb E}` brace style; no other issues. |
| Code         | 6/10  | Installs `myst-nb` (unusual — likely a leftover); Unicode Greek; pip at top. |
| JAX          | out of scope | uses JAX, but JAX rules out of scope. |
| Figures      | 9/10  | No matplotlib titles; lowercase labels; no figsize. |
| References   | 10/10 | Single `{cite}` parenthetical. |
| Links        | 9/10  | `{doc}` used 6×; no raw cross-series URLs. |
| Admonitions  | 9/10  | One `{exercise}` + `solution-start` with `:label:` and dropdown. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-003]** — pip install includes `myst-nb` (line 40), which is a build-time dependency, not a runtime lecture requirement. Should be removed.

### Low severity
- **[qe-math-A1]** — Single expectation appears as `{\mathbb E}` (line 88) — acceptable but slightly nonstandard brace usage; preferred `\mathbb{E}`.
- **[qe-writing-001]** — A few paragraphs run two sentences (e.g. 220-221, 280, 310-311).

## Strengths
- Lecture title correctly Title Case.
- All H2/H3 headings sentence case.
- Equation labels and `{eq}` cross-references used consistently.
- "IID" correct.
- No bold vectors, transpose, align, or `\tag` issues.
- Unicode Greek; pip install at top.
- `{doc}` used for cross-series.
- Exercise uses `{exercise}` + `solution-start` with dropdown.
- No matplotlib titles, no figsize, no spine, no Title-Case axis labels.

## Recommended actions
1. Remove `myst-nb` from the pip install on line 40 (build-time dep, not user-facing).
2. Normalise `{\mathbb E}` to `\mathbb{E}` on line 88.
3. Optional: split a handful of two-sentence paragraphs.
