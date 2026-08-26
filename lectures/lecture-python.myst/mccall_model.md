# mccall_model

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_model.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×12; `qe-writing-002` ×4; `qe-writing-001` ×1, +3 more. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×1; `qe-math-001` ×1. |
| Code         | 7/10  | `qe-code-001` ×22. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×8; `qe-fig-003` ×2; `qe-fig-008` ×2. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 22. *Lines:* 368, 391, 456, 457, 458, 459, 462, 464, 470, 552, …. *Example:* trailing whitespace on seven code lines (391, 462, 464, 470, 557, 559, 571; 464 and 470 are whitespace-only); six annotated parameters written without spaces around `=` - `tol: float=1e-6` and `max_iter: int=500` at 456-457, 552-553 and 710-711 - where PEP8 asks for `tol: float = 1e-6` and where the same file writes `c: float = 25` correctly at 390; four closing brackets parked at column 4 under an 8-space hanging indent (458, 554, 712, 804); `jnp.linspace(w_min, w_max, n+1)` at 368 with no spaces around `+`; `β ** periods` spaced at 1009 where 915 correctly writes `σ**2`; a single-quoted one-line docstring at 459 where the other five docstrings use triple quotes (968, 1017, 1091, 1131, 1167); and two code lines at 84 characters (1130, 1155).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 373, 427, 495, 581, 858, 931, 1049, 1089. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 104. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 12. *Lines:* 78, 117, 133, 200, 257, 287, 317, 485, 612, 741, …. *Example:* H2 Title Case: 'The McCall Model' (Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 6. *Lines:* 52, 111, 174, 202, 351. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 602, 868. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 375, 1178. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 124, 382. *Example:* raw link to dp.quantecon.org.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 1. *Lines:* 425. *Example:* unicode `β` inside a math environment.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 33. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 150, 155, 152, 955. *Example:* line 150 ends with a dangling fragment left over from an edit - '$v^*(w)$ denotes the total sum of expected discounted earnings when an agent always behaves in an optimal way. points in time.' - in the sentence that defines the lecture's central object; line 155 contains two typos in one clause, 'If we don't know what opimal choices are, it feels imposible to calculate $v^*(w)$'; lines 152-160 then make the same point three times in a row (we cannot compute $v^*$ yet, it feels impossible to compute $v^*$, let us set that aside), where one paragraph would do; and the numbered list at 952-956 runs '1.' then '3.'.

### Low severity
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 739. *Example:* `compute_reservation_wage_two` is derived over forty lines of algebra (636-675), stated as an algorithm (679-699), implemented (708-736), and then never called - by the lecture or by the exercise. Line 739 says 'You can use this code to solve the exercise below', but the exercise at 1065 is about unemployment duration under a *continuous* distribution and its solution (1089-1182) uses `compute_reservation_wage_continuous` instead. So the whole point of '## Computing an Optimal Policy: Take 2' - that iterating on a scalar beats iterating on an $n$-vector - is never demonstrated, and the one sentence that promises a payoff points at the wrong place.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 409. *Example:* the lecture contains no admonition at all, and four substantive asides are carried in inline parentheses instead: the broadcasting clarification at 409-410 ('The first term inside the max is an array and the second is just a number -- here we mean that the max comparison against this number is done element-by-element'), the scope note at 91, the offer-in-hand clarification at 147, and the reading instruction for $Tv$ at 335-336. The one at 409 is the most important - it is the only place the array form of the Bellman operator is explained - and it is the easiest to skip in its current form.


## Strengths

- The lecture states its method before using it - 'dynamic programming can be thought of as a two-step procedure that first assigns values to states and then deduces optimal actions given those values' (126-129) - and then the next two subsections are exactly those two steps, in that order.
- The reduction to a scalar equation is shown one operation at a time (638-675): multiply by $q(w')$, sum over $\mathbb W$, multiply by $\beta$, add $c$, then recognise the left side as $h$. A reader can follow each step without reconstructing it.
- The comparative-statics figure at 496-534 plots the two reservation wages as vertical lines *on top of* the wage offer distribution, which is what makes the answer legible: the reader can see what fraction of offers each reservation wage rejects, exactly as 492-493 promises.
- The volatility section does not stop at the reservation wage: it goes on to show that expected lifetime value also rises with volatility (941-1059), so the reader is not left with the impression that a higher reservation wage is a cost to the worker.
- The successive-approximation algorithm is written out as five numbered steps (289-311) and only then justified by the Banach fixed point theorem (317-352), including the two implications that matter - a unique fixed point, and convergence from any starting vector.

## Recommended actions

1. Lower-case the twelve Title Case section headings (78, 117, 133, 200, 257, 287, 317, 485, 612, 741 and the rest) - only the H1 takes title case (qe-writing-006, 12 occurrences, very-high weight).
2. Either run `compute_reservation_wage_two` and compare its answer and timing against the vector method, or delete it - and fix the pointer at 739, which sends the reader to an exercise that uses a different function.
3. Repair the prose in 'The Value Function': delete the 'points in time.' fragment at 150, fix 'opimal' and 'imposible' at 155, and merge the three paragraphs at 152-160 into one.
4. Add `mystnb: figure: caption/name` metadata to the eight un-named figure cells (373, 427, 495, 581, 858, 931, 1049, 1089) and move the two `set_title` strings (602, 868) into captions (qe-fig-005 x8, qe-fig-003 x2).
5. Replace the unicode `β` inside the math at 425 with `\beta` (qe-math-001), change `\mathbf{1}` to `\mathbb{1}` at 226, 233 and 238 - the manual's own indicator notation, and it also settles the qe-math-008 flag - and convert the two raw cross-series links at 124 and 382 to `{doc}` references (qe-link-002, 2 occurrences).
6. Say what $T = 100$ costs at 963: with $\beta = 0.99$ the truncated tail carries about 37% of the discounted weight, so the plotted level is not the lifetime value of `` {eq}`obj_model` `` - either raise $T$ or state that only the comparison across $\sigma$ is intended.
7. Clear the mechanical items: split the two-sentence paragraph at 33 (qe-writing-001), close the six double spaces (52, 111, 174, 202, 351), set `lw=2` on the two thin plots (375, 1178), renumber the list at 952-956, and fix the 22 PEP8 items above.
