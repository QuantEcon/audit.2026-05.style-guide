# ak2

- **Series:** lecture-python.myst
- **File:** `lectures/ak2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×2; `qe-writing-005` ×4; `qe-writing-003` ×4, +3 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×5; `qe-fig-003` ×3; `qe-fig-008` ×27, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 655, 758, 1012, 1098, 1177, 1242. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 734, 801, 816, 843, 1154. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 27. *Lines:* 660, 668, 676, 763, 764, 772, 773, 781, 782, 817, …. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 176, 1210. *Example:* H2 Title Case: 'Activities in Factor Markets' (Factor, Markets).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 197. *Lines:* 26, 29, 32, 40, 48, 50, 56, 75, 77, 78, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 946, 1075, 1142. *Example:* lines 946 and 1052 write the `brent_max` upper bound as `W*(1-τ)-δy-1e-6` with no space around any of the four binary operators, and `**` is the only operator the rule exempts; lines 1075-1076 join the two convergence tests with a backslash continuation where PEP8 asks for parentheses; three lines reach exactly 80 characters (1142, 1166, 1201) and line 1085 carries trailing whitespace. `class AK2():` at 957 also has empty parentheses where `class ClosedFormTrans:` at 540 does not.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 819, 1026, 1031. *Example:* plt.title.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 229, 507, 859, 1207. *Example:* line 229 is a 48-word sentence with three semicolon-joined clauses, and line 232 then restates its content in full ("The firm thus sells output to old people, young people, and the government"); the three bullets at 509-511 give the $t=0$ shock twice - bullet one is "a time-varying government policy sequences that disrupts an original steady state" and bullet three is "sudden revelation of a new government policy in the form of sequences starting at time $t=0$"; line 859 is a 44-word sentence; line 1207 uses "comparing to" twice in 27 words.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 40, 246, 498, 885. *Example:* line 40 promises that the model "is a good setting for illustrating a **shooting method** for solving a system of non-linear difference equations with initial and terminal condition", and no shooting method appears anywhere - the lecture uses a closed form (348-493) and then a sequence-space fixed point (864-1123). Line 246 introduces the initial old person's assets as $A_0$, a symbol never defined: assets are only ever written $A_{t+1}$ (192, 280, 317), and the same equation charges the $t=0$ old person $\delta_{ot}$ rather than $\delta_{o0}$ (249, 256), with the same index slip at 281. Lines 498-500 are a commented-out HTML block still carrying a drafting note to a co-author ("<font color='red'>Zejin: I tried to edit the following part..."). And the lecture defines "competitive equilibrium" twice, differently: the definition at 324-328 requires the allocation to solve the firms' problems, the one at 885-895 drops that requirement and adds the lump-sum taxes.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 178, 187, 324, 885. *Example:* the lecture uses bold for four structural labels rather than for defined terms - `**Old people:**` (178) and `**Young people:**` (187) as headings over bullet lists, and `**Definition:**` (324, 885) as a label introducing a definition rather than naming the thing defined - while using italic nowhere at all in 1280 lines. The genuine definitions in the file (**policy** 82, **allocation** 92, **price system** 109, **numeraire** 212, **state variables**/**control variables** 537) are correctly bolded, so the convention is otherwise sound.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 176. *Example:* a lecture titled "Transitions in an Overlapping Generations Model" never draws the overlap. "Setting" (52-113) and "Activities in Factor Markets" (176-196) describe entirely in prose who is alive at each date, that the old bring $K_t$ and $D_t$ in and sell $K_t$ to the young, and that the young buy $D_{t+1}$ maturing at $t+1$ - a two-row generations timeline with the transfers drawn as arrows between cohorts is the standard figure for exactly this, and all eight figures in the lecture are transition-path panels instead.


## Strengths

- The fixed-point solver is validated against the closed form before it is trusted with anything new: line 1131 says so explicitly and the run at 1133-1156 reproduces the {ref}`exp-tax-cut` experiment with the lump-sum taxes muted.
- `simulate` takes `τ_pol`, `D_pol` and `G_pol` and requires exactly two of the three, computing the remaining one from the government budget constraint (583-594, 617-631) - so a policy experiment is specified by naming which instrument is residual, and the prose at 529-535 says that is the design.
- Every experiment is set up as a numbered list of policy commitments before any code runs (694-696, 795-797, 837-841), and each is followed by an interpretation in terms of who gains and who loses (822-828, 857-861, 1272-1280).
- `verbose=True` plots the price and tax-rate paths at every iteration of the fixed point (1022-1032), turning the convergence of the algorithm into something the reader can watch rather than take on faith.
- The cross-references between experiments use labelled targets - `(exp-tax-cut)=` at 689 and `(exp-expen-cut)=` at 790, cited at 861, 899, 1160, 1207 and 1228 - so the comparisons the prose makes are navigable.

## Recommended actions

1. Collapse the five copies of the nine-panel plotting block into one function: 649-679 (`ClosedFormTrans.plot`), 757-786, 1092-1122 (`AK2.plot`), 1176-1204 and 1241-1269 are the same 30 lines with only the labels changed. Both `plot` methods also read the globals `T` and `init_ss` (660-661, 1103-1104) instead of instance state, so a `plot()` call silently depends on whatever `T` happens to be bound to at the time.
2. Fix the four mathematical errors: {eq}`eq:firmfonc` at 225 gives $r_t = \alpha K_t^{\alpha} L_t^{1-\alpha}$ where the exponent must be $\alpha - 1$ (the code at 444 has it right); {eq}`eq:Klawclosed` at 365 subtracts $D_t$ where the code at 610-611 subtracts $D_{t+1}$, and the line ends with a stray `\\`; $\delta_{ot}$ appears in the $t=0$ and $t+1$ budget constraints at 256 and 281 where $\delta_{o0}$ and $\delta_{o,t+1}$ belong; and line 309 writes `C_{0t+1}` with a zero for the letter o.
3. Collapse the 197 double and triple spaces (qe-writing-008, 197 occurrences) - by far the largest mechanical item in the lecture - and sentence-case the two Title Case H2s at 176 and 1210.
4. Set `lw=2` on the 27 plot calls that lack it (660, 668, 676, 763, 764, 772, 773, 781, 782, 817, and 17 more) and drop the six `figsize=` overrides at 655, 758, 1012, 1098, 1177 and 1242 (qe-fig-008 27 occurrences, qe-fig-001 6 occurrences).
5. Reconcile the two definitions of competitive equilibrium (324-328 and 885-895) into one, and either add the shooting method promised at line 40 or drop the promise.
6. Add a generations diagram to "Activities in Factor Markets", and give the `-D/K` figure at 816-819 an axis label instead of `plt.title('-D/K')` (part of qe-fig-003, 3 occurrences at 819, 1026, 1031).
7. Delete the commented-out drafting note at 498-500, add `mystnb: figure: caption/name` metadata to the five bare figures at 734, 801, 816, 843 and 1154 (qe-fig-005, 5 occurrences), fix the PEP8 spacing at 946 and 1052, and correct the spellings "Equilbrium" (322), "caluations" (866), "expeditures" (841), "perople" (861), "goverment" (190), "the the" (1274) and "is good laboratory" (38).
