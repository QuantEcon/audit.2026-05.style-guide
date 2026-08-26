# markov_perf

- **Series:** lecture-python.myst
- **File:** `lectures/markov_perf.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×8; `qe-writing-003` ×3; `qe-writing-008` ×12, +1 more. |
| Math         | 5/10  | `qe-math-002` ×37. |
| Code         | 7/10  | `qe-code-002` ×2; `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×6; `qe-fig-003` ×1; `qe-fig-002` ×3, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 480, 509, 629, 730, 740, 839. *Example:* {figure} without :name:.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 37. *Lines:* 202, 203, 204, 205, 206, 248, 249, 250, 265, 266, …. *Example:* apostrophe transpose `x_t'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 8. *Lines:* 91, 177, 188, 229, 326, 332, 351, 427. *Example:* H3 Title Case: 'Example: A Duopoly Model' (Duopoly, Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 12. *Lines:* 80, 148, 149, 175, 220, 328, 330, 353, 392. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 548, 623, 636, 642. *Example:* the $R_1$ literal at 548-550 writes the same entry three different ways in three adjacent rows - `-a0/2` (548), `-a0 / 2.` (549), `-a0 / 2` (552 in $R_2$) - and mixes integer and float zeros within one row (`0` and `0.` at 550); `float(x.item())` at 623 casts a value `.item()` has already returned as a Python float; and `frameon=0` at 636 and 642 passes an integer where the same lecture writes `frameon=False` at 496. The space-aligned matrix literals themselves are fine - laying them out to look like matrices is the mathematical-notation exemption qe-code-001 allows.
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 453, 455. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 492, 630, 848. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 509, 730, 740. *Example:* static image .png.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 495. *Example:* .set_title.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 444, 476, 446. *Example:* three sentences describe a document that is not the one in front of the reader. Line 444, 'Running the code produces the following output', is followed by nothing - the `:load:` cell at 438-442 has already executed and shown its output above the sentence. Line 476 says 'The following program imports $F1$ and $F2$ from the previous program along with all parameters', describing a two-file structure the notebook does not have: the cell at 480 imports nothing and depends on names the loaded cell left in the namespace. And line 446 writes '$F_i$ is indeed optimal for firm $i$ taking $F_2$ as given', mixing the generic index with the specific one inside a single clause, where the next sentence at 448 says F2 and F1 plainly.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 492. *Example:* the body's only generated figure (492-497) puts total output and price on a single un-labelled axis, distinguished only by a legend and an embedded title, even though the two series measure different things on different scales. The exercise solution at 629-643 plots exactly this comparison correctly - two stacked panels, each with `xlabel` and `ylabel` - so the lecture already contains the better version of its own figure, 140 lines later and inside a dropdown.


## Strengths

- The `prf:definition` at 143-156 does more than state the fixed point: it unpacks both words of the name, saying what 'Markov' restricts (dependence on the current state only) and what 'Perfect' buys (optimizing behaviour at all future states), and then makes the point that this includes states never reached on the equilibrium path.
- The equilibrium is verified rather than asserted: F2 is substituted into player 1's transformed problem `` {eq}`eq_mpe_p1p` ``-`` {eq}`eq_mpe_p1d` ``, re-solved with the general-purpose LQ class, and compared with `np.allclose` (452-465) - a real best-response check on the output of `nnash`, not a restatement of it.
- The general coupled-regulator setup lists the dimension of every one of the eight matrices before any of them is used (220-227), and the three substitution shorthands $\Lambda_{it}$, $\Pi_{it}$, $\Gamma_{it}$ are defined at 264-266 exactly where the substitution creates them, so the transformed problem reads as an ordinary single-agent LQ problem.
- The MPE is given economic content by matching it against a monopoly benchmark with deliberately comparable initial conditions - $q_0 = 2.0$ for the monopolist to mirror $q_{10} = q_{20} = 1.0$ in the duopoly (515) - so the output and price comparison at 517 means something.
- Exercise 2 poses a genuine modelling task, Judd's two-good inventory duopoly, gives the full list of variables and cost functions (659-714), and supplies target figures for both $\delta = 0.02$ and $\delta = 0.05$ so the reader can check the comparative static as well as the level.

## Recommended actions

1. Fix `` {eq}`eq_mpe_cle` `` at 424: the closed loop is $x_{t+1} = (A - B_1 F_1 - B_2 F_2)x_t$, not $A - B_1F_1 - B_1F_2$ - the code at 481 and 569 uses `B2 @ F2`, and 472 and 477 tell the reader the code implements this equation.
2. Replace every apostrophe transpose with `^\top` - 35 occurrences concentrated in the coupled-Riccati algebra at 202-206, 248-250, 264-266 and 276-310, where they sit next to primed matrices and are hardest to read (qe-math-002, a very-high-weight rule).
3. Lower-case the eight Title Case section headings (91, 177, 188, 229, 326, 332, 351, 427) - only the H1 takes title case (qe-writing-006, 8 occurrences, very-high weight).
4. Generate the three static PNGs in code (509, 730, 740) and give all six figures descriptive names (480, 509, 629, 730, 740, 839); the $\delta = 0.05$ image at 740 is currently a result no cell in the lecture can reproduce (qe-fig-002 x3, qe-fig-005 x6).
5. Rewrite the three sentences at 444, 446 and 476 so they describe the notebook as it is, and consider inlining `duopoly_mpe.py` (439) - as it stands the matrices the next four cells depend on are invisible in the lecture source.
6. Split the body figure at 492 into two labelled panels, matching the treatment at 630-643, and move the embedded title into a caption (qe-fig-003, 1 occurrence); drop the three `figsize` overrides at 492, 630 and 848 unless the aspect ratios are deliberate.
7. Rename the `beta` variable at 453 to `β` to match `β` at 541 (qe-code-002), close the twelve double spaces (80, 148, 149, 175, 220, 328, 330, 353, 392, ...) (qe-writing-008), and clean the four code items above.
