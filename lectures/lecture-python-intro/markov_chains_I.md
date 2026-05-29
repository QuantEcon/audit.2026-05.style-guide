# Style Audit — markov_chains_I

- **Series:** lecture-python-intro
- **File:** `lectures/markov_chains_I.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 OK; mostly sentence-case H2/H3/H4; a couple of H3 use Title Case for proper nouns ("Markov chains", "QuantEcon's"). |
| Math         | 8/10  | `\mathbb P` (M7 OK); `\mathbf 1` used for ones vector (M3 violation); sequences `\{X_t\}` correct. |
| Code         | 8/10  | `!pip install quantecon` at top with `hide-output` (qe-code-003 OK); unicode Greek in code (qe-code-002 OK). |
| JAX          | out of scope | — |
| Figures      | 8/10  | No `figsize=` / `ax.set_title` violations; 3D simplex plots use `mpl_toolkits` standard usage. |
| References   | 7/10  | 7 `{cite}` usages; 2 are in-text ("proved in Chapter 4 of {cite}", "can be found in Chapter 4 of {cite}") — should be `{cite:t}`. |
| Links        | 8/10  | `{doc}` used once; one direct URL on line 473 `python-programming.quantecon.org/numba.html`. |
| Admonitions  | 9/10  | `{prf:theorem}` × 3 used (qe-admon-004 OK); solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **M3** — Uses `\mathbf 1` (lines 1245, 1246, 1248) for ones vector; should be `\mathbb{1}` per M3. *Count:* 4 occurrences in one solution block.
- **[qe-ref-001]** — In-text citations should use `{cite:t}`. *Examples:* `lectures/markov_chains_I.md:699` ("proved in Chapter 4 of {cite}\`sargent2023economic\`"), 797 ("can be found in Chapter 4 of {cite}\`sargent2023economic\`"). *Count:* 2 occurrences.
- **[qe-link-002]** — Cross-series link uses direct URL. *Example:* `lectures/markov_chains_I.md:473` (`[JIT compiled](https://python-programming.quantecon.org/numba.html#numba-link)`). Should be `{doc}\`programming:numba\``.

### Low severity
- **W3** — "### Defining Markov chains" (line 297) and "### Using QuantEcon's routines" (461) — "Markov" and "QuantEcon" are proper nouns; acceptable.
- **W1** — Some short two-sentence paragraphs.

## Strengths
- `\mathbb P` consistently used for probability (M7 OK).
- Sequences use `\{X_t\}` (M6 OK).
- Bold for definitions (**probability mass function**, **stochastic matrix**, **Markov matrix**, **states**).
- IID written correctly in cross-reference (line 202).
- `{prf:theorem}` directives (qe-admon-004 OK).
- `quantecon` install at top with `hide-output` (qe-code-003 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Replace `\mathbf 1` with `\mathbb{1}` per M3 (and add explanation).
2. Convert in-text `{cite}` usages on lines 699, 797 to `{cite:t}`.
3. Replace direct URL on line 473 with `{doc}\`programming:numba\``.
