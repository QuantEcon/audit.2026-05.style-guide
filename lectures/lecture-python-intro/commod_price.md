# commod_price

- **Series:** lecture-python-intro
- **File:** `lectures/commod_price.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-003` ×2; `qe-writing-005` ×1; `qe-writing-007` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 9/10  | `qe-code-001` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×3; `qe-fig-008` ×2. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 66, 352, 410. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 71, 429. *Example:* plot() without lw=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 240, 362. *Example:* two breaks. (a) The central functional equation appears at lines 240-246 with no introducing sentence: line 236 says only 'we seek a p such that ... hold', then the display defines p* and line 248 picks up with 'where'. The reader is handed the defining equation without being told it is the candidate. (b) Line 190 defines P as the inverse demand function D^{-1}, but line 362 sets `D = P = lambda x: 1.0 / x`, silently relying on 1/x being its own inverse; nothing in the text says so, so the code appears to contradict the definition.

### Low severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 1. *Lines:* 424. *Example:* the loop body at lines 424-425 is indented 12 spaces inside a `for` at indent 4, where 8 is required; the block is over-indented by one level relative to its header.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 91. *Example:* line 91 names the lecture's model in italic - 'a dynamic model of supply and demand, called the *competitive storage model*' - which is the rule's own counter-example: a definition should be bold, and italic reserved for emphasis. It is the only emphasis mark in the file.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 298. *Example:* lines 298-339 describe successive approximation as a sequence of functions p_1, p_2, ... converging to p*, but the code at 385-400 plots only the first iterate (the inverse demand curve) and the last. Overlaying two or three intermediate iterates would show the convergence the section spends forty lines describing.


## Strengths

- The lecture flags its own difficulty and says precisely what makes it hard - the unknown is a function rather than a number or vector (lines 26-35) - so the reader knows what they are in for before the first equation.
- The solution technique is taught, not just used: line 222 explains what an ansatz is and why one is being made, and line 287 closes the loop with 'We have found an equilibrium, which verifies the ansatz'.
- The verification at lines 255-287 actually checks the candidate against both equilibrium conditions in turn, deriving eq:arbi from the max at eq:dopf and then handling eq:pmco separately, rather than asserting that the ansatz works.
- Sentence discipline is exceptional - not one sentence in the file reaches 28 words - which is what makes a functional-equation argument legible at introductory level.
- The `{note}` at lines 113-120 pre-empts a reader's objection to the word 'harvest' for standardized goods like computer chips, and says plainly that the term is kept for simplicity.

## Recommended actions

1. Add a sentence before the display at line 240 introducing p* as the candidate price function that the ansatz produces - the lecture's defining equation currently arrives with no lead-in.
2. Explain or split the `D = P = lambda x: 1.0 / x` at line 362: line 190 defines P as D inverse, and the code works only because 1/x is self-inverse, which the lecture never says.
3. Change the italic at line 91 to bold, since it names the model rather than emphasizing it.
4. Plot two or three intermediate iterates in the successive-approximation cell at lines 385-400, so the convergence described at lines 298-339 is visible; then add mystnb figure metadata to the three figure cells at lines 66, 352 and 410 (qe-fig-005) and set `lw=2` on the plots at lines 71 and 429 (qe-fig-008).
5. Use the `beta_a, beta_b` values defined at line 354 in the call at line 360 instead of the hard-coded `beta(5, 5)`, and fix the over-indented loop body at lines 424-425.
6. Remove or reference the two dead equation labels - eq:mkeq (line 207) and eq:dopf2 (line 320) are defined but never cited, while every other label in the file is.
