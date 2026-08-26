# cross_product_trick

- **Series:** lecture-python.myst
- **File:** `lectures/cross_product_trick.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, links  *(JAX out of scope)*
- **Overall score:** 5.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×2; `qe-writing-005` ×2; `qe-writing-003` ×2, +3 more. |
| Math         | 3/10  | `qe-math-002` ×52; `qe-math-006` ×5; `qe-math-013` (proposed) ×1. |
| Code         | N/A   | no executable code cells. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 52. *Lines:* 48, 63, 68, 84, 85, 86, 119, 120, 127, 128, …. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-006]** — Use aligned environment correctly for PDF compatibility. *Count:* 5. *Lines:* 82, 104, 118, 126, 140. *Example:* bare \begin{align*} display block; the corpus convention is $$ … \begin{aligned} … $$.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 33, 92. *Example:* H2 Title Case: 'Undiscounted Dynamic Programming Problem' (Dynamic, Programming, Problem).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 24. *Lines:* 20, 22, 27, 28, 41, 65, 75, 80, 94, 95, …. *Example:* 2 spaces.

### Medium severity
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 77, 80, 94. *Example:* line 80 is a single 55-word sentence that names both 4-tuples, both value-function matrices and both policy matrices before reaching its verb ("...are related to...by"); lines 94-95 are a 58-word sentence carrying the duality claim, the existence of the transformation and the before/after covariance structure at once, and it contains the doubled word "between between"; lines 77-78 read "That the omitted matrix $H=0$ indicates that there are no cross products..." - the sentence has no main clause and says only that H is omitted because it is zero.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 106, 173. *Example:* $F$ carries two unrelated meanings that are never distinguished: the optimal feedback matrix in the LQ half (59, 63, 87) and the measurement-noise loading matrix in the Kalman half (106, 109, 119-120), and the duality table then uses both senses in the same table - row 165 maps $Q$ to the Kalman $FF'$ while row 167 maps the LQ $F$ to $K'$; separately, the lecture ends at 173-175 with an empty `{code-cell}`, so a reader who follows the Algorithm section (131-151) is left with a stub where the numerical demonstration should be.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 74, 145. *Example:* bold is used for emphasis rather than definition in both places it appears outside a heading: **equivalent** at line 74 stresses a word in an ordinary sentence, and **with non-zero covariance** at line 145 stresses a qualifying phrase; neither is a term being defined, so both should be italic.

### Low severity
- **[qe-math-013 (proposed)]** — Reference equations via `` {eq}`label` ``. *Count:* 1. *Lines:* 133. *Example:* malformed `` {eq} `` reference `{eq}`eq:Kalman102}`.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 110. *Example:* i.i.d..


## Strengths

- The duality table (160-168) is a genuinely useful compact device: seven rows pairing each LQ matrix with its Kalman counterpart, which is the one thing a reader will come back to this lecture for.
- Every matrix has its dimensions declared before it is used - the 5-tuple at line 42, the hidden-Markov matrices at 109, and the state and signal dimensions at 113.
- Notation stays plain throughout: single capitals for every matrix, no `\mathcal`, `\mathbf` or `\boldsymbol` anywhere, and starred names ($A^*$, $R^*$, $B^*$, $F^*$) used consistently for the transformed problem.
- The Overview states the transformation strategy as three ordered steps (27-29) before any algebra appears, and points at the prerequisite with a `{doc}` link rather than a raw URL.

## Recommended actions

1. Replace every apostrophe transpose with `^\top` - 52 occurrences, and by far the largest single fix in this lecture (qe-math-002).
2. Convert the five bare `\begin{align*}` blocks at 82, 104, 118, 126 and 140 into `$$ ... \begin{aligned} ... $$`; as written they fail the PDF build, and it is why the `(eq:Kalman102)` label at line 121 never attaches to an equation (qe-math-006).
3. Fix the malformed cross-reference at line 133 - `` `` {eq}`eq:Kalman102} ` ``` closes with a brace instead of a backtick - once the equation at 118-121 is a labelled `$$` block (qe-math-013 (proposed), proposed).
4. Rewrite the two overlong sentences at 80 and 94-95, and fix the typos they carry: "between between" (95), "measurments" (95), "distibuted" (110), "tranformed" (124), "reconstrution" (151), "non zero" (133).
5. Disambiguate $F$: the LQ feedback matrix and the Kalman measurement-noise matrix share the symbol, and the duality table uses both senses; rename one of them or annotate the table rows.
6. Fill in the empty `{code-cell}` at 173-175 with the numerical check the Algorithm section implies, or delete the cell - an empty cell renders as an empty input box on the site.
7. Sweep the remaining mechanical items: sentence-case the two H2s at 33 and 92 (qe-writing-006), collapse the 24 double spaces (qe-writing-008), write "IID" at line 110 (qe-writing-009 (proposed), proposed), and italicise the emphasis at 74 and 145.
