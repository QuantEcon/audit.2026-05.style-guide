# Style Audit — markov_jump_lq

- **Series:** lecture-dp
- **File:** `lectures/markov_jump_lq.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 6.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Mostly sentence-case headings. |
| Math         | 3/10  | Apostrophe transpose throughout; `\cal N`; bare `E`; `i.i.d.`. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8 generally OK; no figsize. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 4/10  | Six `ax.set_title(...)` calls — embedded matplotlib titles violate qe-fig-003. |
| References   | 9/10  | Citations parenthetical via `{cite}`; no narrative-author misuse. |
| Links        | 7/10  | One raw markdown link to `python.quantecon.org`; `{doc}` used in 3 places. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Apostrophe `'` used as transpose throughout the Riccati derivation. *Lines:* 81, 94, 108, 114-115, 122, 128, 169, 191, 197, 200, 206-208, 217, 219-220, 225, 231-232. *Count:* 25+ occurrences.
- **[qe-fig-003]** — Six embedded matplotlib titles via `ax.set_title(...)`. *Lines:* 488, 550, 619, 660, 682, 716. Captions should be in MyST `{figure}` blocks, not embedded.

### Medium severity
- **[qe-math-011 (proposed)]** — Multivariate normal written as `{\cal N}(0,I)` (line 180). Style is plain `N(0, I)`.
- **[qe-writing-009 (proposed)]** — `i.i.d.` used in narrative (line 179). Should be `IID`.
- **[qe-math-010 (proposed)]** — Bare `E` used for expectation in display equations (lines 94, 163, 207). Style is `\mathbb{E}`.
- **[qe-link-002]** — Raw markdown link to `python.quantecon.org/markov_perf.html` (line 1411); should be `{doc}` form.
- **[qe-writing-009 (proposed)]** — Smart quotes ’ in narrative (lines 156, 157).

### Low severity
- **[qe-writing-001]** — Several multi-sentence paragraphs.

## Strengths
- Lecture title in correct Title Case.
- H2 headings sentence case ("Overview", "Review of useful LQ dynamic programming formulas", "Linked Riccati equations for Markov LQ dynamic programming", "Applications", "Example 1", "Example 2", "More examples").
- Matrices use `bmatrix` (13 matrix blocks).
- Definitions bolded.
- Equation labels and `{eq}` references used cleanly.
- pip install at top; Unicode Greek in code.
- No `\tag`, no `align`-inside-`$$` issues; no figsize, no Title-Case axis labels.

## Recommended actions
1. Replace every `'` used as transpose with `^\top` (highest priority).
2. Remove the six `ax.set_title(...)` calls; if a label is needed, use a `{figure}` block with caption.
3. Replace `{\cal N}` with plain `N`.
4. Replace `i.i.d.` with `IID`.
5. Replace bare `E` with `\mathbb{E}`.
6. Convert markdown URL to `python.quantecon.org/markov_perf.html` into a `{doc}` reference.
