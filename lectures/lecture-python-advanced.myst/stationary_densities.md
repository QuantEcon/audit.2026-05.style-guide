# stationary_densities

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/stationary_densities.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-002` ×5; `qe-writing-001` ×4; `qe-writing-005` ×3, +3 more. |
| Math         | 6/10  | `qe-math-010` (proposed) ×5; `qe-math-009` ×3. |
| Code         | 7/10  | `qe-code-001` ×10. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×6; `qe-fig-004` ×1; `qe-fig-002` ×2, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 7.5/10 | `qe-link-002` ×7. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 10. *Lines:* 833, 834, 838, 879, 901, 915, 922, 1026. *Example:* the same expression is written two ways in the same lecture: 497 has `k[:, t+1] = s * A[:, t] * k[:, t]**α + ...` and 922 has `s * A[:,t] * k[:, t]**α + ...`, dropping the space after the comma in the slice. Multiplication spacing is likewise inconsistent - `loc=i*2` at 879 and 915 and `figsize=(10, 4*J)` at 1026 against `(1 - δ) * x` at 487 and 903 - where the rule asks for `a * b` and reserves the tight form for `a**b`. The three one-line docstrings at 834, 838 and 901 are delimited with a single `"` rather than `"""` (PEP 257), unlike the triple-quoted docstring at 482-485, and they disagree with each other on terminal punctuation (838 and 901 end with a period, 834 does not) and on case ("the TAR Model" at 834). Finally 833, 837 and 900 are top-level `def`s preceded by one blank line where PEP8 asks for two - and 481 in this same lecture uses two.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 696, 794, 824, 890, 959, 1016. *Example:* {figure} without :name:.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 7. *Lines:* 281, 290, 331, 415, 445, 520, 610. *Example:* raw link to python.quantecon.org.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 5. *Lines:* 110, 420, 571, 1054. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 445, 456, 639, 664, 975. *Example:* 445 is 33 words that spend most of themselves on Python mechanics rather than on the estimator ("Given our use of the `__call__` method, an instance of `LAE` acts as a callable object, which is essentially a function that can store its own data (see ...)"), and 452-457 continues for three more paragraphs on the vectorisation of code the lecture does not show, closing with the unsupported "Because the implementation is fully vectorized, it is about as efficient as it would be in C or Fortran". 664 is 40 words carrying a nested parenthetical ("it means we can learn about $\psi^*$ (i.e., approximate the right-hand side of `` {eq}`statd_lln` `` via the left-hand side) without requiring any special knowledge about what to do with $X_0$"), and "This is actually very important" opens it with two words of filler. 639 packs a 36-word sentence around an inline formula in parentheses, $\psi \in \mathscr D \text{ and } \psi = \psi P \implies \psi = \psi^*$, where a displayed line would read cleanly. 975 is 35 words describing the anatomy of a boxplot. Separately, nine paragraphs are wholly parenthesised (88, 118, 135, 225, 244, 276, 312, 454, 800), which signals to the reader that they are optional - but two of them are not: 244 is the only pointer to the appendix proof and 454 carries the reason the class is written the way it is.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 12. *Lines:* 67, 244, 354, 385, 395, 445, 639, 660, 677, 678, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 908, 1026. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 2. *Lines:* 696, 794. *Example:* static image .png.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 314, 639, 644. *Example:* the set of densities on $S$ is written `\mathscr D` at 314, 639 and 644, where a plain $D$ would carry exactly as much information - the symbol appears only three times, is never manipulated, and nothing else in the lecture competes for the letter $D$. The neighbouring notation is otherwise plain ($S$, $P$, $p$, $\psi$, $\phi$), so the script letter is the one piece of decoration in the file.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 66, 244, 328, 353. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 454, 606, 792, 975. *Example:* the Implementation section (441-457) discusses a class whose source is not in the lecture: 443 links out to `lae.py` on GitHub, then 445 explains "our use of the `__call__` method", 449 refers to "the data and stochastic kernel that it stores as its instance data", and 454 says "(This is the reason that we reshaped `X` and `y` inside the class --- to make vectorization work)" - a reference to a reshape that appears nowhere in the file, so "we" did something the reader cannot see. Second, exercise 1 gives away its own answer inside the exercise block: 792 announces "The next figure shows the result of such a computation", 794 shows it, 798 explains what the *solution* added to it ("The additional density (black line) ... added to the solution for illustration"), 802-803 states the conclusion ("the look-ahead estimator is a much tighter fit"), and only then does the dropdown solution at 810-856 appear. Third, 975 tells the reader that in the boxplot "the red line in the center is the median", but matplotlib has drawn the median in orange (`boxplot.medianprops.color: C1`) since 2.0, so the prose describes a figure the cell at 959-973 no longer produces. Fourth, the CDF machinery built in "Beyond densities" (522-596) is dropped one line into the next section - 604 says "We will, however, treat only the density case" and 606 promises "The general case is relatively similar --- references are given below", but the reference list at 675-682 is about stability in the density case and says nothing about the general case.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 68, 281, 530. *Example:* the file contains no italics at all - not one `*...*` span in 1059 lines - so emphasis is carried by bold throughout: "any discrete **time** Markov process" (68), "our lecture on **finite** Markov chains" (281), and "**cannot** be represented as a density" (530) are all emphasis, which the rule assigns to italic. Bold is otherwise used correctly and consistently for definitions (**stochastic kernel on** 130, **Markov operator** 325, **look-ahead** 371, **stationary** 612, **global stability** 649, **ergodicity** 651), so the fix is only to move the three emphases to italic. Line 130 also bolds the trailing preposition, `**stochastic kernel on** $S$`, where the defined term is "stochastic kernel".
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 101, 522, 589. *Example:* the lecture's whole pedagogical device is a term-by-term translation of the finite case into the density case, and it is carried entirely in prose spread over 500 lines - stochastic matrix $P[i,j]$ (101) against family of densities $p(x, \cdot)$ (126), the sum $\sum_{i \in S} P[i,j]\psi_t[i]$ (293) against the integral $\int p(x,y)\psi_t(x)dx$ (306), stationary distribution against stationary density (610-621), and the $\psi P$ convention (314-332). A four-row two-column table would put the correspondence in front of the reader once instead of asking them to hold it. Second, "Beyond densities" (522-596) has neither a figure nor a code cell: its point is that $h(x) := x \mathbf 1\{0 \leq x \leq 1\} + \mathbf 1\{x > 1\}$ (557) puts atoms at 0 and 1 so no density exists, and a single plot of $G(x, \cdot)$ showing its two jumps would make that visible immediately, where the prose asks the reader to "think about it" (560). Its "Computation" subsection (589-596) recommends the empirical distribution function and shows neither code nor output, in a lecture that plots everything else.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 464. *Example:* caption of 7 words.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 678. *Example:* `` {cite} `` in narrative flow: 'and `` {cite} ``'.


## Strengths

- Every step of the finite-to-continuous translation names the object it replaces: 101 defines the stochastic matrix $P[i,j]$ and 126 replaces it with the family of densities $p(x, \cdot)$ "analogous to the finite state case" (128); 293 writes the finite update $\psi_{t+1}[j] = \sum_{i \in S} P[i,j]\psi_t[i]$ and 300-306 replaces the sum with an integral explicitly; and the unusual choice to write the operator on the right, $\psi P$, is given its reason in a note at 327-332 rather than left as a convention to absorb.
- The look-ahead estimator is derived rather than asserted: 399-409 states it, 415-423 gives the strong-law argument as a two-step chain, and 427-428 says which equality comes from the definition of $\psi_{t-1}$ and which from `` {eq}`statd_fdd` `` - and the same treatment is repeated for the stationary-density version at 722-742, where 741-742 again attributes each step to `` {eq}`statd_lln` `` and `` {eq}`statd_dsd` ``.
- The case convention for densities against CDFs is exact everywhere it matters: lowercase $p$, $\phi$, $\psi$ and $f_U$, $f_V$ for densities (239-241), uppercase $G$ (571), $F_t$, $F_{t+1}$ (582), $F_U$, $F_V$ (1052) and $\Phi$ (778) for CDFs - including the appendix proof at 1052-1058, which is precisely the place where a slip between $f$ and $F$ would break the argument.
- The three worked examples at 188-228 each say which special case of `` {eq}`statd_srs` `` they are and give $\mu$ and $\sigma$ explicitly (188 random walk, 206 ARCH, 228 stochastic growth), and the growth model is then carried unchanged through the rest of the lecture - restated at 375-378, computed at 461-511, cited for stability at 686 and reused in exercise 2 at 870.
- Displayed equations are labelled and the labels are genuinely used: `statd_srs` is cited at 188, 206, 228, 248 and 714, `statd_dv` at 247, 254 and 1050, `statd_fdd` at 334, 428, 577 and 587, `statd_lln` at 662, 664 and 741, `statd_tar` at 984 and 999 - so a reader who loses the thread can always find the equation being invoked.
- The three `{note}` admonitions take exactly the asides that would otherwise interrupt the argument: that "Markov chain" is being used in the broad sense (65-70), why the operator is written to the right of its argument (327-332), and that discrete chains are a special case via the counting measure (352-357).

## Recommended actions

1. Fix the Implementation section (441-457) so it does not describe code the reader cannot see - either show the `LAE` class body or drop the references to `__call__`, to "its instance data" and to "the reason that we reshaped `X` and `y` inside the class" (454), which points at a reshape that is not in the file.
2. Redraw the two static PNGs from code that is already in this lecture: {figure} at 696 is the output of the solution cell at 890-934, and the {image} at 794 is the output of the solution cell at 824-856, so both can become executed cells with `mystnb: figure: caption/name` metadata and no raster asset (this also clears the qe-fig-002 and qe-fig-005 hits at those two lines).
3. Correct 975 - matplotlib draws the boxplot median in orange, not red - and while in that cell, name the boxes in the caption instead of via `set_xticklabels` with `fontsize=16` (971).
4. Restructure exercise 1 (754-808) so the answer is not inside the question: move 792-805, including the figure and the sentence about the black line the solution adds, into the `solution-start` block at 810.
5. Give "Beyond densities" (522-596) one figure - a plot of $G(x, \cdot)$ for the truncated process at 555-557 showing the two jumps at 0 and 1 - and add the two-column finite-versus-density correspondence table the prose at 101-135, 292-308 and 610-621 currently spells out.
6. Move the three bold emphases at 68, 281 and 530 to italic, tighten the bold at 130 to the defined term, and replace `\mathscr D` with $D$ at 314, 639 and 644.
7. Sweep the mechanical items: 7 raw `python.quantecon.org` URLs to `{doc}` links (281, 290, 331, 415, 445, 520, 610), the 5 `\mathbb P`/`\mathbb E` without braces (110, 420, 571, 1054), `{cite}` to `{cite:t}` at 678 where the two papers are the sentence's subject, the 4 two-sentence paragraphs (66, 244, 328, 353), 12 double spaces, the 2 `figsize=` overrides (908, 1026), and the PEP8 items above.
