# cons_news

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/cons_news.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 6.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-005` ×21; `qe-writing-004` ×8; `qe-writing-002` ×7, +4 more. |
| Math         | 4.5/10 | `qe-math-003` ×17; `qe-math-010` (proposed) ×4. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×4; `qe-fig-008` ×11. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 7.5/10 | `qe-link-002` ×7. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 11. *Lines:* 748, 749, 768, 769, 770, 798, 799, 800, 807, 808, …. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 7. *Lines:* 36, 56, 86, 412, 486, 498, 501. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 17. *Lines:* 549, 553, 557, 561, 565, 566, 576, 580, 584, 588, …. *Example:* array used as matrix.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 234, 380, 383, 405. *Example:* bare expectation `E [`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 7. *Lines:* 94, 101, 269, 441, 449, 753, 774. *Example:* line 441-447 is a single 71-word sentence covering the shock, the consumer's response, the saving decision, the future taxes and the government's bond issuance; 449 is 51 words, 753-757 is 59 words, 269-273 is 46, 101 is 42, 94 is 40 and 774-777 is 39 - the pattern is one sentence per causal chain instead of one sentence per link, and every one of these splits at a comma into two or three sentences.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 8. *Lines:* 485, 486, 680, 711. *Example:* mid-sentence 'Difference'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 21. *Lines:* 42, 62, 63, 80, 140, 275, 313, 316, 320, 351, …. *Example:* bold is the lecture's emphasis marker and italic is essentially unused - the whole file contains 2 italic spans against roughly 50 bold ones, and at least 21 of the bold spans emphasise an ordinary word rather than define a term: `**regardless**` (42), `**today's**`/`**future**` (62, 63, 80), `**same**` (140, 275, 497), `**increases**`/`**all**`/`**decreases all**` (313, 316, 320), `**increase**` (351), `**exactly**` (383), `**saving**`/`**permanent**` (443, 451, 452), `**decreases**` (760), `**permanently**` (777), `**single**` (816), `**evaluate**`/`**simulate**` (842), `**identical**`/`**different**` (847, 848); each of these should be italic, leaving bold for the genuine definitions the lecture does mark well (115, 116, 120, 158, 269, 279).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 52. *Lines:* 40, 45, 49, 58, 62, 65, 66, 67, 82, 87, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 618, 731, 770. *Example:* inline comments at 618 (`1e-12]]) # put penalty on debt`) and 731 (`J = 5 # Number of coefficients that we want`) are preceded by one space where PEP8 asks for two; line 770 writes `[0, J-1]` without spaces round the subtraction while the same cell spaces every other operator.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 747, 767, 801, 810. *Example:* plt.title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 746, 766, 796, 805. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 820, 869. *Example:* the last code cell in the lecture is at 805, but two sections after it promise computations that never run: 820-844 lays out a four-step procedure for building a single shared $\{y_t\}$ realization and using it to evaluate both decision rules, and 852-870 derives $a_{t+1}$ from the $\epsilon$ history and then says "We can verify that we recover the same $\{a_t\}$ sequence computed earlier" - no verification, and no simulation of the shared path, appears anywhere in the file.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 4. *Lines:* 127, 146, 149, 481. *Example:* i.i.d..

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 796. *Example:* the experiment the lecture exists to display - two consumers with identical income and different information - is drawn as two separate single-axis figures at 796-803 and 805-812, each with its own independent vertical scale and its own title, so the consumption paths the reader is asked to compare are never on the same axes; the same is true of the impulse responses at 746 and 766.


## Strengths

- Code uses Unicode Greek throughout (`β`, `σϵ`, `σa` at 610-611, 628, 658, 743, 763) so the variable names read the same as the equations they implement.
- The two income-process representations get equation labels (`eqn_1`, `eqn_2`) and are then cited by label at every single point of use - 136, 158, 161, 269, 275, 279, 641, 669, 683, 754, 776 - so the reader never has to guess which representation is in play.
- The paper-and-pencil decision rules at 643-650 and 671-678 are set directly against Python's `-F1` and `-F2` output at 637 and 665, and the text says so at 784-785; the analytics and the computation check each other.
- The innovations representation is derived from the more informative one via the Kalman filter (225-265) rather than asserted, and the derivation's key intermediate - $\sigma_a^2 = \beta^{-2}\sigma_\epsilon^2$ - is stated at 151-156 before it is used.
- The three distinct roles of $\beta$ are enumerated as a bullet list at 115-117 and the discount-factor role is picked up again at 497 where the LQ problem needs it.

## Recommended actions

1. Convert the 17 `\begin{array}` blocks used as matrices to `bmatrix` - 549, 553, 557, 561, 565, 566, 576, 580, 584, 588 and 7 more - and drop the hand-written `\left[ \right]` delimiters (qe-math-003, 17 occurrences; this is the largest single fix in the file).
2. Reconcile the simulation with the text: 787-789 says both consumers are "always present[ed] with the same $\{y_t\}$ path", but 797 and 806 call `LSS1.simulate` and `LSS2.simulate` independently, so each figure is driven by its own random draw - implement the four steps described at 820-844 (build one $\{y_t\}$, derive $\{a_t\}$ from it, feed both decision rules) or drop the claim.
3. Either add the code that section 814 and section 850 describe, or delete those two sections - as it stands the lecture ends with two sections of unexecuted plans and an unperformed verification.
4. Switch the 21 emphasis bolds listed above to italic, keeping bold for the definitions at 115, 116, 120, 158, 269 and 279.
5. Replace `plt.title(...)` at 747, 767, 801 and 810 with figure captions, add `mystnb: figure: caption/name` metadata to the four plotting cells at 746, 766, 796 and 805, and set `lw=2` on the 11 `plt.plot` calls at 748, 749, 768, 769, 770, 798, 799, 800, 807, 808, 809 (qe-fig-003 ×4, qe-fig-005 ×4, qe-fig-008 ×11).
6. Collapse the 52 double and triple spaces (40, 45, 49, 58, 62, 65, 66, 67, 82, 87 and 42 more) - at 52 occurrences in 879 lines this is a source-formatting habit, not a set of slips (qe-writing-008).
7. Sweep the remaining mechanical and typographic items: `i.i.d.` to `IID` at 127, 146, 149, 481 (qe-writing-009 (proposed), proposed), brace the bare expectations at 234, 380, 383, 405 as `\mathbb{E}` (qe-math-010 (proposed), proposed), turn the seven raw quantecon URLs at 36, 56, 86, 412, 486, 498, 501 into `{doc}` references (qe-link-002), and fix the typos `the the` (227), `reprentation` (361) and `thid` (486).
