# dyn_stack

- **Series:** lecture-dp
- **File:** `lectures/dyn_stack.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-005` ×7; `qe-writing-002` ×5; `qe-writing-003` ×2, +2 more. |
| Math         | 5/10  | `qe-math-002` ×25. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×6; `qe-fig-005` ×6; `qe-fig-008` ×7, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 7.5/10 | `qe-link-002` ×5. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 1031, 1101, 1106, 1110, 1364, 1429. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 1021, 1094, 1151, 1264, 1355, 1417. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 1155, 1156, 1276, 1277, 1426, 1427, 1428. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 5. *Lines:* 42, 324, 519, 814, 1411. *Example:* raw link to python.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 25. *Lines:* 355, 513, 516, 523, 529, 658, 669, 714, 887, 1073. *Example:* apostrophe transpose `y'`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 42, 690, 718, 1100, 1406. *Example:* line 42 drops a preposition - 'our calculations are closely related to ones described [this lecture]'; lines 690-694 announce 'several reasons' and give two; lines 717-719 restate 703-706 without adding anything ('That we distinguish $\check z_t$ from $z_t$ is part and parcel of the Big K, little k device in this instance'); line 1100 has a double space inside a figure legend string, `label='reborn  at t Stackelberg leader'`, so the extra space is rendered into the published figure rather than just sitting in the source; and 'equilbrium' is misspelled twice, at 1406 and 1410, in the heading paragraph of the lecture's concluding comparison.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 7. *Lines:* 252, 470, 476, 494, 538, 718, 813. *Example:* line 252 uses bold for emphasis three times in one sentence - a component that is unstable if solved **backwards** and **stable** if solved **forwards**. Lines 470, 476, 494 and 538 use '**Subproblem 1**' and '**Subproblem 2**' as bold pseudo-headings, each label appearing twice (once to announce the decomposition, once to head the solution), where real subheadings would let the reader navigate between the statement and the solution. The **Big K, little k** device is bolded at 703, bolded again at 718 in a sentence that adds nothing to 703-706, bolded a third time at 809, and then written a fourth way at 813 as “Big $K$, little $k$” inside curly quotes - one device, four presentations.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 30. *Lines:* 311, 314, 315, 339, 438, 441, 445, 557, 570, 583, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 1005, 1097, 1098. *Example:* line 1005 writes `π_matrix = (R + F. T @ Q @ F)` - a space between `F.` and `T`. It is legal Python and it works, but it is plainly a typo for `F.T`, and every other transpose in the same block is written tight (`yt[:, t].T` at 1008, `z[:, t].T` at 1421, `yt_tilde[:, t].T` at 1422). Line 1097 and 1099 write `(- F @ yt).flatten()` with a space after the unary minus. Lines 1098 and 1100 indent the continuation of `axes[0].plot(...)` by four spaces instead of aligning it with the opening delimiter (E128), where the parallel calls at 1105-1111 keep their arguments on one line.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 1027, 1095, 1361. *Example:* figsize=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 685, 1447. *Example:* line 685 says 'We'll report results of implementing this code soon' - no code has been shown at that point. The duopoly section has been pure algebra since line 58, and the first cell that builds $A$, $B$, $R$, $Q$ and calls the LQ solver is roughly 300 lines further on (around 980-1013), so 'this code' has no referent for a reader who has just been handed the matrices at 640-683. Second, the lecture ends on an uninterpreted number: the final cell (1445-1447) evaluates `vt_leader[0] + vt_follower[0] - 2 * vt_MPE[0]` with a comment saying it is 'the difference in total value between the Stackelberg and the MPE', and then the file stops. Nothing states what sign to expect or what the comparison establishes, although 1406-1411 promised it would be 'enlightening to compare equilibrium values for firms 1 and 2 under two alternative settings'.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 323. *Example:* mid-sentence 'Programming'.

### Low severity
_None found._


## Strengths

