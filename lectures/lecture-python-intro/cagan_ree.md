# cagan_ree

- **Series:** lecture-python-intro
- **File:** `lectures/cagan_ree.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-002` ×9; `qe-writing-004` ×2; `qe-writing-005` ×4, +3 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×4; `qe-fig-008` ×5; `qe-fig-001` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 344, 690, 812, 875, 876. *Example:* plot() without lw=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 9. *Lines:* 39, 50, 420, 473, 570, 582, 586, 615, 618. *Example:* nine sentences of 30-44 words. Line 39 opens with a 39-word sentence that carries a parenthetical definition inside it; line 420 is a 41-word sentence defining the velocity dividend; line 473 runs 44 words across three source lines and also leaves its opening double quote unclosed; lines 570, 582, 586, 615 and 618 each join two findings with 'and how', 'but how', or 'that it reaps from'.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 245, 330, 518, 643. *Example:* line 245 indents the namedtuple continuation to column 24 where the visual-indent target is 22; lines 330, 518 and 643 space the same operator two ways - `μ0*np.ones(T1), μ_star*np.ones(T-T1+1)` at 330 against the identical `μ0 * np.ones(T1+1), μ_star * np.ones(T - T1)` at 681 and 857, `cm2.α*(μ0 - μ_star)` at 518, and `ϕ**t * μ0 + (1-ϕ**t)*μ_star` at 643 where one product is spaced and the other is not inside a single expression.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 342, 535, 593. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 676, 732, 792, 850. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 469. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 23, 455, 623. *Example:* two structural gaps. (a) The bullet list at lines 23-25 hangs directly off line 21 with no introducing clause, so the reader meets three claims about fiscal policy with nothing saying what the list enumerates. (b) The heading tree misplaces two of the three experiments: 'Experiment 1' is an H4 under '### Some quantitative experiments' (line 285), but '### The log price level' (372) and '### What jumps?' (398) close that section, and 'Experiment 2' (455) and 'Experiment 3' (623) are then H4s nested under 'What jumps?'. The three experiments are not siblings in the document tree even though the text treats them as such.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 465, 469. *Example:* mid-sentence 'Path'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 421, 461, 465, 469. *Example:* the lecture's two coined terms are defined in scare quotes rather than bold - 'the velocity dividend' at line 421 and 'MIT shock' at line 461, both of which the text then reuses. Conversely the only bold in the lecture, at lines 465 and 469 ('Initial Path:', 'Revised Continuation Path'), is doing the job of a heading rather than marking a definition or emphasis.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 292. *Example:* 2 spaces.


## Strengths

- Twelve display equations are labelled and re-cited by name (eq:caganmd, eq:ree, eq:cagan, eq:pieq, eq:fisctheory1, eq:eq101, eq:mcum, eq:fisctheory2, eq:piterm, eq:pformula2, eq:pfiscaltheory2, eq:eqnmoneyjump), and the exercise solutions at lines 765 and 886 cite them back to the derivation they check.
- The theory is anchored to named sources and named episodes - Sargent and Wallace's 'Unpleasant Monetarist Arithmetic' at lines 27-28, Cochrane at 32, Cagan at 48, Sargent's four big inflations at 50 - with three `` {doc} `` links to the inflation_history data lecture at 34, 612 and 618.
- Line 621 states the limit of its own evidence: the informal comparison between model paths and the four hyperinflations 'should be supplemented with a more formal structural statistical analysis', rather than letting eyeballed pattern-matching stand as proof.
- All four exercises verify something the lecture asserts rather than extending it decoratively - the anticipation effect against alpha, the matrix solution against the closed-form discounted sum (agreeing to machine precision, line 765), gradual against sudden stabilization, and the real-balance path implied by eq:caganmd.
- The namedtuple at lines 245-251 documents each of its five fields with an inline comment, so the model parameters are self-describing where they are defined rather than only in the prose above.

## Recommended actions

1. Promote 'Experiment 2' (line 455) and 'Experiment 3' (line 623) to the same heading level as 'Experiment 1' (line 302), or move 'The log price level' (372) and 'What jumps?' (398) so they no longer close the section the experiments belong to - as it stands two of the three experiments are nested inside a subsection about whether m or p jumps.
2. Break the nine 30-44 word sentences at lines 39, 50, 420, 473, 570, 582, 586, 615 and 618 into one idea each, and close the unterminated double quote that opens at line 473.
3. Give the bullet list at lines 23-25 an introducing clause, and bold the two terms the lecture coins and then reuses - 'velocity dividend' (line 421) and 'MIT shock' (line 461) - instead of leaving them in scare quotes.
4. Add mystnb figure metadata to the six figure cells at lines 340, 529, 676, 732, 792 and 850 (qe-fig-005), set `lw=2` on the plot calls at 344, 690, 812, 875 and 876 (qe-fig-008), and drop the `figsize=` overrides at 342, 535 and 593 (qe-fig-001).
5. Convert the bold pseudo-headings at lines 465 and 469 into real headings (or into ordinary sentences), which also removes the mid-sentence capitals flagged there by qe-writing-004, and split the two-sentence paragraph at line 469.
6. Delete the stray LaTeX comment `% \forall t` left inside the display equation at line 105 - MathJax silently swallows the rest of the line, so the source carries a fragment that does nothing.
7. Fix the four PEP8 spacing sites at lines 245, 330, 518 and 643, the typo 'goverment's' at line 23, the double space at line 292 (qe-writing-008), and the two-sentence bullet at line 74.
