# Style Audit — hs_recursive_models

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/hs_recursive_models.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 4.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Sentence-case headings; many long paragraphs; bolded labels. |
| Math         | 2/10  | Pervasive bare `E_t`, `^\prime` and `^T` for transpose. |
| Code         | N/A   | no executable code cells |
| JAX          | N/A   | not a JAX lecture |
| Figures      | N/A   | no figures |
| References   | 7/10  | 13 `{cite}` used; multiple narrative author refs ("Rosen, Murphy, and Scheinkman (1994)", "Hansen, Sargent, and Roberts (1991)", "Attanasio and Pavoni (2011)") should use `{cite:t}`. |
| Links        | 4/10  | One raw `python-intro.quantecon.org` URL pair (L91); but heavy `{doc}` use (17 occurrences). |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Bare `E_t`, `E_0`, `E[...]` used throughout instead of `\mathbb{E}`. *Example:* `lectures/hs_recursive_models.md:296`, `:299`, `:304`, `:309`, `:1022`, `:1060`, `:1197`, `:1230`. *Count:* 33 occurrences (file has zero `\mathbb{E}`).
- **[qe-math-002]** — Prime `'` and `^\prime` used systematically as transpose. *Example:* `lectures/hs_recursive_models.md:309`, `:1022`, `:1060`; also `^T` at L1486-1525. *Count:* ~20+ occurrences.

### Medium severity
- **[qe-math-011 (proposed)]** — `\mathcal N` / `\cal N` used as Normal distribution. *Count:* 3 occurrences.
- **[qe-writing-005]** — Heavy bolding for keyword definitions and labels.
- **[qe-ref-001]** — Multiple "Author, Coauthor, and Coauthor (Year)" narrative refs should use `{cite:t}`. *Example:* `lectures/hs_recursive_models.md:1937`, `:2197`, `:2198`. *Count:* 3+ occurrences.
- **[qe-link-002]** — Raw `python-intro.quantecon.org` URLs (L91 has 2 URLs).

### Low severity
- **[qe-writing-001]** — Multiple long compound paragraphs (e.g. L57-68 bullets, L82-88).

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings in sentence case (qe-writing-006).
- `\begin{bmatrix}` largely used (qe-math-003).
- Sequences in curly brackets (qe-math-005).
- Heavy `{doc}` use for cross-series references (qe-link-002).

## Recommended actions
1. Replace all bare `E_t` / `E_0` / `E[\cdot]` with `\mathbb{E}` (qe-math-010, proposed).
2. Replace `^\prime` and `^T` (when used for transpose) with `^\top` (qe-math-002).
3. Replace `\mathcal N` / `\cal N` with `N` (qe-math-011, proposed).
4. Convert "Author, et al. (Year)" narrative refs to `{cite:t}` (qe-ref-001).
5. Convert raw `python-intro.quantecon.org` URLs to `{doc}\`intermediate:linear_models\`` style (qe-link-002).
