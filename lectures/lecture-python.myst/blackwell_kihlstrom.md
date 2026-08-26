# blackwell_kihlstrom

- **Series:** lecture-python.myst
- **File:** `lectures/blackwell_kihlstrom.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-001` ×6; `qe-writing-005` ×4; `qe-writing-003` ×3, +4 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×13; `qe-math-004` ×2; `qe-math-008` ×1, +2 more. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-004` ×2; `qe-fig-001` ×8. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 505, 566, 664, 840, 908, 994, 1074, 1130. *Example:* figsize=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 13. *Lines:* 100, 377, 389, 538, 586, 739, 861, 1335, 1341, 1359. *Example:* non-blackboard `\Pr`.
- **[qe-math-014 (proposed)]** *(reviewer)* — Braces \{…\} for events, parentheses (…) for sets. *Count:* 5. *Lines:* 100, 377, 389, 739, 1335. *Example:* every probability in the lecture is an event - a logical condition on random variables - and every one is written with parentheses: `\Pr(\tilde x_\mu = x_j \mid \tilde s = s_i)` (100), `\Pr(\tilde s = s_i \mid \tilde x_\mu = x)` (377), `\Pr(\tilde x_\mu = x)` (389, 739) and `\Pr(s_1 \mid w^t)` (1335). The proposed convention is braces for events, so these should read `\mathbb{P}\{\tilde x_\mu = x_j \mid \tilde s = s_i\}` and so on; there is no set-valued argument anywhere in the file that would want parentheses.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 6. *Lines:* 362, 366, 397, 404, 859, 877. *Example:* 3 sentences in one paragraph.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 1174. *Example:* H2 Title Case: 'The Data Processing Inequality and Coarse-Graining' (Data, Processing, Inequality, Coarse-Graining).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 6. *Lines:* 35, 40, 44, 48. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 178, 509, 889. *Example:* lines 178-179 split a lambda's parameter list across two lines with the continuation at the same indent as the opening line and trailing whitespace after `lambda q_flat,`; line 509 indents the `zip(...)` continuation to column 9 under a paren opened at column 42; and lines 889 and 935 reach exactly 80 characters.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 1048, 1103. *Example:* caption of 7 words.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 2. *Lines:* 818. *Example:* \mathbf.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 286, 1267. *Example:* line 286 reaches for `\mathscr{G}` for the sigma-algebra of the signal space - the only script letter in the file, used once, and never defined anywhere; line 1267 writes the information-bottleneck objective as $\mathcal{L}[p(T \mid X)]$, the only calligraphic symbol in that section, where a plain $L$ collides with nothing.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 39, 48, 217. *Example:* line 48 is a 56-word sentence that ends "in this QuantEcon lecture `` {doc}`likelihood_bayes` `` as well as several other lectures in this suite of QuantEcon lectures"; lines 39-40 use "appreciate" twice in one sentence ("To appreciate the connection involved, it is helpful to appreciate how..."); and lines 217-218 ("No stochastic transformation can undo the information loss") repeat 214-215 ("The reverse residual is large: no stochastic transformation can recover $\mu$ from $\nu$") in the very next paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 318, 964, 1174. *Example:* line 318 writes "let $Q = p^\mu(X)$ denote the random posterior" - inside the section whose whole subject is the garbling matrix $Q$ defined at 129-146 and bound in code at 111 - and $Q$ then takes a third meaning at 1180-1211 as one of the two distributions in $D_f(P \| Q)$, which line 1306 makes explicit as "$(P, Q) = (\mu_1, \mu_2)$". Application 1 contradicts itself: line 958 says "the unknown state $\tilde s$ is a product parameter $\theta$", and 964-1034 then treat $\theta$ as the consumer's chosen quality investment, while the $\lambda$ units of information priced at $c(\lambda)$ in line 959 disappear and are replaced by $c(\theta) = c\theta^2$ at 968. And the lecture summarises itself at "## Summary" (1152-1171) and then runs for another 210 lines across two further H2 sections (1174, 1316).
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 96, 245, 372, 711. *Example:* four terms are introduced in italic where the lecture's own convention is bold: *Markov matrix* (96), *achievable expected-utility vectors* (245), *posterior belief vector* (372) and *value of experiment $\mu$ given prior $p$* (711). Compare the seventeen terms it bolds at their point of definition - **experiment** (44), **stochastic transformation** (129), **uncertainty function** (296), **standard experiment** (395), **informationally equivalent** (400), **mean-preserving spread** (416), **f-divergence** (1180), and so on. The two criteria named in italic at 60-61 (*Sufficiency*, *Uncertainty reduction*) are the same terms that get bold treatment at 256 and 307.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 351, 1284. *Example:* the garbling operation is the lecture's central object and is never drawn: criterion 2 (275-290) and the theorem sketch at 351-360 describe in words the chain state $\to$ signal of $\mu$ $\to$ kernel $Q$ $\to$ signal of $\nu$, and the reader has eight figures of posterior distributions but no picture of the transformation that generates them. The DPI section is worse: line 1284 writes out a layered Markov chain inline as prose ("layers $X \to T_1 \to T_2 \to \cdots \to T_L \to \hat Y$") and 1272 another ("$Y - X - T$ forms a Markov chain"), then states the resulting chain of inequalities at 1289 - and the whole 140-line section (1174-1313) contains no figure at all.

### Low severity
- **[qe-math-008]** — Explain special notation (vectors/matrices). *Count:* 1. *Lines:* 818. *Example:* ones vector `\mathbf{1}` used 2x with no 'vector of ones' explanation in the prose.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 703. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.


## Strengths

- The sufficiency criterion is tested rather than asserted: `find_stochastic_transform` (163-196) solves for the garbling in both directions and prints the residual each way (199-208), so the reader sees that $\nu = \mu Q$ has a solution and $\mu = \nu Q'$ does not.
- The mean-preserving-spread claim is verified three independent ways - the call-option convex-order sweep over 200 thresholds (548-583), the integrated-CDF test (881-951), and a table of four different concave uncertainty functions (791-806) - which is exactly the right response to a theorem quantified over *all* concave functions.
- Definitions and theorems are placed in labelled `prf:` directives throughout (`def-sufficiency`, `def-economic-criterion`, `def-blackwell-sufficiency`, `def-degroot-uncertainty`, `prop-mean-preservation`, `thm-blackwell`, `thm-kihlstrom`, `thm-data-processing`), so the formal statements are separable from the discussion.
- The note at 743-749 states the limit of the entropy special case honestly - the Blackwell order implies the entropy inequality but not conversely, because one concave function cannot detect every difference in posterior dispersion.
- The closing dictionary table (1349-1363) maps twelve concepts from `` {doc}`likelihood_bayes` `` onto their counterparts here, which is a better closing than a restatement of the theorem.

## Recommended actions

1. Replace the ten `\Pr` operators with `\mathbb{P}` and brace their arguments (100, 377, 389, 538, 586, 739, 861, 1335, 1341, 1359) - this clears qe-math-010 (proposed) (13 occurrences, proposed) and qe-math-014 (proposed) at the same time and is the largest single mathematical fix.
2. Rename the random posterior at 318 and the divergence argument at 1180-1211: $Q$ is already the garbling kernel, in the prose, the mathematics and the code.
3. Fix Application 1 (954-1034): $\theta$ cannot be both the unknown product parameter (958) and the consumer's choice variable (964 onward), and $\lambda$ is introduced at 959 with a cost $c(\lambda)$ that is never used.
4. Drop the eight `figsize=` overrides at 505, 566, 664, 840, 908, 994, 1074 and 1130 (qe-fig-001, 8 occurrences) and remove the `\mathbf{1}\mathbf{1}^\top` bold at 818 in favour of a plain ones vector, explaining it in the prose (qe-math-004 2 occurrences, qe-math-008).
5. Move "## Summary" (1152) to the end, after the DPI and likelihood-ratio sections, or demote those two sections so the lecture does not conclude twice.
6. Bold the four terms currently italicised at their definitions (96, 245, 372, 711), and give the f-divergence generator a letter other than $f$ - $f$ and $g$ are the conditional densities at 48 and again at 1320-1322.
7. Sweep the remaining items: split the six two-sentence paragraphs at 362, 366, 397, 404, 859 and 877 (qe-writing-001, 6 occurrences), collapse the six double spaces at 35, 40, 44 and 48 (qe-writing-008, 6 occurrences), sentence-case the H2 at 1174, shorten the captions at 1048 and 1103 (qe-fig-004, 2 occurrences), move the mid-narrative `{cite}` at 703 (qe-ref-001), fix "synyomyms" at 52, and replace the Unicode μ/ν inside the math span of the matplotlib label at 572 with `\mu`/`\nu`.
