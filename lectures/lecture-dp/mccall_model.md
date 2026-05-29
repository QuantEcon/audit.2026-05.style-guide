# mccall_model

- **Series:** lecture-dp
- **File:** `lectures/mccall_model.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 6.9 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | Systemic Title Case on nearly every H2/H3 heading. |
| Math         | 7/10  | `\mathbf{1}` used as indicator; otherwise OK. |
| Code         | 7/10  | Unicode Greek; pip install at top; PEP8; no figsize. |
| JAX          | out of scope | uses JAX but JAX rules out of scope per spec. |
| Figures      | 6/10  | Two `ax.set_title("reservation wage")` calls; `fontsize=` overrides. |
| References   | 9/10  | Single `{cite}` for McCall1970, used parenthetically (no narrative-author misuse). |
| Links        | 6/10  | One raw `python-programming.quantecon.org/jax_intro.html` markdown link. |
| Admonitions  | 8/10  | Exercises labelled; solution dropdown used; clean structure. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Systemic Title Case on H2/H3 headings. *Examples:* `## The McCall Model` (78), `### A Trade-Off` (117), `### The Value Function` (133), `### The Optimal Policy` (200), `## Computing the Optimal Policy: Take 1` (257), `### The Algorithm` (287), `### Fixed Point Theory` (317), `### Implementation` (355), `### Comparative Statics` (485), `## Computing an Optimal Policy: Take 2` (612), `## Continuous Offer Distribution` (741), `### Implementation with Lognormal Wages` (780), `## Volatility` (879), `### Lifetime Value and Volatility` (941). *Count:* 14+ headings.
- **[qe-math-008]** — Indicator/ones vector written as `\mathbf{1}{...}` (bold-face), not `\mathbb{1}`. *Lines:* 226, 233, 238. *Count:* 3.

### Medium severity
- **[qe-math-010 (proposed)]** — Expectation uses `{\mathbb E}` (line 104) — borderline; preferred `\mathbb{E}`.
- **[qe-fig-003]** — Two embedded `ax.set_title("reservation wage")`. *Lines:* 602, 868.
- **[qe-link-002]** — Raw markdown link to `python-programming.quantecon.org/jax_intro.html` (line 382); should be `{doc}` form.
- **[qe-writing-001]** — Several multi-sentence paragraphs.

### Low severity
- **[qe-writing-004]** — Capitalised "Banach contraction mapping theorem" OK as proper noun, but "Bellman operator" sometimes capitalized inconsistently.

## Strengths
- Lecture title correctly Title Case.
- Equations use `{math} :label:` + `{eq}` refs cleanly.
- Greek letters via Unicode in code (`β`, `σ`, `μ`), LaTeX inside math environments.
- "IID" used correctly throughout.
- No transpose violations.
- pip install at top.
- No figsize, no spine issues, mostly lowercase axis labels.
- Exercises use labels + dropdown solutions.

## Recommended actions
1. Convert all H2/H3 headings to sentence case.
2. Replace `\mathbf{1}\{ … \}` indicator with `\mathbb{1}\{ … \}` (and introduce the notation at first use).
3. Remove the two `ax.set_title("reservation wage")` calls.
4. Convert the `python-programming.quantecon.org/jax_intro` markdown link to `{doc}` form.
5. Tighten multi-sentence paragraphs.
