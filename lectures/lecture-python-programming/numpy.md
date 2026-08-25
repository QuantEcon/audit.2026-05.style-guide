# numpy

- **Series:** lecture-python-programming
- **File:** `lectures/numpy.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×12; `qe-writing-001` ×3; `qe-writing-005` ×4, +4 more. |
| Math         | 8/10  | `qe-math-010` (proposed) ×1; `qe-math-015` (proposed) ×1. |
| Code         | 7/10  | `qe-code-001` ×7; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×2; `qe-fig-008` ×13; `qe-fig-001` ×4. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 491, 492, 613, 678, 748, 807, 961. *Example:* trailing whitespace after the array rows at 491-492 (W291); a redundant trailing semicolon closing each of the four broadcasting diagram cells, `ax.text(...);` at 613, 678, 748 and 807 (E703); and a space after the unary minus in `np.exp(- 0.5 * z**2)` at 961 (E225).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 13. *Lines:* 519, 522, 525, 528, 532, 535, 538, 541, 545, 548, …. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 1190. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 12. *Lines:* 69, 122, 161, 222, 314, 383, 432, 836, 891, 923, …. *Example:* H2 Title Case: 'NumPy Arrays' (Arrays).

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1442. *Example:* install cell at line 1442 of 1539 (not near the top).
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 570, 635, 705, 778. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 1111, 1397. *Example:* {figure} without :name:.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 27, 468, 1436. *Example:* 5 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 850, 1273. *Example:* 850 reads "We already saw examples of multability above"; and 1273-1274 ("The logic is not obvious, but if you take your time and read it slowly, you will understand") substitutes an exhortation for the explanation of the `cumsum`/`searchsorted` trick, which is the one line of the `DiscreteRV` solution that needs explaining.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 1087, 1440. *Example:* "Implicit Multithreading" (1087-1118) ends the lecture body with an htop screenshot loaded from `/_static/lecture_specific/parallelization/`, a directory belonging to a lecture that is not in this series, with no transition from "Sub-packages" above it and no closing paragraph before "## Exercises"; and 1440-1447 wraps a second `!pip install quantecon` cell - 1,400 lines after the one at 32-36 - with "Let's make sure this library is installed" and "Now we can import the quantecon package", but the cell that follows at 1449 performs no import, using the `qe` bound at line 60.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 818, 907, 1031, 1417. *Example:* the file bolds terms well in places (**flat**, 133; **broadcasting**, 475; **ufuncs**, 951) and then breaks the convention four ways: *deep copy* (907) and *conditional extraction* (1031) are definitions set in italic; *Step 1:*, *Step 2:* and *Step 3:* (818, 824, 829) use italic as structural labels; and **Part 1**, **Part 2**, **Part 1 Solution**, **Part 2 Solution** (1417, 1436, 1476, 1506) use bold as headings.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 27, 83, 103, 826. *Example:* 2 spaces.

### Low severity
- **[qe-math-015 (proposed)]** *(reviewer)* — Lowercase for densities/PMFs, uppercase for CDFs. *Count:* 1. *Lines:* 1390. *Example:* (proposed) inside `ECDF.plot` the vectorized CDF evaluator is bound to lowercase `f` (`f = np.vectorize(self.__call__)`), while the same solution correctly uses uppercase `F` for the CDF object 11 lines later (`F = ECDF(X)`, 1401) - lowercase is reserved for densities and mass functions, uppercase for CDFs.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 872. *Example:* "Mutability" (848-890) turns on the aliasing surprise `b = a; b[0] = 0.0` (872-876) and explains it in five sentences of prose (878-889) with no figure, in a lecture that invests four hand-drawn cube diagrams in broadcasting - and `names.md` already draws exactly this box-and-arrow picture for the same idea at its lines 524-565, so the figure exists and could be reused.


## Strengths

- The broadcasting section earns its length: three cube diagrams (501, 630, 699) show the expansion NumPy performs, and a fourth (773) shows the case that fails, placed immediately after the `ValueError` it raises (755-766).
- The three broadcasting rules at 816-832 are stated as an algorithm and then traced on concrete shapes, so a reader can apply them rather than merely recognise them.
- Mutability is taught in the order a reader hits it - the aliasing surprise first (866-876), then `np.copy` (897-918) - rather than as a rule to remember in advance.
- `DiscreteRV` (1246-1271) is followed by an honest critique of itself: 1276-1300 shows that mutating `q` leaves `Q` stale, then points at the descriptor-based version in QuantEcon.py rather than pretending the solution is finished.
- Every dtype claim is checked in the notebook instead of asserted - `type(a[0])` at 111 and 118 demonstrates both the `float64` default and the `dtype=int` override.

## Recommended actions

1. Sentence-case the 12 headings (69, 122, 161, 222, 314, 383, 432, 836, 891, 923 ...) - Writing at 3.5 is the lowest score in the series and this is nearly all of it.
2. Move the duplicate `!pip install quantecon` at 1442-1445 up to the one at 32-36 and delete the stranded sentence at 1447 (qe-code-003).
3. Give the four near-identical `draw_cube` call blocks (574-613, 639-678, 709-748, 782-807) one parameterised helper - 200 lines of hidden-input code repeated four times, in the lecture that teaches loop elimination.
4. Add `:name:` and a caption to the two figures (1111, 1397) and remove the unused `Axes3D` and `cm` imports at 62-63 (there are no 3D plots in this lecture).
5. Add a reference diagram to "Mutability" (848-890), reusing the one `names.md` already has, and give "Implicit Multithreading" (1087) either a transition into it or a home in the lecture it was taken from.
6. Clean the code cells: trailing whitespace at 491-492, the four trailing semicolons at 613, 678, 748, 807, and the unary-minus spacing at 961.
7. Bold the definitions at 907 and 1031, make 818/824/829 and 1417/1436/1476/1506 real headings, add braces to `\mathbb P` at 1190, rename the lowercase `f` at 1390, and fix "multability" at 850.
