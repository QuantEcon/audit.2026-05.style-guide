# cross_product_trick

- **Series:** lecture-dp
- **File:** `lectures/cross_product_trick.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, links  *(JAX out of scope)*
- **Overall score:** 5.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×2; `qe-writing-005` ×2; `qe-writing-002` ×2, +3 more. |
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
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 80, 94. *Example:* the two sentences that carry the lecture's main claims are also its longest. Line 80 is a single 55-word sentence naming two 4-tuples, two matrix pairs and the relation between them before it reaches its verb ('are related to ... by'); lines 94-95 run ~60 words and contain the duplicated word 'between between' plus the typo 'measurments'. Both want splitting into one clause per sentence.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 74, 145. *Example:* bold used for emphasis where italic is wanted: line 74 'an **equivalent** problem without cross-products' and line 145 'the original problem **with non-zero covariance** between shocks'. Neither is a definition - both are stressing a contrast with the preceding paragraph. The bold on **duality** at 94 is correct, since that sentence is where the term enters the lecture.

### Low severity
- **[qe-math-013 (proposed)]** — Reference equations via {eq}`label`. *Count:* 1. *Lines:* 133. *Example:* malformed {eq} reference `{eq}`eq:Kalman102}`.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 135. *Example:* the algorithm's first step contradicts the formula it points at. Lines 135-136 say to 'compute $\Sigma, K^*$ using the ordinary Kalman filtering formula with $BF' = 0$', but the displayed system at 140-143 is not the ordinary formula with $BF'=0$ - it is the ordinary formula with $A$ replaced by $A^*$ and $BB'$ by $B^*{B^*}'$, the transformed matrices defined at 126-129. A reader who follows 135 literally substitutes into 119-120 and gets $A$, not $A^*$, so the step as written does not produce the state it claims.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 110. *Example:* i.i.d..


## Strengths

- The duality table at 160-168 pairs each LQ matrix with its Kalman counterpart ($A \leftrightarrow A'$, $H \leftrightarrow FB'$, $P \leftrightarrow \Sigma$), so the two halves of the lecture are explicitly tied together instead of being left as two parallel derivations the reader has to align.
- The LQ transformation at 82-88 is given as a complete five-line system - $A^*$, $R^*$, the Riccati equation in the starred matrices, $F^*$, and the recovery $F = F^* + Q^{-1}H$ - so a reader has every piece needed to implement it without going elsewhere.
- Conformability is stated for every matrix as it is introduced (line 42 for the LQ 5-tuple, line 109 for the hidden Markov model), which makes the transposes in the displayed formulas checkable at a glance.
- The forward pointer at line 28 uses the `{doc}` form with an explicit title (`{doc}`Linear Control: Foundations <lqcontrol>``) rather than a bare URL, and it names exactly the lecture whose no-cross-product formulas the transformation is designed to reach.

## Recommended actions

1. Replace the 52 apostrophe transposes with `^\top` (qe-math-002) - at 52 occurrences in a 175-line file this is the dominant fix, and it touches nearly every display block plus the duality table at 162-167.
2. Convert the 5 bare `\begin{align*}` blocks at 82, 104, 118, 126 and 140 into `$$ ... \begin{aligned} ... \end{aligned} ... $$` (qe-math-006, build risk). While doing 118-121, note that the label is currently attached as `\end{align*} (eq:Kalman102)`, which will not survive the conversion - move it to the `$$ ... $$ (eq:Kalman102)` form.
3. Fix the malformed cross-reference at line 133: `` {eq}`eq:Kalman102} `` closes with a brace instead of a backtick, so the reference does not resolve (qe-math-013 (proposed), proposed).
4. Reconcile the algorithm step at 135-136 with the formulas at 140-143 - say that $A^*$ and $B^*{B^*}'$ from 126-129 are substituted into the ordinary formula, rather than that $BF'$ is set to zero.
5. Sentence-case the two H2 headings at 33 and 92 ('Undiscounted dynamic programming problem', 'Kalman filter') and write IID at line 110 in place of 'i.i.d.' (qe-writing-006 x2, qe-writing-009 (proposed) proposed x1).
6. Break the 55-60 word sentences at 80 and 94 into one idea each, and fix the four typos along the way: 'between between' (95), 'measurments' (95), 'distibuted' (110), 'tranformed' (124) and 'reconstrution' (151).
7. Clear the 24 double spaces (qe-writing-008), switch the emphasis bolds at 74 and 145 to italic, and delete the empty `{code-cell}` at 173-175, which renders as a blank input cell at the foot of the published page.
