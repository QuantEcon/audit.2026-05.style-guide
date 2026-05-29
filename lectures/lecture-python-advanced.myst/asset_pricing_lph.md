# Style Audit — asset_pricing_lph

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/asset_pricing_lph.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 5.9 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Sentence-case headings; some bolded labels and longer paragraphs. |
| Math         | 4/10  | Bare `E` for expectation throughout; `{\mathcal N}` for Normal; `\begin{array}` in piecewise. |
| Code         | 7/10  | Limited code; one `alpha` spelled out. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | N/A   | no figures |
| References   | 7/10  | 9 `{cite}` consistently; one narrative ref ("of {cite}`Ross_76`") would benefit from `{cite:t}`. |
| Links        | 5/10  | Four raw `python-advanced.quantecon.org` / `python.quantecon.org` URLs. |
| Admonitions  | 7/10  | 5 gated exercises and 5 solutions with `:class: dropdown` — well-structured. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-A1]** — Bare `E` used systematically for expectation (carry-forward from v1 M7). *Example:* `lectures/asset_pricing_lph.md:23`, `:67`, `:76`, `:111`, `:118`. *Count:* 10+ occurrences.
- **[qe-link-002]** — Raw URLs for same-series and cross-series references. *Example:* `lectures/asset_pricing_lph.md:57`, `:59`, `:93`, `:96`. *Count:* 4 occurrences.

### Medium severity
- **[qe-math-A3]** — `{\mathcal N}` used as Normal distribution (carry-forward from v1 M9). *Example:* `lectures/asset_pricing_lph.md:241`. *Count:* 1 occurrence.
- **[qe-math-003]** — `\begin{array}{ll}` used inside `\left\{ ... \right.` for a case definition; should use `\begin{cases}`. *Example:* `lectures/asset_pricing_lph.md:342`. *Count:* 1 occurrence.
- **[qe-writing-A1]** — "i.i.d." instead of "IID". *Example:* `lectures/asset_pricing_lph.md:747`. *Count:* 1 occurrence.
- **[qe-writing-005]** — Bolded labels (`**existence**`, `**uniqueness**`, `**complete markets**`) are borderline definitional but mix with emphasis use.

### Low severity
_None found._

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings in sentence case (qe-writing-006).
- Equation labels via `$$ ... $$ (label)` form (qe-math-007) and `{eq}` references.
- One-sentence paragraph rule mostly respected (qe-writing-001).
- Exercises gated with `exercise-start`/`exercise-end` (qe-admon-001).
- Solutions use `:class: dropdown` (qe-admon-002).

## Recommended actions
1. Replace bare `E` with `\mathbb{E}` everywhere (qe-math-A1).
2. Replace `{\mathcal N}` with `N` (qe-math-A3).
3. Convert raw URLs to `{doc}\`advanced:orth_proj\``, `{doc}\`intermediate:aiyagari\``, etc. (qe-link-002).
4. Replace `\begin{array}{ll}` case block with `\begin{cases}` (qe-math-003).
5. Use "IID" in the code comment instead of "i.i.d." (qe-writing-A1).