- The two-subproblem decomposition is set up and then closed: Subproblem 1 is solved as an ordinary LQ problem yielding the Riccati equation and $F$ (500-536), Subproblem 2 is solved in closed form for the free initial jump, $x_0 = -P_{22}^{-1}P_{21}z_0$ (538-551) - and that formula reappears verbatim as the first line of the recursive representation at 725 and as `H_0_0 = -P22inv @ P21` in the code at 994, so the algebra and the implementation are visibly the same object.
- The Big K, little k device is introduced with a reason rather than as a trick: 701-711 explains that a representation of the leader's history-dependent plan requires distinguishing $\check z_t$, which the follower takes as given, from $z_t$, which depends partly on the follower's own decisions - and 795-796 states the payoff precisely, that the representation is cast in terms of $\check z^t$ and *not* $z^t$.
- The lecture states and then demonstrates the asymmetry that motivates it: the follower's problem is recursive in the natural state variables and therefore time consistent (800-805), while the leader's plan is not - and the 'reborn at $t$' experiment at 1088-1112 plots the two paths against each other so the reader sees the leader's incentive to restart.
- Every equality that could be taken on trust is checked in code instead: `(np.abs(v2_direct - v2_direct_alt) < tol2).all()` at 1402 verifies two different computations of the follower's value, and the concluding cells print the three continuation values side by side (1435-1442) before differencing them.
- The mapping from the duopoly model into the general Stackelberg setup is done explicitly and completely (553-683): the state vector, the $4 \times 4$ transition system written out entry by entry, firm 2's revenues as $z_t'R_1z_t$ with $R_1$ displayed, and then $R = \begin{bmatrix} R_1 & 0 \\ 0 & 0\end{bmatrix}$ - so a reader can check every matrix in the code against a display.
- The final comparison is a genuine three-way one - Markov perfect, Stackelberg leader, Stackelberg follower - plotted on one axis with a legend placed outside the frame so the three curves stay readable (1424-1432), and the sign convention (values are negatives of quadratic forms) is applied consistently at 1421-1422.

## Recommended actions

1. Replace the 26 apostrophe transposes with `^\top` (355, 513, 516, 523, 529, 658, 669, 714, 887, 1073 and the rest). Unlike the primes elsewhere in this series these are all genuine transposes of vectors and matrices - $y'Ry$, $u'Qu$, $A'PA$, $B'PB$, $z_t'R_1z_t$, $\check y_t'$ - and at 26 occurrences this is the file's dominant fix (qe-math-002 x26).
2. Work through the figure debt, which is the largest category here: mystnb `name`/`caption` metadata on the 6 figure cells (1021, 1094, 1151, 1264, 1355, 1417), the 6 embedded titles moved into captions (1031, 1101, 1106, 1110, 1364, 1429), `lw=2` on the 13 default-width plots (1097, 1099, 1104, 1105, 1108, 1109, 1155, 1156, 1276, 1277 and the rest), and the 3 hand-set `figsize=` dropped (1027, 1095, 1361) (qe-fig-003 x6, qe-fig-005 x6, qe-fig-008 x13, qe-fig-001 x3).
3. Convert the 5 raw URLs (42, 324, 519, 814, 1411). Three point at lectures in this same series and want a bare `{doc}` reference - `lagrangian_lqdp` at 42, `lqcontrol` at 324 and 519 - while `rational_expectations` (814) and `markov_perf` (1411) live in lecture-python.myst and want `{doc}`intermediate:...``. Note that 42 and 1411 use the `python.quantecon.org` host while 324, 519 and 814 use `python-intro.quantecon.org`, so the file is inconsistent about which site it thinks these lectures are on (qe-link-002 x5).
4. Give the lecture an ending. The last cell (1445-1447) prints a number with no interpretation; one or two sentences saying what $v_{\text{leader}} + v_{\text{follower}} - 2v_{\text{MPE}}$ measures and what its sign shows would close the comparison the section opens at 1406-1411, and would also cash in the 'enlightening' promised there.
5. Fix the math markup: `{\rm max}` at 516 should be `\max`, as line 502 already writes it; the transpose in the same line is written `y^{* \prime}` where `(y^*)^\top` is meant; and the display at 516 carries several runs of stray spaces inside the math that make the source hard to read.
6. Turn the four bold '**Subproblem**' labels (470, 476, 494, 538) into real subheadings so the statement and the solution of each subproblem can be navigated between, switch the three emphasis bolds at 252 to italic, and settle on one presentation of 'Big K, little k' across 703, 718, 809 and 813 - deleting the sentence at 717-719, which restates 703-706.
7. Clear the 30 double spaces, lower-case the mid-sentence capital at 323, and fix the prose slips: the missing preposition at 42, 'several reasons' for two at 690, the double space inside the figure legend at 1100, 'equilbrium' at 1406 and 1410, and the `F. T` typo at 1005 (qe-writing-008 x30, qe-writing-004 x1).
