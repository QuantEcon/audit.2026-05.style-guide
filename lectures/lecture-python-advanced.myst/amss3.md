# amss3

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/amss3.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-005` ×10; `qe-writing-002` ×5; `qe-writing-003` ×3, +2 more. |
| Math         | 8.5/10 | `qe-math-013` (proposed) ×1; `qe-math-009` ×1. |
| Code         | 7.5/10 | `qe-code-001` ×7. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×5; `qe-fig-003` ×3; `qe-fig-008` ×3, +2 more. |
| References   | 7.5/10 | `qe-ref-001` ×5. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 187, 202, 243, 246, 587, 688, 694. *Example:* line 188's continuation is indented 39 spaces against an opening paren at column 38, so the argument list is one column out of alignment (E128); 202 and 243 bind the loop variable `id`, shadowing the builtin; 246, 250 and 252 write `axes[i+2]` without spaces around the operator while the rest of the file spaces its operators; 587-589 and 688-690 use backslash line continuations *inside* parentheses where the parentheses already continue the expression, and add a double space before each backslash and after each `+`; 694 writes `B_star/div` unspaced two lines after `u.β * (...)` spaced normally.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 177, 212, 226, 238, 259. *Example:* {figure} without :name:.
- **[qe-ref-001]** — Use correct citation style. *Count:* 5. *Lines:* 40, 60, 231, 301, 398. *Example:* {cite} in narrative flow: 'of {cite}`'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 49, 229, 234, 263, 528. *Example:* 229-232 is a single 75-word semicolon chain describing three vertical lines on one histogram; 263-265 is a 46-word sentence ("conceal the weak but inexorable force that the Ramsey planner puts into both series driving them toward ergodic marginal distributions that are far from these early observations") and ends with no full stop; 49-50 spends 45 words and says "the ergodic distribution of the par value of government debt" twice; 234-236 is a 40-word sentence whose subject arrives after three subordinate clauses; and 528-530 is a broken paragraph - it opens lowercase on "so while" and line 529 begins with a stray `:` that MyST will read as a definition-list term.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 10. *Lines:* 54, 60, 97, 232, 379, 389, 394, 423, 454, 519. *Example:* bold is used for plain emphasis throughout, where the rule assigns italic: **as close as possible** (54), **three** (97), **before** (232), **in advance** (379), **first** / **then** (389-390), **without** (394), **minus** / **plus** (423), **surplus** (454), **constant** (519). Line 60 additionally puts a bold "**Warning:**" label inside a `{note}` directive that should simply be a `{warning}`. The genuine definitions are bolded correctly (299 effective deficit/debt, 311 fiscal risks, 443 effective return), so the two uses are not being kept apart.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 69. *Lines:* 29, 34, 35, 37, 39, 42, 44, 46, 50, 52, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 200, 241. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 212, 226, 259. *Example:* static image .png.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 204, 249, 250. *Example:* .set(title=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 203, 244, 246. *Example:* plot() without lw=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 224, 656, 676. *Example:* line 221 says "Let's discard the first 2000 observations ... and construct the histogram" and 224 says "We obtain the following graph for the histogram", but no code in the lecture builds that histogram - 226 is a static PNG, so the central object of the section (and the three vertical lines described at 229-232) cannot be reproduced by the reader; 656-660 tells the reader that "0.2 is the initial value for $\tau$ in the root-finding algorithm" while the cell above at 652 passes `.1` and the cell below at 667 passes `.5`; and the Execution walkthrough runs Step 1 (538), Step 2 (560), Step 3 (636), Step 4 (662) and then jumps to Step 6 (676) - Step 5, the variance-minimisation step that defines ${\mathcal B}^*$, has no execution section at all, and the two `###` interludes at 566 and 577 sit a level *above* the `####` steps they interrupt.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 407, 422. *Example:* the seven-step construction at 409-513 is a composition pipeline - $c_\tau(s)$ into ${\mathcal R}_\tau, {\mathcal X}_\tau$ into $\tau({\mathcal B})$ into $J({\mathcal B})$ into ${\rm var}(J)$ into ${\mathcal B}^*$ into the rate and $\hat b$ - and the reader has to hold the whole chain in their head from prose alone; the same section's "chicken and egg" circularity (374-384) is a two-node diagram. Separately, the two typo alerts at 422 and 456 are exactly the "important note" case the rule points at admonitions for, and are typeset as bold labels in running text instead.

