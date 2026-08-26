# lln_clt

- **Series:** lecture-python-intro
- **File:** `lectures/lln_clt.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-003` ×2; `qe-writing-007` ×1. |
| Math         | 4.5/10 | `qe-math-010` (proposed) ×21; `qe-math-004` ×1. |
| Code         | 7.5/10 | `qe-code-001` ×7. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×3; `qe-fig-001` ×3. |
| References   | N/A   | no citations in this lecture. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 94, 267, 304, 305, 479, 530, 703. *Example:* a six-space indent inside a four-space-indented function body (267); spaces around `=` in the default arguments `ns = [...]` and `m = 10_000` (304-305) and in the keyword argument `color = 'black'` (703); `st.beta(2,2)` with no space after the comma (530); and single-space-before-hash inline comments where PEP8 asks for two (94, 479, 530).
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 21. *Lines:* 59, 71, 72, 113, 127, 154, 165, 178, 183, 190, …. *Example:* missing braces: `\mathbb E`.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 490, 541, 685. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 475, 526, 679. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 31. *Example:* raw link to python.quantecon.org.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 1. *Lines:* 580. *Example:* \mathbf.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 349, 457. *Example:* the "## Breaking the LLN" section (349-412) is asymmetric: its first subsection makes its case in prose only while its second gets a worked example, a note and a forward pointer to an exercise; and "### Simulation 1" (457) is the only numbered section in the lecture - there is no Simulation 2, so the numbering promises a sequence that never arrives.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 359. *Example:* "### Infinite first moment" says "We can demonstrate this using the Cauchy distribution" (359) and then demonstrates nothing - lines 361-369 assert in prose that $\bar X_n$ is Cauchy and therefore does not concentrate, with no simulation and no figure. This is the one place in a lecture that announces at line 26 that it "is based around simulations" where a claim is left unillustrated, and the non-settling sample-mean path is the single most memorable picture in the topic.


## Strengths

- Probability events are written with braces throughout - `\mathbb P\{X=1\}` (59, 72), `\mathbb P\{a \leq X_i \leq b\}` (154), `\mathbb P\{\bar X_n \to \mu\}` (183), `\mathbb P\{0 \leq U < p\}` (587) - so the proposed qe-math-014 (proposed) convention holds without exception.
- Density and CDF case discipline is exact: lowercase $f$ for the common density (147, 154, 165, 190) and uppercase $F$ for the distribution the draws come from (463, 469), matching proposed qe-math-015 (proposed).
- "IID" is written in the correct form every time it appears (178, 189, 363, 376, 435, 611, 674), including inside the theorem statement - no "i.i.d." anywhere.
- The LLN is introduced by simulation before it is stated (50-131), and the statement that follows is a real `prf:theorem` with a label that the prose then cites by `{eq}` (205).
- The illustration section spells out the simulation algorithm as a numbered recipe (222-241) and then implements it in two small composable functions, `draw_means` and `generate_histogram`, whose parameters are documented inline.

## Recommended actions

1. Add braces to the 21 blackboard operators - `\mathbb E` -> `\mathbb{E}`, `\mathbb P` -> `\mathbb{P}` - the single largest fix in this lecture (qe-math-010 (proposed)).
2. Simulate the Cauchy failure in "### Infinite first moment": plot a running sample mean of Cauchy draws against $n$, in the style of the violin plots at 302-343, so the section demonstrates rather than asserts.
3. Add `mystnb: figure: caption/name` metadata to the five un-named figures (260, 302, 475, 526, 679) - the CLT histogram at 475 is the lecture's headline figure and is referred to only as "[above](sim_one)".
4. Replace `\mathbf 1` with the plain indicator `1` or `\mathbb{1}` (580, 590) and, whichever is chosen, say in the prose that it denotes the indicator - the current text explains it once but the notation is bold-face, which qe-math-004 rules out.
5. Convert the code cell inside the non-gated `{exercise}` at 567 to gated `exercise-start`/`exercise-end` syntax, and the raw `python.quantecon.org` link at 31 to a `{doc}` reference.
6. Fix the PEP8 items above and drop the three `figsize=(10, 6)` arguments (490, 541, 685) unless the wide aspect ratio is deliberate.
7. Give "### Simulation 1" a descriptive name (or add the missing second simulation), fix `$X_n$` -> `$\bar X_n$` at 300, and close the space in "Gaussian(Normal)" at 452.
