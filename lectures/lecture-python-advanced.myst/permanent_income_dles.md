# permanent_income_dles

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/permanent_income_dles.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-004` ×7; `qe-writing-005` ×2; `qe-writing-003` ×4, +3 more. |
| Math         | 7.5/10 | `qe-math-003` ×9. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×1; `qe-fig-008` ×6; `qe-fig-001` ×1. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 8/10  | `qe-link-002` ×3. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 209, 216, 222, 279, 287, 289. *Example:* the rule explicitly permits capitals for matrices, and the cell at 207-236 takes both choices at once: the scalars and small matrices keep their unicode symbols (`ϕ_c`, `ϕ_g`, `ϕ_i`, `δ_k`, `θ_k`, `γ`) while $A_{22}$, $C_2$, $U_b$, $U_d$ are downcased to `a22`, `c2`, `ub`, `ud` (222-229). Worse, `γ` at 209 is the *technology* matrix $\Gamma$ of 166, not the bliss level $\gamma$ of 85 and 172 - which is what `ub = np.array([[100, 0, 0]])` at 229 actually sets - so the one glyph the lecture reuses is the one that changes meaning between prose and code. 216 `β = np.array([[β]])` rebinds the scalar `β` set at 207 to a 2-D array, so 215 (`θ_k = np.array([[1 / β]])`) must run before it and the cell cannot be re-executed. 222 pads the first matrix row for column alignment (`[[1,   0,   0],`) but leaves the third unpadded (`[0, 1, 0]`), so the alignment the extra spaces were for does not survive. 279 and 287 write `for i in range(25):` with `i` unused where `_` is the convention. And 289 uses `color='r'` where the five sibling calls at 281-284 and 290 all use `c=`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 281, 282, 283, 284, 289, 290. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 9. *Lines:* 161, 163, 165, 166, 170, 171, 172, 173, 256. *Example:* array used as matrix.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 7. *Lines:* 40, 41, 48, 270. *Example:* mid-sentence 'Savings'.

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 3. *Lines:* 40, 41, 270. *Example:* raw link to python-intro.quantecon.org.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 27, 157. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 38, 46, 239, 268. *Example:* 268-271 is spliced together from two sentences and reads as neither: "Consequently, the relevant elements of `econ1.Sc` are the same as in $-F$ occur when we apply other approaches to the same model in the lecture ...". 38-42 is a 45-word sentence that chains three destinations with two bare "and"s ("complementing the other two solution methods described in [Optimal Savings I ...] and [Optimal Savings II ...] and [this Jupyter notebook]"). 46-48 restates what 26-27 has already said - 26-27 gives the {cite}`HS2013` label and the {doc} link with the book's title, and 46-48 repeats the author, year and full title again three sentences later. And 239 says "To check the solution of this model with that from the **LQ** problem", where the verb wanted is compare.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 160, 186, 231, 269. *Example:* the mapping into the DLE framework - the whole content of the lecture - is asserted without the equations it lives in. 156-158 says the problem is mapped "into the framework outlined in Section 4.8 of {cite}`HS2013`" and 160-176 then lists twelve matrices ($\phi_c$, $\phi_g$, $\phi_i$, $\Gamma$, $\Delta_k$, $\Theta_k$, $A_{22}$, $C_2$, $U_b$, $U_d$, $\Lambda$, $\Pi$, $\Delta_h$, $\Theta_h$) without ever writing down the technology, information or preference equations they enter, so a reader who has not opened HS2013 cannot check a single entry. 186-196 then presents the three equations those matrices imply and introduces $k_{t-1}$, $i_t$ and $l_t$ for the first time: $k$ is tied back at 199 ("where $k_t = b_{t+1}$"), $i_t$ is never defined, and $l_t$ at 195 appears nowhere else in the lecture - the $\phi_g$ row of 163 and 165 gives $g_t = -0.00001\,i_t$, so both the symbol and the exponent in $l_t^2 = (0.00001)^2 i_t$ look wrong. The code at 231 sets `x0 = np.array([[0], [0], [1], [0], [0]])`, five elements whose ordering $[h_{t-1}, k_{t-1}, z_t]$ is only given 25 lines later at 256-260, and the third entry (the constant in $z_t$, per row 1 of `a22` at 222) is never explained. And 269 says the elements of `econ1.Sc` "are the same as in $-F$" where $F$ is never defined in this lecture at all.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 44, 239. *Example:* bold is used for emphasis in the two places it is not marking a definition: "uses the **DLE** class" (44) and "that from the **LQ** problem" (239) both emphasise a name the reader already has - `DLE` is set plain at 26 and imported plain at 55 - where the rule assigns emphasis to italic. The genuine definition in the file is bolded correctly (**savings problem**, 62), and the three paragraph labels **Technology:** / **Information:** / **Preferences:** (160, 169, 175) are labels rather than emphasis; no italic appears anywhere in the lecture.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 160, 250. *Example:* the lecture's claim is an equality between two solutions and the equality is never put on the page. 250 prints `econ1.Sc` on its own; 268-271 asserts its relevant elements match $-F$ from another lecture, so the check is left to the reader holding two browser tabs, when printing $-F$ (or an `np.allclose`) beside it would settle it in one cell. Second, the correspondence between the permanent-income objects and the DLE matrices (160-176 in one direction, 253-266 in the other) is carried entirely in running prose with the two state vectors written 10 lines apart; a two-column table - permanent-income object against DLE matrix, with $k_{t-1} = b_t$ as one of its rows - is exactly the kind of layout the rule asks for and would replace the hardest paragraph in the file.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 29, 46, 274. *Example:* 2 spaces.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 277. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 276. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- The model is stated in full before any DLE machinery appears, and every symbol is glossed in the sentence after the display that introduces it: preferences at 67-71 with $E_t$, $c_t$, $u$, $\beta$ explained at 73-76; the budget constraint at 91-95 with $y_t$, $R$, $b_t$, $b_0$ at 97-100; the endowment state-space at 111-116 with $w_{t+1}$, $A_{22}$, $U_y$ at 118-122.
- The three technology equations are motivated one by one instead of being left to the matrices: 198-199 identifies $c_t + k_{t-1} = i_t + y_t$ together with $k_t/R = i_t$ as the permanent-income budget constraint under $k_t = b_{t+1}$, and 201-202 says the third equation is a very small debt-accumulation penalty standing in for the no-Ponzi condition imposed at 126-130.
- The $\beta R = 1$ assumption named in the overview at 38-39 is traceable all the way through: 102 states $R^{-1} = \beta$ in one line, 167 sets $\Theta_k = R$, and 215 implements it as `θ_k = np.array([[1 / β]])` rather than as a second free parameter.
- 182 answers the objection the parameter list at 180 invites - "(The value of $\gamma$ does not affect the optimal decision rule)" - so the reader is not left hunting for the bliss level, and 134-135 does the same job for the square-summability condition at 126-130 by restating it as the borrow-more-and-more plan it rules out.
- The verification is like-for-like and says so: 273-274 names which figures of which lecture and notebook are being reproduced, and 277-292 draws exactly those two panels - 25 sample paths of consumption against income, then of debt - so the comparison is against a stated target rather than a new picture.
- 57 sets `np.set_printoptions(suppress=True, precision=4)` before the one cell whose entire output is a printed matrix (250), so `econ1.Sc` arrives readable rather than in scientific notation.

## Recommended actions

1. Write down (or link to the exact display in `hs_recursive_models`) the technology, information and preference equations that the twelve matrices of 160-176 enter, and fix 195: $l_t^2 = (0.00001)^2 i_t$ uses a symbol found nowhere else in the lecture and squares only the left-hand side, where the $\phi_g$ row of 163/165 gives $g_t = -0.00001\,i_t$.
2. Repair the spliced sentence at 268-271 and either define $-F$ or name the lecture whose $F$ is meant; 269 is the sentence the lecture's conclusion rests on.
3. Rename `γ` at 209 to `Γ` (it is the technology matrix of 166, not the bliss level of 85), restore the capitals on `a22`, `c2`, `ub`, `ud` (222-229), and build 229 from a named bliss level so that $U_b = [\gamma\ 0\ 0]$ at 172 and the literal `100` in the code agree.
4. Split the rebinding at 216 (`β = np.array([[β]])`) into a separate name so the setup cell is re-runnable, and pad the third row of `a22` at 224 to match the alignment of 222.
5. Print $-F$ (or an `np.allclose`) beside `econ1.Sc` at 250, and add a two-column table mapping each permanent-income object to its DLE matrix in place of the prose at 160-176 and 253-266.
6. Recast the nine `\left[ {\begin{array}{c} ... \end{array} } \right]` displays at 161, 163, 165, 166, 170, 171, 172, 173 and 256 as `bmatrix` (qe-math-003) - the file already does this correctly at 140 and 266, so the two forms currently sit in the same lecture.
7. Sweep the remaining measured items: the three double spaces (29, 46, 274), `lw=2` on the six plot calls (281-284, 289, 290), `mystnb` caption/name metadata on the figure cell at 276, drop `figsize=(12, 4)` at 277, and convert the three raw `python-intro.quantecon.org` URLs (40, 41, 270) per qe-link-002.
8. Un-bold **DLE** (44) and **LQ** (239), using italic if emphasis is wanted at all.
