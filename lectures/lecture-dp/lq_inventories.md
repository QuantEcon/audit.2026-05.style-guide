# lq_inventories

- **Series:** lecture-dp
- **File:** `lectures/lq_inventories.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×2; `qe-writing-001` ×4; `qe-writing-003` ×3, +2 more. |
| Math         | 3/10  | `qe-math-002` ×15; `qe-math-003` ×17; `qe-math-009` ×1. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-003` ×4; `qe-fig-008` ×10; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 226, 271, 292, 333, 640, 743. *Example:* line 292 writes the demand shock as `𝜈_path`, where the character is U+1D708 MATHEMATICAL ITALIC SMALL NU, not Greek nu U+03BD - it looks right in a browser but will not match a search for `ν`, is not what qe-code-002 means by a Greek identifier, and is a hazard for any tool that normalises identifiers. Lines 333-336 use a backslash continuation inside a string literal, so the label becomes 'production when  $I_t$             forced to be zero' with the next line's indentation baked into it (and a double space before `$I_t$`). Then: three spaces after the comma in `A22=[[1,   0],` (226, E241); a space after the unary minus in `N[1, 0] = - d2` (271) and `N[1, 1:] = - a0 / 2 * Sc` (273); the bare trailing-dot float `b = 3.` (640); and `A22 =[[1,  0,  0],` (743) with no space after `=` and continuation lines indented 10 against a visual indent of 6 (744-745).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 306, 307, 308, 312, 326, 327, 328, 332, 333, 335. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 15. *Lines:* 131, 137, 148, 149, 151, 153, 661, 720. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 17. *Lines:* 114, 150, 151, 154, 157, 158, 161, 164, 165, 168, …. *Example:* array used as matrix.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 417, 448. *Example:* H2 Title Case: 'Inventories Not Useful' (Not, Useful).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 310, 316, 330, 338. *Example:* .set_title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 489, 716, 722, 769. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 71, 177, 489. *Example:* the bullet at 71-72 defines the production cost function and then contradicts itself in the same breath: '$c(Q_t) = c_1 Q_t + c_2 Q_t^2$, be a cost of production function, where $c_1>0, c_2>0$, be an inventory cost function' - the trailing clause belongs to the next bullet, which defines the inventory cost function properly at 73-78. The '**Remark on notation:**' at 177-178 says only that the cross-product matrix is called $N$, which lines 137 and 140 have already established, and bolds the label for it. And the point that the no-inventory production path can start below the optimal one takes five paragraphs (489-508): a claim, a two-sentence gloss, '"typical" does not mean "always"', 'Thus, if we look closely, we notice that...', and then a forward pointer to Example 6.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 129, 358, 425. *Example:* three symbols carry two meanings each, and the lecture knows about only one of them. (i) $Q_t$ is production and $Q$ is the quadratic-form matrix; the lecture apologises for this at 129-132 ('we ask that you please forgive us') instead of renaming one of them. (ii) The demand shock is $v_t$ - Latin vee - at 79, 92, 366, 372 and 619, and $\nu_t$ - Greek nu - at 358, 445, 474, 520, 523, 713, 726 and 769; the two render as visibly different glyphs, and a reader meeting `\nu_t = \alpha + \rho \nu_`` {t-1}` at 358 has no way to know it is the $v_t$ defined at 79. (iii) $C$ is the noise-loading matrix in ` ``x_{t+1} = A x_t + B u_t + C \epsilon_{t+1}` (126) and then the production cost function at 425, 439, 458 and 468, while the same cost function is lowercase $c$ at 71 and 430 - so `C(Q_t)` at 425 collides with a matrix defined three hundred lines earlier.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 56, 62, 432, 507. *Example:* 2 spaces.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 304. *Example:* figsize=.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 144. *Example:* the derivation of $R$, $Q$ and $N$ from the profit function is a single display 30 lines long (144-173) whose last step nests three `\underset{\equiv R}{\underbrace{\left[\begin{array}...\end{array}\right]}}` groups, plus three more `array` blocks for the vectors, inside one `aligned` (150-171). Splitting it into three short displays - one per matrix, each with the term of the profit function it comes from - would say the same thing, would let each matrix be labelled and cited, and would remove most of the 17 `array` environments that qe-math-003 is reporting.


## Strengths

