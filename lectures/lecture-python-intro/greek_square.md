# greek_square

- **Series:** lecture-python-intro
- **File:** `lectures/greek_square.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-001` ×2; `qe-writing-005` ×4; `qe-writing-003` ×2, +4 more. |
| Math         | 7.5/10 | `qe-math-004` ×4; `qe-math-009` ×4. |
| Code         | 7/10  | `qe-code-001` ×32. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-003` ×2; `qe-fig-005` ×2; `qe-fig-001` ×2. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 32. *Lines:* 343, 346, 358, 365, 368, 375, 378, 391, 408, 470, …. *Example:* 28 code lines carry trailing whitespace, including whitespace-only lines inside function bodies (343, 346, 358, 365, 368, 375, 378, 470, 474, 476, 478, 483, 533, 535, 539, 540, 542, 543, 648, 661, 662, 679, 693, 695, 699, 704, 706, 710); on top of that `dev = abs(sqrt_σ-np.sqrt(σ))` at 391 drops the spaces around the minus that line 377 has, `y = lambda t, ηs: ...` at 408 binds a lambda to a name where a `def` belongs, and `V[1,1]/V[0,1]` at 649 and `V[1,0]/V[0,0]` at 662 omit the space after the comma in the index that line 353 includes.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 184. *Example:* H2 Title Case: 'Algorithm of the Ancient Greeks' (Ancient, Greeks).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 45. *Lines:* 30, 37, 43, 70, 86, 96, 106, 159, 186, 198, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 531, 690. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 699, 710. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 527, 686. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 4. *Lines:* 317, 321, 323, 329. *Example:* {\bf.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 4. *Lines:* 188, 190, 192, 194. *Example:* `{\mathcal I}` is used four times for the set $\{2, 3, \ldots\}$ - a calligraphic symbol carrying no more information than a plain letter, defined on the spot at 188 and then never used again after 194; the same lecture writes plain $M$, $V$, $\Lambda$ for its matrices.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 23, 86. *Example:* 7 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 291, 309, 608. *Example:* lines 279-306 state the same limit four times over - $\eta_1 = 0$ at 279-289, then "Actually, if $\eta_1 = 0$" at 291-297 adding only that convergence is immediate, then the symmetric $\eta_2 = 0$ case at 299-306 - where two displays would carry the content; line 309 restates the signpost already given at 264; and 576 ("The following notations and equations will help us") with 608 ("These equations will be very useful soon") are two content-free announcements around one short derivation.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 249, 515. *Example:* lines 249-262 re-derive the general solution and the two-equation system for $(\eta_1, \eta_2)$ that {eq}`eq:2diff9`-{eq}`eq:2diff11` already gave at 156-169, switching the root symbol from $\delta$ to $\lambda$ without saying that this is the same result specialised - the reader has to re-map the notation rather than being told; and line 515 breaks the thread outright with "each eigenvector is just a two-dimensional subspace of ${\mathbb R}^3$" in a lecture whose state vector has been $x_t \in \mathbb{R}^2$ since line 439.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 102, 128, 192, 317. *Example:* four definitions set in italics: "We call such a function $g$ a *solution*" (102), "which we can rewrite as the *characteristic equation*" (128), "$\sigma$ is said to be a *perfect square*" (192 - the same term the lecture correctly bolds at 41), and "we constructed an *invariant subspace* of ${\bf R}^2$" (317), which is where the lecture's central concept is introduced and is followed by "Here is what is going on".

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 19. *Example:* {cite} in narrative flow: 'of {cite}`'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 266. *Example:* the algorithm's central claim - that $y_{t+1}/y_t \to 1 + \sqrt{\sigma}$ for almost all initial conditions (266-277) - is never plotted; `solve_sqrt` at 361-379 builds exactly that sequence and then discards everything but the last two entries at 377, and the only ratio figure (686-716) shows the two muted cases where convergence is immediate, so the generic convergence the ancient Greeks relied on is the one thing the reader never sees.


## Strengths

- Every display equation that is referred to again carries a label, and every label is actually cited - `eq:2diff1` (74) at 78, 94, 116, 141, 153; `eq:2diff6` (132) at 134, 159, 214; `eq:second_order` (202) at 208, 246, 249, 329, 429, 458; `eq:cha_eq0` (212) at 216, 235, 503; `eq:secretweapon` (239) at 241, 502; `eq:leq_sq` (262) at 264, 309; `eq:deactivate1` and `eq:deactivate2` (629, 641) at 643, 645, 658, 724 - which is what lets the lecture argue by reference instead of repetition.
- The algebra is checked numerically rather than asserted: {eq}`eq:deactivate1` and {eq}`eq:deactivate2` are each verified by constructing the initial condition and printing `V_inv @ xd` to show the intended component is zero (647-669).
- The same answer is reached twice by different routes - the scalar characteristic equation at 208-306 and the eigendecomposition of $M$ at 429-499 - and the two are then compared explicitly by printing the roots side by side at 502-508.
- Greek names in code are Unicode throughout (`λ_1`, `λ_2`, `ηs`, `σ`, `Λ`, `V_inv`), so the implementation reads as the mathematics does.
- The Russell epigraph is load-bearing rather than decorative: the exercise at 730-739 asks the reader to put Russell's two-column recursion into the matrix form the lecture developed and match its eigenvalues to $1 \pm \sqrt{2}$.

## Recommended actions

1. Fix the dimension claims: line 515 calls each eigenvector "a two-dimensional subspace of ${\mathbb R}^3$" and 558 speaks of constructing "2-dimensional invariant subspaces", but $M$ is $2 \times 2$, $x_t \in \mathbb{R}^2$, and each eigenvector spans a one-dimensional invariant subspace of $\mathbb{R}^2$.
2. Fix the transposed eigenvector indices: line 523 states $\lambda_i = V_{i,1}/V_{i,2}$, and the figure annotations at 540 and 543 are labelled $V_{1,1}/V_{1,2}$ and $V_{2,1}/V_{2,2}$, but the code computes `V[0,0]/V[1,0]` and `V[0,1]/V[1,1]` - that is $V_{1,i}/V_{2,i}$, a ratio within one eigenvector. As written the text and labels divide one eigenvector's entry by the other's.
3. Replace `{\bf R}^2` at 317, 321, 323 and 329 with `\mathbb{R}^2`, which is what line 515 already uses (qe-math-004 x4), and replace `{\mathcal I}` at 188-194 with a plain letter.
4. Run one whitespace sweep: 45 multi-space runs in the prose (qe-writing-008 x45) and 28 code lines with trailing whitespace.
5. Move the two `axs[...].set_title` calls at 699 and 710 into mystnb figure captions and add `mystnb: figure: name/caption` metadata to the two plotting cells at 527 and 686, dropping the `figsize` overrides at 531 and 690 (qe-fig-003 x2, qe-fig-005 x2, qe-fig-001 x2).
6. Bold the four definitions now in italics - **solution** (102), **characteristic equation** (128), **perfect square** (192), **invariant subspace** (317) - and lower-case the heading at 184 to "Algorithm of the ancient Greeks" (qe-writing-006 x1).
7. Compress 279-306 to two limit statements, cut the empty signposts at 309 and 576-608, and add the missing figure: plot $y_{t+1}/y_t$ against $t$ for an arbitrary $(y_{-1}, y_{-2})$ converging to $1 + \sqrt{\sigma}$, using the sequence `solve_sqrt` already computes at 374. Also move the `{cite}` at 19 out of the sentence flow (qe-ref-001).
