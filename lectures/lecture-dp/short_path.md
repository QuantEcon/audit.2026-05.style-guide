# short_path

- **Series:** lecture-dp
- **File:** `lectures/short_path.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-002` ×4; `qe-writing-003` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×4; `qe-fig-002` ×4. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 221, 231, 404, 436. *Example:* four PEP8-level defects in a lecture reported clean on all five mechanical code rules. (1) `J = np.zeros_like(nodes, dtype=int)` and `next_J = np.empty_like(nodes, dtype=int)` (221-222) build integer arrays from `range(7)` via `*_like`, where `np.zeros(7, dtype=int)` is the direct spelling; the integer dtype also silently truncates any non-integer cost, which is precisely the change the exercise then makes (266-269 warns the reader that costs become floats), and the two comments on those lines are aligned at two different columns. (2) Trailing whitespace on three lines of that same cell - 231 and 234 are whitespace-only, and 232 carries sixteen trailing spaces after the colon (W291/W293). (3) `Q[destination_node, destination_node] = 0` at 404 sits inside the per-line loop, so it is re-executed once per input row; it belongs beside the `np.full` at 391. (4) `return(J)` at 436 reads as a call rather than a return statement; every other function in the file writes `return X`. Also `map_graph_to_distance_matrix` reads `num_nodes` and `destination_node` from module scope (385-386) while `compute_cost_to_go` derives `num_nodes` from its argument at 423, shadowing the global with the same value - two conventions in adjacent functions.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 4. *Lines:* 57, 78, 84, 96. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 57, 78, 84, 96. *Example:* {figure} without :name:.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 34, 72, 210, 272. *Example:* (1) 101 of this lecture's 474 lines - 21% of the file - are the exercise's graph data pasted into the body as a `%%file graph.txt` cell (272-372). The lecture already keeps assets in `_static/lecture_specific/short_path/` (it loads four PNGs from there at 57, 78, 84 and 96), so the data has a home; as it stands the reader scrolls a hundred lines of `node57, node86 701.09, ...` between the exercise statement and its solution. (2) Two bulleted lists end with the non-item 'etc., etc.' (34, 72), one of them in a list whose previous item is already 'Telecommunication network design and routing'. (3) 'the principle diagonal' at 210 should be 'principal' - and the sentence is about `Q`'s diagonal, which the code at 201-207 sets to `inf` off-destination and 0 at the destination, so the word matters to a reader checking the array.

### Low severity
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 122. *Example:* the one idea the lecture exists to teach is the only step it does not argue. Line 41 states the purpose - 'the shortest path problem also provides a nice introduction to the logic of **dynamic programming**' - and the Bellman equation `` {eq}`spbell` `` then arrives at 122-129 on the strength of 'Some thought will convince you that, for every node $v$, the function $J$ satisfies'. Two sentences would supply it: moving to $w$ first costs $c(v,w)$ and then $J(w)$ at best, so the best route from $v$ is the best over $w \in F_v$ of that sum - which is also exactly the reading of `` {eq}`spprebell` `` given twelve lines earlier at 104-116, so the material is already on the page in the wrong order. The contrast with 164-167 makes the gap sharper: there the lecture is explicit that it omits the convergence proof and says where it is proved, whereas here the omission is not flagged at all.


## Strengths

- The abstract argument is carried by four pictures of one concrete graph, each doing a different job: the problem (57), the two optimal paths drawn separately so the reader can see the tie at cost 8 (78, 84), and the cost-to-go function labelled on every node (96) - which is what makes 'Note that $J(G) = 0$' (100) and the check at 241 ('This matches with the numbers we obtained by inspection above') land without further explanation.
- The two equations are introduced in the right order and kept distinct: `` {eq}`spprebell` `` (107-111) as the rule for choosing the next step *given* $J$, then `` {eq}`spbell` `` (125-129) as the restriction $J$ itself must satisfy, with 118-120 marking the transition ('Hence, if we know the function $J$, then finding the best path is almost trivial. But how can we find the cost-to-go function $J$?').
- The move from mathematics to code is made explicit rather than assumed: the cost function becomes the matrix $Q$ with a displayed definition of its entries (177-184), the node relabelling is stated ('We're also numbering the nodes now, with $A = 0$', 188) and illustrated with $Q(1,2)$ (190-194), and the two diagonal conventions are justified in the reader's terms ('moving on is required' / 'here is where we stop', 212-213).
- The exercise is a genuine scaling test of the same algorithm - 100 nodes rather than 7 - and its note (266-269) warns about the one thing that actually breaks when costs stop being integers, pointing at `np.allclose()`; the solution then explains why it took that advice (439-440).
- The solution is decomposed exactly as it is announced at 408-411 - a reader, a Bellman operator, a cost-to-go iterator, a path printer - and the vectorized `bellman(J, Q) = np.min(Q + J, axis=1)` (418-419) is a one-line statement of `` {eq}`spbell` `` for all nodes at once, with 415 saying so.
- The final cell (468-472) checks the answer against an independent quantity - the printed path cost against $J[0]$ - rather than stopping at the printout.

## Recommended actions

1. Move the 101-line `graph.txt` block (272-372) into `_static/lecture_specific/short_path/`, where this lecture's other assets already live, and load it in the solution; the exercise statement at 252-269 then sits next to its solution.
2. Give the Bellman equation at 122-129 the two-sentence derivation the lecture's own `` {eq}`spprebell` `` discussion already contains, instead of 'Some thought will convince you'.
3. Fix the four code items: `np.zeros(7, dtype=int)` / `np.empty(7, dtype=int)` at 221-222 (and consider `float`, since the exercise's costs are floats), strip the trailing whitespace at 231, 232 and 234, hoist `Q[destination_node, destination_node] = 0` out of the loop at 404, and write `return J` at 436.
4. Decide one parameter convention for the solution's functions: `map_graph_to_distance_matrix` takes `num_nodes`/`destination_node` from globals (385-386) while `compute_cost_to_go` reads its own from `Q.shape` (423).
5. Replace 'etc., etc.' at 34 and 72 with a real item or nothing, and correct 'principle diagonal' to 'principal diagonal' at 210.
6. Mechanical items from the draft: the four `{figure}` directives (57, 78, 84, 96) carry neither `:name:` nor a caption (qe-fig-005 x4) and are static PNGs rather than code-generated figures (qe-fig-002 x4). Two of the four - the annotated optimal paths at 78 and 84, and the cost-to-go labels at 96 - would be a networkx drawing built from the `Q` the lecture already defines at 201-207, which would also let the exercise's 100-node graph be drawn.
7. Also worth fixing while there: the two `{figure}` directives at 78 and 84 are placed between the items of one bulleted list (76-86), which ends the list and starts a new one at each directive; and `np.allclose()` is written as bare prose at 439 where 268 writes it as inline code.
8. This file is byte-identical to `lecture-python-intro/lectures/short_path.md`, so fix it once upstream and re-sync - the findings are counted twice in the corpus totals until then.