### Low severity
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 506. *Example:* line 506 defines `div = {\beta E u_{c,t+1}}` - a three-letter roman-less identifier that renders as the product $d\,i\,v$ - and 512 then divides by it; the same quantity already has a name in the lecture ($\beta E u_{c,t+1}$, used inline at 349), so the abbreviation buys nothing. The calligraphic ${\mathcal B}, {\mathcal R}, {\mathcal X}$ elsewhere is *not* counted: 286-297 introduces them explicitly as BEGS's objects against the lecture's own $b, B, R, X$, so the decoration is carrying a real distinction.
- **[qe-math-013 (proposed)]** — Reference equations via {eq}`label`. *Count:* 1. *Lines:* 422. *Example:* manual reference 'equation (42)'.


## Strengths

- The calligraphic notation earns its keep: 286-297 states which objects are BEGS's (${\mathcal B}_t, {\mathcal R}_t, {\mathcal X}_t$) and gives the full change of variables to the lecture's own $b_t, B_t, R_t$ in one display, so a reader can move between the paper and the code without guessing.
- The lecture corrects its source in public: the sign error in BEGS equation (42) is flagged at 422-425 and the one in equation (46) at 456-459, each with a note that the displayed equation above has already been fixed - and the up-front `{note}` at 59 warns that this is coming.
- The seven algebraic steps at 409-513 are mirrored by execution cells in the same order (538-714), so each formula can be checked against the function that implements it.
- The IID structure is used deliberately rather than silently: 566-575 explains that π has identical rows and that setting $s=0$ picks off the one row that matters, which is why the later cells all pass `s = 0`.
- The convergence story is argued from the simulation rather than asserted - 216-218 reads the roughly 1000-period transient off the long simulation and ties it to the BEGS rate-of-convergence approximation derived at 356-366.

## Recommended actions

1. Replace the three static PNGs (212, 226, 259) with code-generated figures (qe-fig-002). Two of them duplicate plots the adjacent cells already draw, and the histogram at 226 - whose three vertical lines get 75 words of description at 229-232 - is never computed anywhere in the lecture.
2. Give the five figures `:name:` labels and captions (qe-fig-005 ×5), move the embedded `set(title=)` calls at 204, 249 and 250 into those captions (qe-fig-003 ×3), set `lw=2` at 203, 244 and 246 (qe-fig-008 ×3), and drop the `figsize` overrides at 200 and 241.
3. Strip the 69 runs of double spaces (qe-writing-008), and repair the broken paragraph at 528-530 - the stray leading `:` on 529 makes MyST parse the passage as a definition list, and the sentence begins lowercase.
4. Convert the bold emphasis at 54, 97, 232, 379, 389-390, 394, 423, 454 and 519 to italic, turn the two typo alerts at 422 and 456 into `{warning}` admonitions, and make the `{note}` at 59 a `{warning}` rather than a note carrying a bold "**Warning:**" label.
5. Write the expectation and variance operators the way the guide asks: $\mathbb{E}$ instead of bare `E` and `E_t` (291, 349, 450, 506, 516), and $\mathbb{V}$ / `\operatorname{cov}` instead of `{\rm var}` and `{\rm cov}` (324, 337, 361, 481, 487, 494); replace the `div` identifier at 506 with the expression it abbreviates.
6. Fill the gap in the Execution walkthrough: add the missing Step 5 section, demote the `###` interludes at 566 and 577 so they do not outrank the `####` steps, and fix 659 so it names the initial $\tau$ the code actually passes (`.1` at 652, `.5` at 667).
7. Cite or delete the two dead equation labels `key_formula_1` (347) and `rate_of_convergence_1` (359); unwrap the blockquote around the latter, which quotes a `{math}` directive and leaves two empty `>` lines behind; recast the citations in author position (40, 60, 231, 301, 398) as `{cite:t}`; and clean the PEP8 items listed above.