- The two comparison benchmarks are motivated as economics before they are computed: '## Inventories Not Useful' (417-446) and '## Inventories Useful but are Hardwired to be Zero Always' (448-475) each set out a distinct firm problem with its own objective and constraint, derive a closed-form decision rule, and say what the comparison is for ('in order to shed light on the role that inventories play', 477-479) - so the third and fourth lines in the bottom-right panel mean something.
- The model-to-LQ mapping is spelled out completely rather than asserted: the state and control vectors (100-108), the partitioned law of motion written out in blocks and then in the compact $x_{t+1} = A x_t + B u_t + C \epsilon_{t+1}$ form (112-127), and every one of $R$, $Q$, $N$ traced back to a term in the profit function (144-175). A reader can check the `SmoothingExample.__init__` matrix construction (248-275) against the algebra line by line.
- Six worked examples exercise one class along a single dimension each - AR(1) demand (353), deterministic demand (517), costless carrying with $d_1 = 0$ (535), fully costless inventories (554), a linear trend (614), a seasonal cycle (650) - and each is one call to `SmoothingExample` with one keyword changed, so the comparative statics are legible from the code alone.
- Example 4 (554-612) is the most valuable thing in the lecture: it deliberately breaks the stability conditions, predicts the absurd consequence in advance ($Q_t \equiv -c_1/2c_2$, negative production, inventories run down forever), explains why the Bellman equation does it, and then shows the figure that confirms it - a failure mode presented as a lesson rather than hidden.
- The 4-panel figure produced by `simulate` (304-340) is the same layout for all six examples, including a twin-axis panel that puts the demand shock and the change in inventories on a common time axis (312-324), so the reader learns to read one figure and then reads five more for free.

## Recommended actions

1. Fix the two closed-form decision rules, which disagree with the code that computes them by a factor of 2. Line 445 gives $Q_t^{ni} = (a_0 + \nu_t - c_1)/(c_2 + a_1)$ while line 301 computes `(a0 + 𝜈_path - c1) / (2 * (a1 + c2))`; line 474 gives $Q_t^{h} = (a_0 + \nu_t - c_1)/(c_2 + a_1 + d_2)$ while line 302 computes `/ (2 * (a1 + c2 + d2))`. The code is right: maximising $(a_0 + \nu_t - c_1)Q - (a_1 + c_2)Q^2$ gives the first-order condition $(a_0 + \nu_t - c_1) = 2(a_1 + c_2)Q$. As written, a reader who checks the algebra against the figure will conclude the figure is wrong.
2. Fix the escaped underscore at line 82: `$\pi\_t = p_t S_t - c(Q_t) - d(I_t, S_t)$` renders as a literal underscore rather than a subscript, so the one bullet that defines the objective's summand shows 'π_t' instead of $\pi_t$. It is the only `\_` in the file and looks like a leftover from an rst conversion.
3. Settle the three notation collisions: rename either production $Q_t$ or the matrix $Q$ and delete the apology at 129-132; pick $v_t$ or $\nu_t$ for the demand shock and use it in all 15 places, including the code identifier at 292 (which should be Greek `ν`, U+03BD, not U+1D708); and stop using $C$ for the production cost function at 425, 439, 458 and 468, where $c$ is already that function and $C$ is already the noise matrix.
4. Convert the 17 `array` environments to `bmatrix` (114, 150-171, 364-376, 626-634) and, while doing so, split the 30-line display at 144-173 into three - one per matrix (qe-math-003 x17, the largest mechanical item here). The transposes at 131, 137, 148, 149, 151, 153, 661 and 720 all want `^\top`, and note the reported count of 15 overstates the 11 that are actually there - see scanner_doubts.
5. Figures: name the 4-panel figure so the prose can cross-reference it - 'the lower right panel' (404) and 'The bottom right panel' (481) are 90 lines apart and both refer to the figure produced at 388 - then move the 4 `set_title` calls into captions (310, 316, 330, 338), drop the `figsize=(15, 10)` (304), and add `lw=2` to the 10 line plots (306-335). Also set the three colours in panel [1,1] explicitly: the text at 482-487 names blue, green and orange, which currently depends on matplotlib's default cycle order.
6. Sentence-case the two Title Case H2s - 'Inventories Not Useful' (417) and 'Inventories Useful but are Hardwired to be Zero Always' (448) - split the four two-sentence paragraphs (489, 716, 722, 769) and clear the 4 double spaces (56, 62, 432, 507).
7. Tidy the writing per the findings above (the self-contradicting bullet at 71-72, the redundant Remark at 177-178, the five-paragraph 'typical' passage at 489-508) and the PEP8 items. Note that this file is byte-identical to `lecture-python.myst/lectures/lq_inventories.md`, so every fix should be made once, upstream, and it clears both series.
