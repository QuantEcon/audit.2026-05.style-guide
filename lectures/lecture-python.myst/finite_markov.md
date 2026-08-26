# finite_markov

- **Series:** lecture-python.myst
- **File:** `lectures/finite_markov.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×11; `qe-writing-004` ×4; `qe-writing-001` ×2, +4 more. |
| Math         | 3.5/10 | `qe-math-010` (proposed) ×21; `qe-math-003` ×6. |
| Code         | 8/10  | `qe-code-001` ×4; `qe-code-004` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×8; `qe-fig-002` ×6; `qe-fig-008` ×2, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 6. *Lines:* 200, 538, 572, 607, 635, 1115. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 200, 538, 572, 607, 635, 801, 1058, 1115. *Example:* {figure} without :name:.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 6. *Lines:* 156, 179, 457, 548, 923, 1016. *Example:* array used as matrix.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 21. *Lines:* 99, 100, 110, 368, 369, 370, 437, 903, 911, 937, …. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 11. *Lines:* 223, 295, 319, 419, 440, 466, 742, 790, 893, 965, …. *Example:* H3 Title Case: 'Rolling Our Own' (Our, Own).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 35. *Lines:* 71, 174, 225, 227, 229, 340, 374, 376, 447, 472, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 312, 316, 1274, 1293. *Example:* single space before an inline comment where PEP8 asks for two, at 312, 316 and 1274 (`n = 14 # Total number of web pages (nodes)`), and whitespace before the dict colon at 1293 (`{alphabet[i] : r[i] for i in range(n)}`, E203). The matrix-aligned padding at 1063-1064 is the mathematical-notation exception and is left alone.
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 312, 316. *Example:* %time.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 809, 1067. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 1079, 1081. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 309. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 227, 1377. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 79, 402, 497, 760. *Example:* three sentences are ungrammatical as written - 'It is too not difficult to check' (79), 'To get uniqueness an invariant distribution' (697), 'one way to finding it is to solve the system' (760). Line 402 says 'This is very important, so let's repeat it' and then displays at 404-408 and again at 412-416 what 396-400 has already stated. Lines 490-501 make the same cross-sectional point in four consecutive paragraphs, ending with 'This is exactly the cross-sectional distribution' after the previous three have each said so.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 466, 1004, 1099. *Example:* '### Example 2: Cross-Sectional Distributions' at 466 is the second example of the marginal-distributions section, but '### Example 1' and '### Example 2' already exist at 135 and 172 as different examples, and this one's anchor is `mc_eg1-1` - three numbering schemes overlapping. Line 1004 closes '### Expectations of Geometric Sums' by introducing a new term in scare quotes, 'applying the **resolvent operator**', with no explanation and no sequel; '## Exercises' begins on the next line. Line 1099 is a parenthetical tangent about search ranking and competitive-equilibrium prices dropped into the middle of the PageRank exercise statement.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 472, 494, 495. *Example:* mid-sentence 'Law'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 687, 708. *Example:* both theorems are labelled with bold prose - '**Theorem.** Every stochastic matrix $P$ has at least one stationary distribution' (687) and '**Theorem.** If $P$ is both aperiodic and irreducible' (708) - which is neither a definition nor emphasis. The file otherwise reserves bold correctly for the terms it defines (71, 90, 92, 516, 531, 603, 622, 671, 683, 698, 718, 967), and MyST has `{prf:theorem}` for exactly this job.

### Low severity
_None found._


## Strengths

- Cross-referencing is the lecture's strongest feature: named anchors at 65, 134, 171, 346, 418, 465, 673, 707, 866, 871 and 892 are pulled back in by `` {ref} `` at 445, 474, 525, 726, 795, 836, 874, 1011 and 1181, so a 1377-line lecture stays navigable and never says 'as discussed earlier' without a link.
- Every equation that is reused carries a label and is cited by `` {eq} ``: `fin_mc_fr` (387) at 396 and 660, `mdfmc2` (413) at 428, 432 and 974, `mc_cce2` (957) at 976, `llnfmc0` (852) at 867 and 869, `p_unempemp` (152) at 488, `eq:eqpsifixed` (764) at 768 and 774.
- Probability events are written with braces throughout - $\mathbb P \{X_{t+1} = y \mid X_t\}$ (99-100), $\mathbb P \{X_{t+1} = y \mid X_t = x\}$ (110), the total-probability decomposition (368-370), $\mathbb P \{X_{t+m} = y \mid X_t = x\}$ (437) - so the proposed qe-math-014 (proposed) convention holds without exception.
- The homemade simulator at 248-270 is checked against `qe.MarkovChain` on the same matrix (287-306) and then timed against it (311-317), so 'roll our own first' ends in a measured comparison rather than an assertion.
- Both theorems point at real proofs rather than waving - Brouwer or EDTC theorem 4.3.5 at 691, `` {cite}`haggstrom2002finite` `` theorem 5.2 at 713 - and the footnote at 1377 gives the induction argument for the claim made at 79.
- The code uses unicode `ψ`, `α`, `β` (237, 249, 807, 1059) so the simulation reads like the mathematics (0 qe-code-002 violations).

## Recommended actions

1. Brace the 21 blackboard operators - `\mathbb P` to `\mathbb{P}`, `\mathbb E` to `\mathbb{E}` (99, 100, 110, 368, 369, 370, 437, 903, 911, 937, ...) - the single largest fix in this lecture (qe-math-010 (proposed)).
2. Sentence-case the 11 Title Case headings at 223, 295, 319, 419, 440, 466, 742, 790, 893, 965 and 984 (qe-writing-006), and fix the mid-sentence capitals at 472, 494 and 495 ('Law of Large Numbers') (qe-writing-004).
3. Replace the six static PNGs at 200, 538, 572, 607, 635 and 1115 with code-generated graphs (qe-fig-002) - they are the lecture's only figures that cannot be reproduced or edited - and give all eight figures a `:name:` so they can be cross-referenced (qe-fig-005).
4. Convert the six `\left(\begin{array}{...}...\right)` displays at 156, 179, 457, 548, 923 and 1016 to `bmatrix` (qe-math-003).
5. Turn the two bold '**Theorem.**' paragraphs at 687 and 708 into `{prf:theorem}` directives with labels, so the convergence theorem the text refers back to at 795 is a real target rather than an anchor placed above it.
6. Fix the defective sentences and notation: 79, 697 and 760 as quoted above; the missing set braces at 221 ($S = 0,\ldots,n-1$) and 1315 (`${u_t}$`, which renders without braces); the mismatched delimiters at 992-996 (`[ ... \Bigr]`); and the typos 'cummulative' (238), 'distibution' (491) and 'Horizonal' (1070).
7. Replace the two `%time` calls at 312 and 316 with `quantecon.Timer` (qe-code-004), make the raw python-programming.quantecon.org link at 309 a `` {doc} `` reference (qe-link-002), drop `figsize=` at 809 and 1067 and add `lw=2` at 1079 and 1081 (qe-fig-001, qe-fig-008), sweep the 35 double-space runs (71, 174, 225, 227, 229, 340, 374, 376, 447, 472, ...), split the two-sentence paragraphs at 227 and 1377, and change `reverse=1` to `reverse=True` at 1296.
