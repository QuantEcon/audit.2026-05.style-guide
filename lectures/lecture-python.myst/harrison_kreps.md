# harrison_kreps

- **Series:** lecture-python.myst
- **File:** `lectures/harrison_kreps.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-002` ×4; `qe-writing-008` ×30; `qe-writing-001` ×1, +1 more. |
| Math         | 8/10  | `qe-math-010` (proposed) ×1; `qe-math-009` ×2. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 106. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 30. *Lines:* 78, 97, 119, 129, 131, 174, 177, 202, 214, 216, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 408, 421, 585. *Example:* the two solver signatures under-indent their continuation line to 28 spaces against a visual indent of 30 (408, 476; E128) and line 421 then over-indents the closing `axis=0)` of the same call (E127), while the equivalent call at 489 aligns it correctly - the same expression is laid out two ways in one file. Line 585 names a variable `dividendreturn` and 581-583 use `qopt` and `qpess`, none of which is the snake_case PEP8 asks for.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 253, 323. *Example:* line 323 writes `$max$` in prose, which renders as three italic letters rather than the operator - `\max` is used correctly inside the displays at 313 and 352, so the inline form is inconsistent with the lecture's own math. Matrix rows are separated by `\cr` at 253 and 266-267 but by `\\` at 114-115 and 124-125, two spellings of one thing in the same file.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 621. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 32, 155, 185, 460. *Example:* line 460 packs three errors into one sentence: 'Notice from the sixth row of that the pessimistic price $p_o$ is lower than the homogeneous belief prices' - the noun after 'of' is missing, the pessimistic price is $p_p$ not $p_o$, and it is the fourth row of the table, not the sixth. '### Ownership rights' opens at 155 by restating what 97-101 have just said about entitlement to the next dividend and the right to resell; '### Optimism and pessimism' restates at 185-188 what 129-131 and 147-151 have already established, stationary distributions included. Line 32 reads 'this lecture uses following libraries'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 219, 400. *Example:* the lecture has no figures at all, and its central object is six price functions over a two-state space - exactly the comparison a single grouped bar chart or a pair of step plots would make instantly legible. The summary table at 219-226 is explained row by row over the following 300 lines with the reader holding six numbers in their head, and the resale-option story at 396-402 ('the asset changes hands whenever the state changes') is a simulated state path with holdings marked, which the `quantecon` MarkovChain already imported at 57 could generate in a few lines.

### Low severity
_None found._


## Strengths

- The table-first structure works: all six price functions are tabulated at 219-226 with a legend naming each one, followed by 'We'll explain these values and how they are calculated one row at a time' (237) - and the lecture then does exactly that, so the reader always knows where in the argument they are.
- Every pricing rule is a labelled equation that later prose cites rather than restates: `eq:assetpricehomog` (259), `HarrKrep1` (264), `hakr2` (309) cited at 342, 443, 468 and 504, `HarrKrep3` (349), `HarrKrep4` (446) cited at 462.
- The two belief matrices are given exactly, as fractions in `bmatrix` (112-127), and their stationary distributions are computed with `qe.MarkovChain` (135-145) rather than asserted - which is what makes the 'more optimistic in state 0, more pessimistic on average' contrast checkable.
- The bubble definition is quoted before the model (74) and the lecture returns to it at the end through Scheinkman's reading (500-517), including the two policy levers - short-sale limits and leverage limits - that act in opposite directions.
- The exercise does more than recompute the table: it introduces permanently optimistic and permanently pessimistic investors (539-563) and uses them to explain why the heterogeneous-belief price coincides with the permanently-optimistic single-belief price (615-616).

## Recommended actions

1. Repair line 460: it names the wrong row, the wrong symbol ($p_o$ for $p_p$) and is missing the noun after 'of'.
2. Either call `price_pessimistic_beliefs` (474-495) or delete it - as the lecture stands, the function written to solve `` {eq}`HarrKrep4` `` is never used, and the $p_p$ row is instead obtained from `price_single_beliefs` with the permanently-pessimistic matrix at 583-593.
3. Add a figure: plot the six price functions of the summary table across the two states, and optionally a simulated state path with the marginal investor's type marked, so the resale-option argument at 368-402 has a picture.
4. Cut the restatements at 155 and at 185-188, which repeat 97-101 and 129-151 respectively.
5. Fix the math typography: `\max` instead of `$max$` at 323, one row separator inside `bmatrix` (`\\` at 114-125 versus `\cr` at 253-267), `s_t \in S = \{0,1\}` instead of `$S \in \{0, 1\}$` at 84, and braces on `\mathbb P` at 106 (qe-math-010 (proposed), proposed).
6. Tidy the code: fix the continuation indents at 408, 421 and 476; rename `dividendreturn`, `qopt` and `qpess`; replace the three Title Case docstrings ('Function to Solve Single Beliefs', 277, 410, 478) with a line saying what is returned; and fold the three near-identical max/min iterations at 419-429 and 487-489 into one helper.
7. Sweep the 30 double-space runs (78, 97, 119, 129, 131, 174, 177, 202, 214, 216, ...), split the two-sentence footnote paragraph at 621, and close the gap in 'investors(i.e.,' at 544.
