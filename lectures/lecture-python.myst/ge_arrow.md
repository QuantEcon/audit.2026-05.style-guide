# ge_arrow

- **Series:** lecture-python.myst
- **File:** `lectures/ge_arrow.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×15; `qe-writing-005` ×6; `qe-writing-002` ×5, +5 more. |
| Math         | 3/10  | `qe-math-003` ×11; `qe-math-010` (proposed) ×3; `qe-math-004` ×5, +1 more. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×1; `qe-fig-005` ×1; `qe-fig-008` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 940, 1110, 1126, 1130, 1188, 1287. *Example:* three dead locals in `wealth_distribution` - `n = self.n`, `Q = self.Q`, `y, ys = self.y, self.ys` at 940-942 - are assigned and never read (F841); `print (` has a space before the parenthesis at 1110, 1188 and 1287 (E211); and `ex2.P[0,1]` / `ex2.P[1,0]` at 1126 and 1130 omit the space after the comma (E231).
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 11. *Lines:* 540, 550, 566, 597, 607, 623, 627, 721, 731, 754, …. *Example:* array used as matrix.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 5. *Lines:* 67, 187, 704, 711, 765. *Example:* {\bf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 299, 393, 446. *Example:* non-blackboard `\Pr`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 33, 443, 623, 754, 802. *Example:* large blocks are repeated verbatim rather than referred back to. The 'Inputs' bullet at 443-447 reproduces 296-300 word for word, display included; the column vectors $y^k$ and $y$ are displayed three times (566-571, 623-632, 754-763); the two Remarks at 636-641 reappear almost unchanged at 767-772; and the five-step algorithm at 677-687 is re-listed at 802-813 with only the equation labels changed. Line 33 is a single 50-word bullet that chains a utility assumption, a representative-consumer claim, a pricing-kernel formula and an ordering result together.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 6. *Lines:* 528, 583, 636, 641, 767, 772. *Example:* bold is used as a directive label six times - '**Key finding:**' at 528 and '**Remark:**' at 583, 636, 641, 767 and 772 - none of which is a definition. MyST has `{note}` for exactly this, and the file already uses it correctly once at 346-349 for the resolvent operator.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 15. *Lines:* 148, 242, 287, 318, 355, 373, 435, 486, 588, 643, …. *Example:* H2 Title Case: 'Recursive Formulation' (Formulation).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 142. *Lines:* 19, 27, 33, 35, 37, 39, 50, 52, 58, 62, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 1249. *Example:* .set_title.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 4. *Lines:* 187, 201, 311, 449. *Example:* plain TeX and decorative constructions are used where standard LaTeX is shorter: `\hskip.5cm` at 187, `{\beta u'_k(c_{t+1}^k) \pi(s_{t+1}|s_t) \over u'_k(c_t^k)}` at 201-202 instead of `\frac`, and an invented braced operator `{\textrm{Price}}\{\cdot\}` at 311. Most pervasive is `\left( \right)` wrapped around single-symbol arguments - `y^k\left(s\right)`, `u\left(c\right)`, `c\left(s\right)`, `\left[1, \ldots, K\right]` - dense from 449 through 520 and again at 540-570, 601-611 and 651-657, where plain `(s)` and `\{1,\ldots,K\}` would read better.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 583, 636, 767, 772. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 72, 584. *Example:* line 72 warns the reader in a parenthesis that the notation is unreliable - '(Sometimes we inadvertently reverse the recording order and denote a history as $s^t = [s_t, s_{t-1}, \ldots, s_0]$)' - which leaves every later history expression ambiguous rather than fixing the convention. Line 584 points forward in prose, 'See the section on a Finite Horizon Economy below', to a section actually titled '## Finite Horizon' (701), where a `` {ref} `` to a label would carry the reader there.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 584. *Example:* mid-sentence 'Horizon'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 641, 1357. *Example:* the lecture's headline result - state-variable degeneracy, that every agent's continuation wealth returns to zero whenever the Markov state returns to $s_0$ (263-280, 641, 772) - is asserted three times and never drawn, although a simulated $\{\psi_t^k\}$ path along a Markov sample path shows it in one panel. In the finite-horizon example the text says at 1350-1352 that `ψ` and `J` come back as sequences ordered from $t=T$ to $t=0$, and then prints them as raw arrays at 1357-1365; a sequence indexed by $t$ is a line plot. The lecture has exactly one figure in 1387 lines (1242-1252).

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 1243. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 1242. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 1247. *Example:* plot() without lw=.


## Strengths

- The law of iterated values is derived in deliberate parallel with the law of iterated expectations (380-433), the two chains of equalities lined up term for term, so the analogy the section is about is visible in the layout rather than only asserted.
- Every formula the algorithm needs is labelled and then cited by `` {eq} `` at the point of use: `eq:Qformula` (521) at 679 and 805, `eqn:alphakform` (668) at 681, `eq:continwealth` (618) at 685, `eqn:optport` (652) at 687, and `eq:vv`, `eq:w`, `eq:ww` (749, 787, 795) at 807-811.
- One `RecurCompetitive` class covers both the infinite-horizon and the finite-horizon economy (858-905), and the finite-horizon results are then checked numerically against the infinite-horizon ones at $T = 10000$ (1370-1387) - the convergence claim at 1368 is verified rather than stated.
- The resolvent operator is defined in a `{note}` at the moment it first appears (346-349), and the same object is then recognised in the continuation-wealth and value-function formulas later, which is the thread the introduction promises at 50.
- Code identifiers use unicode Greek matching the mathematics - `γ`, `β`, `α`, `ψ`, `λ`, `μ`, `δ` (862-863, 946, 959, 1229, 1265-1267) - with 0 qe-code-002 violations across a 1387-line lecture.

## Recommended actions

1. Fix the class's dependence on notebook globals: `__init__` uses a module-level `n` at 891-902, `pricing_kernel` uses a module-level `P` at 927, and `continuation_wealths` uses `n` and `K` at 955, so `RecurCompetitive` only works because every example redefines `K, n` and `P` first (1030, 1086, 1259, 1312). Use `self.n`, `self.K`, `self.P` and delete the dead locals at 940-942.
2. Sentence-case the 15 Title Case headings at 148, 242, 287, 318, 355, 435, 486, 588, 643, 701, ... (qe-writing-006) and fix the mid-sentence capitals at 584 (qe-writing-004).
3. Correct the index and operator slips: `\sum_i` should be `\sum_k` at 143; 'for all $i$' should be 'for all $k$' at 263, 268 and 271; the last line of the law-of-iterated-values derivation at 431 writes $E V(\cdot)$ where the claim at 419 is about $V$; `Prob(` at 360 should be `\mathbb{P}`; and the two apostrophe transposes at 187 and 473 should be `^\top` (qe-math-002).
4. Cut the duplication: make 443-447 a reference back to 296-300, display $y^k$ and $y$ once instead of at 566, 623 and 754, and merge the two algorithm lists (677-687, 802-813) and the two Remark pairs (636-641, 767-772).
5. Modernise the math markup: convert the 11 `\left[\begin{array}` displays at 540, 550, 566, 597, 607, 623, 627, 721, 731, 754, ... to `bmatrix` (qe-math-003); replace `{\bf S}`, `{\bf T}` at 67, 187, 704, 711 and 765 (qe-math-004); use `\frac` at 201, `\quad` at 187, `\mathbb{P}` at 299 and 446 (qe-math-010 (proposed)); and drop the `\left(\right)` padding around single arguments.
6. Add the two missing exhibits: a simulated continuation-wealth path showing the recurrence claimed at 641 and 772, and a plot of the finite-horizon `ψ` and `J` sequences instead of the raw arrays at 1357-1365; then give the existing figure mystnb metadata (1242), move `set_title` at 1249 into its caption, drop `figsize` at 1243 and set `lw=2` at 1247.
7. Sweep the typos and the whitespace: 'pricing kernal' at 1054, 1109, 1117, 1121, 1286 and 1341; the method name `value_functionss` (981); 'Engle curves' for Engel at 504; '$s^\tau$as' at 79; 'the following a string of inequalities' at 422 (they are equalities); the duplicated comment 'when the initial state is state 2' at 1355 and 1362; the four two-sentence paragraphs at 583, 636, 767 and 772; and the 142 double-space runs.
