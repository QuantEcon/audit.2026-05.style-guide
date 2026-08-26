# cass_koopmans_1

- **Series:** lecture-python.myst
- **File:** `lectures/cass_koopmans_1.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×11; `qe-writing-005` ×4; `qe-writing-003` ×3, +3 more. |
| Math         | 9.5/10 | `qe-math-009` ×2. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×3; `qe-fig-005` ×1; `qe-fig-004` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 569, 657, 829, 895, 1087. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 8. *Lines:* 577, 672, 852, 901, 1093, 1097, 1101, 1102. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 11. *Lines:* 82, 102, 154, 216, 250, 477, 691, 785, 913, 967, …. *Example:* H2 Title Case: 'The Model' (Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 79. *Lines:* 30, 33, 37, 39, 54, 61, 84, 86, 95, 116, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 423, 456, 624, 853. *Example:* line 423 writes `if γ!= 1` with no space before the operator (`γ != 1` elsewhere in the corpus); line 456 opens a docstring with four quotes, `''''`, so the docstring's first character is a stray apostrophe; three lines run well past 79 characters (100 at 853, 89 at 873, 95 at 897, the first because a conditional expression, an f-string and a keyword argument share one line); and eight lines carry trailing whitespace (624, 830, 835, 838, 842, 852, 861, 864).
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 578, 673, 903. *Example:* .set(xlabel='t', ylabel=ylabels[i], title=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 31. *Example:* raw link to python-programming.quantecon.org.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 128, 227. *Example:* the same object gets two names a hundred lines apart: line 128 writes "Form a Lagrangian $L = \int_0^1 u(c(\omega)) d\omega + \lambda[\ldots]$" with a plain $L$, and line 227 writes the planner's Lagrangian as $\mathcal{L}(\vec C, \vec K, \vec \mu)$ (again at 237, 305). The plain letter already served, nothing collides with it, and the calligraphic form buys nothing.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 37, 151, 1073. *Example:* line 37 uses the phrase "in this lecture" twice in one sentence for two *different* lectures ("a planning problem in this lecture, and a competitive equilibrium in this lecture `` {doc}`cass_koopmans_2` ``"), and line 151 repeats the construction; line 1073 is a 40-word sentence that restates the sub-bullet two lines above it - 1071 already said the arrows show where the dynamics push successive $(K_{t+1}, C_t)$ pairs, and "Figure `` {numref}`stable_manifold` ``" is written out five times in the twelve lines 1026-1073.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 102, 154, 1152. *Example:* "### Digression: Aggregation Theory" (102-151) is fifty lines of representative-consumer aggregation dropped between the statement of the commodity space (84-100) and the description of the economy, and the lecture names it a digression itself - it is the rule's "tangential content that distracts from the main narrative", and lines 146-151 say the payoff only arrives in a later lecture. Worse, the heading levels make "#### An Economy" (154) a *subsection of the digression*, so the model of the lecture is nested inside its own aside. And the exercises are scattered rather than collected: `ck1_ex1` sits inside "## A Turnpike Property" (811) and `ck1_ex2` inside an "### Exercise" H3 under "## Concluding Remarks" (1152), with no "## Exercises" section anywhere.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 146, 511, 606, 609. *Example:* line 146 sets a term being named in italic where the rule asks for bold - "the special *aggregation theory* that lies beneath outcomes in which a representative consumer consumes amount $C$" - and it is the one term in the lecture treated that way, against roughly twenty bolded definitions. In the other direction, bold is used for plain emphasis at 511 ("part of our task is to compute the **optimal** value of $\mu_0$"), 606 ("our new **lower** bound") and 609 ("our new **upper** bound"). A fourth, line 521's "**simple algorithm**", bolds a name for the procedure at 498-503 that was never given that name.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 1079. *Example:* Title Case caption (Manifold, Phase, Plane).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 568. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 1124. *Example:* the phase-plane figure labels a region it never delimits: line 1124 places the text "infeasible consumption" at $(0.5, 5)$, but nothing in the cell draws the feasibility frontier $C = f(K) + (1-\delta)K$ that separates it from the rest of the plane, and the positivity condition stated at line 989 is likewise never plotted, so the annotation points at open space.


## Strengths

- The shooting algorithm is taught by first showing what would work if $\mu_0$ were known (496-503), then why that fails (505-509), then the guess-and-verify fix with its three-way branch on the sign of $K_{T+1}$ (520-526) - the reader learns the algorithm from the obstacle rather than from the recipe.
- The first guess is deliberately wrong: line 562 says "We'll start with an incorrect guess", the figure at 568-583 shows the miss, and 586-590 reads the sign of the error back to the direction the guess must move.
- The turnpike property is demonstrated by superimposing four horizons on one set of axes (782, 792) and stating the pattern in terms of what varies (795-801), rather than by asserting the theorem.
- The chain-rule and product-rule manipulations at 270-299 annotate each step with the rule being applied - `\quad \text{(Chain rule)}`, `\quad \text{(Product rule)}` - and close with the $N_t = 1$ substitution spelled out at 301.
- The phase diagram is built up before it is drawn: $\tilde C(K)$ and $\tilde K(C)$ each get an equation label and a one-line implementation (991-1021), the steady state is defined as their intersection (1023-1026), the two convergent trajectories are computed separately (1056-1058), and 1065-1077 explains each curve and each arrow before the reader sees the figure.

## Recommended actions

1. Fix the axis description at 971 and 1063: both say $K$ is on the ordinate and $C$ on the "coordinate" axis, but the cell sets `ax.set_xlabel('$K$')` and `ax.set_ylabel('$C$')` (1129-1130), so $K$ is on the abscissa and $C$ on the ordinate - the prose describes the figure backwards, twice.
2. Sentence-case the eleven Title Case headings at 82, 102, 154, 216, 250, 477, 691, 785, 913, 967 and 1135 (qe-writing-006, 11 occurrences) and collapse the 79 double spaces (qe-writing-008, 79 occurrences) - together these are the largest mechanical load in the lecture.
3. Fix the two mathematical typos that change meaning: line 1001 writes $K = f(K) + (1 - \delta K) - C$ where the paren belongs around $1-\delta$, and line 1069 reads "the green line graphs the stable traced out by paths", missing the word "manifold".
4. Move the aggregation digression (102-151) out of the main line - into a `{note}` or an appendix - and promote "An Economy" to an H3 so it is not nested inside the digression; then collect both exercises into one "## Exercises" section.
5. Move the three embedded matplotlib titles into figure captions - `axs[i].set(..., title=titles[i])` at 578, 673 and 903 (qe-fig-003, 3 occurrences) - and add `mystnb: figure: caption/name` metadata to the cell at 568 (qe-fig-005).
6. Drop the five `figsize=` overrides at 569, 657, 829, 895 and 1087 (qe-fig-001, 5 occurrences), set `lw=2` on the eight plot calls at 577, 672, 852, 901, 1093, 1097, 1101 and 1102 (qe-fig-008, 8 occurrences), sentence-case the caption at 1083 (qe-fig-004), and convert the raw `python-programming.quantecon.org` link at 31 to a `{doc}` reference (qe-link-002).
7. Sweep the code and spelling: fix `γ!= 1` at 423, the four-quote docstring at 456, the `fix`-for-`fig` typo at 657 and 895, the three over-length lines at 853, 873 and 897, the eight trailing-whitespace lines, and the misspellings "woujld" (505) and "Evalauating" (702).
