# Style Audit — smoothing

- **Series:** lecture-dp
- **File:** `lectures/smoothing.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 5.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H2/H3 mostly sentence case. |
| Math         | 3/10  | Apostrophe transpose throughout LQ section; `\cal N` distribution; bare `E_t`. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize used 2×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 6/10  | Title-Case `'Periods'` xlabel (4×); 2 figsize calls. |
| References   | 4/10  | Four narrative-author `{cite}` patterns (e.g. "Lucas and Stokey {cite}…") — should be `{cite:t}`. |
| Links        | 4/10  | Six raw markdown links to `python-intro.quantecon.org` / `python.quantecon.org`. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Apostrophe `'` used as transpose throughout the LQ derivation. *Lines:* 151, 177, 190, 196, and dozens through the LQ section. *Count:* 50+ occurrences.
- **[qe-link-002]** — Six raw markdown links to `python-intro.quantecon.org` / `python.quantecon.org` cross-series URLs; should be `{doc}` intersphinx references.

### Medium severity
- **[qe-math-A3]** — Multivariate normal written as `{\cal N}(0,I)` (line 140); style is plain `N(0, I)`.
- **[qe-math-A1]** — Bare `E_t b_{t+1}` (lines 190, 196) and `\mathbb E_t` without braces (lines 177, 184); style is `\mathbb{E}_t`.
- **[qe-ref-001]** — Narrative-author citations using parenthetical `{cite}`. *Count:* 4 occurrences (e.g. "Lucas and Stokey {cite}`LucasStokey1983`", "Barro {cite}`Barro1979`", "Hall {cite}`Hall1978`").
- **[qe-fig-006]** — Title-Case `xlabel('Periods')` 4 times. *Lines:* 333, 342, 924, 933.

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs.
- **[qe-fig-001]** — `figsize=` set 2 times.

## Strengths
- Lecture title in correct Title Case.
- Most H2/H3 headings sentence case ("Background", "Linear state space version of complete markets model", "Interpretation of graph", "Incomplete markets version", "Finite state Markov income process").
- Matrices use `bmatrix`.
- "IID" used correctly.
- `\mathbb{P}` and `\mathbb{E}` partially used.
- Equation labels and `{eq}` references used cleanly.
- pip install at top; Unicode Greek in code.
- No matplotlib titles, no spine issues.

## Recommended actions
1. Replace every `'` used as transpose with `^\top` (highest priority).
2. Change `{\cal N}` to plain `N`.
3. Standardise `\mathbb E_t` → `\mathbb{E}_t` and bare `E_t` → `\mathbb{E}_t`.
4. Switch narrative `Author {cite}…` to `{cite:t}` form.
5. Convert 6 raw markdown URLs to `{doc}` form.
6. Lowercase `'Periods'` axis labels.
