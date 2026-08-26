# markov_chains_II

- **Series:** lecture-python-intro
- **File:** `lectures/markov_chains_II.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-003` ×3; `qe-writing-002` ×2; `qe-writing-008` ×5. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×7. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×5; `qe-fig-008` ×5; `qe-fig-002` ×3. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 258, 261, 321, 441, 468, 576, 629. *Example:* spaces around the keyword-argument `=` in `label = fr'...'` (261-262, 321-322); a single space before an inline comment plus trailing whitespace (258); missing space after commas in `('1','2',...)` (441, 468), where `codes_B` is also assigned and never used; an invalid escape sequence in the non-raw f-string `f'$x_0 = \, {x0} $'` (576), which pycodestyle flags as W605 and which the neighbouring cells correctly write as `fr'...'`; and `result = lambda P: ...` bound to a name inside the loop it is used in, shadowing both `result` and the loop variable `P` (629).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 251, 311, 371, 484, 558. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 267, 331, 391, 494, 576. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 96, 114, 224, 344, 420. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 79, 116, 296. *Example:* static image .png.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 158, 404. *Example:* `` {cite} `` in narrative flow: 'of `` {cite} ``'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 351, 406. *Example:* the eight-state Benhabib matrix is printed three times within thirty lines - as a `bmatrix` (406-418), as a Python literal inside the exercise (429-438), and as the same literal again in the solution (458-465); and the six-state political-institutions matrix is printed twice more here (351-361, 372-377) on top of the three copies it already has in markov_chains_I. Referring back to the labelled matrix in the earlier lecture would carry the same information.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 189, 202, 208. *Example:* three cross-references do not connect to what they claim. Line 208 reads `{ref}`discussed before <mc_eg1-1>`` but no label `mc_eg1-1` exists in either Markov lecture - markov_chains_I defines `mc_eg1` and this file defines `mc_eg1-2`, so the reference is broken. Line 189 says "The result in [theorem 4.3](llnfmc0)", which hard-codes a theorem number and then links to the *equation* label `llnfmc0` rather than the theorem's own label `stationary` (169). Line 202 links `[not IID](iid_violation)` to a target defined in lln_clt.md (line 406), which a bare markdown link cannot resolve across documents.

### Low severity
_None found._


## Strengths

- Definitions are bolded once, at the point of definition, and never re-bolded: accessible and reachable (61), communicate (63), irreducible (71), ergodicity (189).
- The ergodicity result is presented as a `prf:theorem` with a labelled equation, and then the lecture immediately gives the two interpretations that make it useful - fraction of time for one worker versus fraction of a population (218-222).
- The periodic-chain example (278-342) is exactly the right counterexample in the right place: it shows ergodicity holding while asymptotic stationarity fails, and 338-342 states that distinction in one sentence.
- The indicator is written `\mathbb{1}\{X_t = x\}` with braces around the event throughout (177, 238, 533), matching the proposed qe-math-014 (proposed) convention, and `\mathbb{1}` is explained at 187.
- The inline comment "# Careful: P and p are distinct" at 563 pre-empts exactly the confusion the reader is about to have between the transition matrix and the unemployment probability.

## Recommended actions

1. Fix the broken reference at 208 - `mc_eg1-1` does not exist; the cross-sectional discussion it points at is `cross-sectional-distributions` in markov_chains_I (line 648).
2. Replace "[theorem 4.3](llnfmc0)" at 189 with `` {prf:ref}`stationary` `` so the theorem number is generated rather than hard-coded, and convert the cross-document link at 202 to a `{ref}` role.
3. Replace the three static transition-graph PNGs (79, 116, 296) with networkx code of the kind markov_chains_I uses at 261-288, and add `mystnb: figure: caption/name` metadata to the five un-named figures (251, 311, 371, 484, 558).
4. Make the state labelling consistent: the figures at 391 and 494 label the series `$x = 1$ ... $x = 8$` while indexing `ψ_star[x0]` and `(X == x0)` from zero, and the figure at 267 labels from zero - and for the political chain the states have names (DG, DC, ...) rather than numbers.
5. Cite the eight-state matrix once and refer back to it rather than printing it three times (406, 429, 458); the same applies to the six-state matrix already given in markov_chains_I.
6. Convert the three narrative-position citations to `{cite:t}` (158, 404, 597) and the code cell inside the non-gated `{exercise}` at 429 to gated `exercise-start`/`exercise-end` syntax.
7. Set `lw=2` on the five line plots (267, 331, 391, 494, 576), fix the PEP8 items above, and drop the unused `codes_B` assignments.
