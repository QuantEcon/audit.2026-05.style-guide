# complex_and_trig

- **Series:** lecture-python-intro
- **File:** `lectures/complex_and_trig.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×6; `qe-writing-001` ×2; `qe-writing-003` ×2, +4 more. |
| Math         | 9.5/10 | `qe-math-009` ×1. |
| Code         | 7/10  | `qe-code-001` ×10. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-007` ×2; `qe-fig-005` ×2; `qe-fig-003` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 10. *Lines:* 100, 103, 143, 146, 152, 153, 347, 351, 416, 418. *Example:* line 100 `#set default figure size` has no space after the hash; lines 143, 347 and 351 leave a single space before an inline comment where two are required; lines 103 and 146 under-indent a continuation line (18 spaces against a visual-indent target of 19; 4 against 13); lines 152 and 153 put a space before a comma (`r+0.01 ,` and `1 ,`); lines 416 and 418 space the same product two ways in one expression (`cos(ω)*cos(θ) - sin(ω) * sin(θ)`).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 138, 139, 140, 141, 337. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 6. *Lines:* 44, 106, 161, 179, 358, 421. *Example:* H3 Title Case: 'Complex Numbers' (Numbers).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 100, 135, 335. *Example:* style override.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 145. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 122, 326. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 2. *Lines:* 342, 343. *Example:* spine removal.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 406, 563. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 66, 376. *Example:* two redundancies. Lines 66-67 redefine the real and imaginary parts of z twenty lines after line 46 already defined them in the same bold form. Lines 373-381 present cos(omega+theta) and sin(omega+theta) via the exponential formulas, which is only the definition restated; line 383 then says 'We can also obtain the trigonometric identities as follows' and gives the actual derivation, so the earlier block adds nothing.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 215, 254. *Example:* line 215 is a sentence fragment - 'For each element of a sequence of integers $n = 0, 1, 2, \ldots, $.' - that never says what is being computed, and then the display at line 223 introduces x_n as if it had been defined. Line 254 reads 'has roots $z_1, z_1$', a clause with no subject dangling off the display above it, with the second root's subscript wrong.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 161, 358. *Example:* a lecture titled 'Complex Numbers and Trigonometry' has two figures. De Moivre's theorem (lines 161-177) is about what raising re^{i theta} to a power does in the complex plane - a rotation and a rescaling - and is presented as three lines of algebra with 'and compute'. The angle-sum identities (lines 358-404) are the canonical unit-circle picture and get none either, although the polar diagram at line 122 shows the lecture can draw exactly that.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 234, 256. *Example:* 2 spaces.

### Low severity
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 191. *Example:* line 191 writes the negated angle as `\cos{(\text{-}\theta)}` and `\sin{(\text{-}\theta)}`, using a `\text{}` box to produce a character that a plain minus sign already gives.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 204. *Example:* line 204 bolds a name for emphasis - 'We recognize this as a theorem of **Pythagoras**' - where the rest of the file reserves bold for the eleven terms it defines.


## Strengths

- Every symbolic claim in the lecture is checked with sympy rather than asserted: the angle-sum identities at lines 410-419, the double-angle identities at 581-596, the product identities at 656-668, and the full 3x3 orthogonality table at 713-724.
- The polar diagram at lines 122-159 labels z, r, x, y and theta directly on the plot, so the three forms of a complex number introduced at line 53 become a single picture the reader can point at.
- The Overview says what the lecture is for and where it is used next - Samuelson's multiplier-accelerator, with a `` {doc} `` link at line 36 - and explicitly offers itself as a stand-alone trigonometry refresher.
- Example 3 carries the complex-conjugate machinery through to a concrete second-order difference equation and then solves for omega and p numerically with `nsolve` at lines 296-318, so the algebra ends in a number and a plot.
- The final exercise closes the loop on why any of this matters: line 728 explains that orthogonality is what makes Fourier decomposition possible, rather than leaving the integral table as an isolated result.

## Recommended actions

1. Repair the two broken passages in Example 2 and Example 3: complete the fragment at lines 215-217 so it states what x_n is before the display at 223 uses it, and give line 254 a subject and the correct second root ($z_1, z_2$).
2. Add a complex-plane figure to De Moivre's theorem (line 161) showing the rotation and rescaling under z^n, and a unit-circle figure to the angle-sum identities (line 358); at present the lecture's two most visual results are pure algebra.
3. Cut the redundant redefinition at lines 66-67 and the redundant display at lines 373-381, both of which restate material already given.
4. Sentence-case the six Title Case headings at lines 44, 106, 161, 179, 358 and 421 (qe-writing-006).
5. Figure hygiene: add mystnb metadata to the two figure cells at lines 122 and 326 (qe-fig-005), set `lw=2` on the five plot calls at 138-141 and 337 (qe-fig-008), drop the size overrides at 100, 135 and 335 (qe-fig-001), move the embedded title at 145 into a caption (qe-fig-003), and restore the spines removed at 341-343 (qe-fig-007).
6. Fix the numeric-versus-symbolic pi collision: line 124 binds `π` to `np.pi` (a float) and line 510 imports sympy's exact `pi`, and the symbolic integral at line 483 is then evaluated with the float bounds `(ω, -π, π)` while the equivalent integrals at lines 517 and 524 correctly use `pi`.
7. Fix the ten PEP8 sites listed above, the typo 'at the heard of' at line 234, the bullet list collapsed onto one line at lines 288-290, the double spaces at lines 234 and 256, the two-sentence paragraphs at lines 406 and 563, and settle on one delimiter-sizing macro - the file currently mixes `\Big(` (85), `\big(` (174) and `\bigg(` (449).
