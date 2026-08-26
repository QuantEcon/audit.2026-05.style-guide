# networks

- **Series:** lecture-python-intro
- **File:** `lectures/networks.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×2; `qe-writing-003` ×3; `qe-writing-002` ×3, +3 more. |
| Math         | 6/10  | `qe-math-004` ×3; `qe-math-003` ×3; `qe-math-009` ×4. |
| Code         | 6.5/10 | `qe-code-001` ×14; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×5; `qe-fig-004` ×3; `qe-fig-002` ×5, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 14. *Lines:* 110, 115, 368, 372, 410, 591, 593, 646, 808, 834, …. *Example:* PEP8 spacing is violated systematically, and the violations cluster in the hand-written networkx cells rather than the imported-helper ones. Missing space after a comma in an argument list: `normalise_weights(node_total_exports,10000)` and `normalise_weights(edge_weights,10)` (109-110), `colorise_weights(list(centrality.values()),color_palette=cm.viridis)` (112), `dict(zip(DG.nodes,node_colors))` (113, 426), `for src,_ in DG.edges` (115, 428), `normalise_weights(node_total_exports,3000)` (421-422), `node_color='none',node_size=500` (808), `print(i+1,e[i])` (967), `def is_accessible(G,i,j)` (1300), and the whole edge list at 1236-1243. Spaces around a keyword-argument `=`, which PEP8 forbids: `with_labels = True` (368, 383), `node_color = 'none',node_size = 500` (591, 594, 646, 649), `linewidths= 0.5, edgecolors = 'black'` (593, 648) - and the identical call at 806-808 gets it right, so the file disagrees with itself. Missing space before `=` in `Z_visual= ch1_data[...]` (410). Missing space after the dict colon in `'centrality':centrality_measures` (834). Inline comments with no space after the hash: `#checking if above graph is strongly connected` (372, 387), `#find adjacency matrix associated with G` (1251). No spaces around a comparison: `if result[i,j]>0` (1306).
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 5. *Lines:* 171, 238, 248, 507, 714. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 312, 575, 631, 840, 1229. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 85, 160. *Example:* H3 Title Case: 'Example: Aircraft Exports' (Exports).

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 16. *Example:* non-Anaconda import with no install cell: ['quantecon_book_networks'].
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 118, 431. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 3. *Lines:* 89, 401, 786. *Example:* Title Case caption (Aircraft, Network).
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 3. *Lines:* 549, 605, 618. *Example:* pmatrix environment.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 3. *Lines:* 1034, 1037, 1049. *Example:* \mathbf.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 4. *Lines:* 545, 904, 916, 1026. *Example:* 545 writes the three-element state set as `$\{$poor, middle, rich$\}$` - three separate maths spans and two of them containing nothing but a brace - where `$\{\text{poor}, \text{middle}, \text{rich}\}$` is one span and one idea; 903-907 and 915-919 each wrap a single unaligned line in `\begin{aligned} ... \end{aligned}` inside `$$`, an environment that buys nothing when there is no `&` to align on (contrast 1091-1093 and 1102-1104, which write the same kind of one-line display bare and read better for it); and the lecture uses two different index bases for the same node set - 896-897 and 917 say the nodes are `$1, \ldots, n$` and sum `$\sum_{1 \leq j \leq n}$`, while the Katz definition twenty lines later indexes `$i \in \{0, \ldots, n-1\}$` and sums `$\sum_{j=0}^{n-1}$` (1025-1026), so a reader comparing `` {eq}`eq_eicen` `` with `` {eq}`katz_central` `` has to re-base the subscripts to see that they are the same recursion.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 695, 1146, 1151. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 189, 855, 1039. *Example:* 187-197 is four sentences of throat-clearing before the section reaches its first definition, and 189 - "This theory will allow us to better organize our thoughts" - carries no information a reader can act on. 855-861 restates 481-489 almost verbatim: 481-486 already said that an edge exists for almost every pair in the credit network and that "the existence of an edge from one node to another is not particularly informative", and 858-859 says it again, followed by "This can be seen in the above graph as well" (861), which names neither figure and cannot use `` {numref} `` because the bar chart at 840 has no name. And the recursive-importance idea is stated five separate times - 878-889 (four sentences), 922-924, 1005, 1009 and 1039-1041 - by the fifth pass it is padding even for an introductory audience.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 1009, 1142, 1219. *Example:* 1142 is a truncated sentence: "We apply the ideas discussed in this lecture to:" ends on a colon and is followed not by a list but by a paragraph about textbooks, so the promised forward reference is simply missing from the Further reading section. 1009 contradicts the argument the lecture just spent twenty-five lines building: 863-889 shows that degree centrality is exactly the wrong measure for ranking web pages (page A has twice the inbound links and is still less important), and then 1009 says PageRank's "main principle is that links from important nodes (as measured by degree centrality) are worth more" - the parenthetical should say eigenvector centrality. And exercise 2 asks for three measures - "in-degree centrality, out-degree centrality and eigenvector centrality" (1219-1220) - while the solution computes out-degree (1256-1261) under the comment `# computing in-degree centrality`, and eigenvector (1263-1268); in-degree is never computed and the one thing that is computed is mislabelled.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 87. *Example:* mid-sentence 'Data'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 241, 847, 1012. *Example:* 847-848 fakes a y-axis label with an invisible legend entry - `mpatches.Patch(color=None, label='in degree', visible=False)` followed by `ax.legend(handles=[patch], handlelength=0, frameon=False)` - where `ax.set_ylabel('in degree')` is the one-line version; worse, the pattern is copied to 992-993 and 1128-1129 with the `label` argument dropped, so those two charts draw an empty invisible legend and end up with no axis label at all, which is why the three centrality bar charts cannot be read against one another. Katz centrality (1012-1057) is the only one of the four centrality measures the lecture defines that is never computed or plotted, even though the credit-network matrix `Z` and the `eigenvector_centrality` helper (943-953) are both already in scope and `` {eq}`katz_central_vec` `` reduces to one `np.linalg.solve`. And three of the five static figures carry no usable label: 241 and 251 give two *different* three-node graphs the identical caption "Poverty Trap", so `` {numref}`poverty_trap_1` `` and `` {numref}`poverty_trap_2` `` render indistinguishably in the reader's figure list, and the `{image}` at 714-717 that illustrates {prf:theorem}`graph_theory_property2` has an empty body where its caption should be.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 262, 660, 931. *Example:* 2 spaces.

### Low severity
_None found._


## Strengths

- Bold marks definitions and nothing else, across nineteen terms, each bolded exactly once at the point it is introduced: nodes/vertices and edges/links (147, 149), directed graph (215), vertices/nodes (220), edges (222), direct predecessor/successor (259-260), in-degree/out-degree (264-265), accessible (337), communicate (351), strongly connected (353), weighted directed graph and weight function (498-499), adjacency matrix (527), centrality measure (770), eigenvector centrality (901), Katz centrality (1020), hub and authority centrality (1065, 1068), authority-based eigenvector centrality (1088) - and italic is reserved for genuine emphasis (*recursive* 878, *it links to* 887, *rates of flow* 924, *suppliers* 935), so no term appears in both forms.
- Every `` {numref} `` target is a target that is actually used, and used to carry the argument forward rather than to decorate: `aircraft_network` (94) is cited at 229 to instantiate the abstract $V$ and $E$ on real data; `poverty_trap_1`/`poverty_trap_2` (239, 249) at 274, 320 and 355-356 to reconstruct the second graph in networkx and then to contrast strong connectedness; `financial_network` (406) at 822, 858, 973 and 1109 so the same network is re-ranked by three different measures; `sample_gph_1` (791) at 956.
- The two theorems are stated as labelled `{prf:theorem}` blocks (673-684, 697-705) rather than as bold prose, and the equivalence the second one asserts is then checked numerically both ways in the same section - `is_irreducible(A)` at 751 against `nx.is_strongly_connected(G6)` at 755 on the same graph - so the reader sees the theorem verified rather than asserted.
- The transpose-reverses-the-arrows point (567-568) is made three ways in sixty lines: the claim in prose, both matrices written out element by element (603-625), and both networks drawn with matching edge labels (575-597, 631-652), which is the right amount of redundancy for a first course.
- The critique of degree centrality is built as a concrete counterexample before any new notation appears - page A has twice the inbound links as page B, the links to A come from pages with no traffic (866-876) - so by the time `` {eq}`ev_central` `` arrives at 903 the reader already knows what problem it solves.
- Every displayed equation the lecture later refers to is labelled and the label is used: `ev_central` (907) at 912, `katz_central_vec` (1035) at 1046, and `eq_eicen`, `eicena0`, `eicena` (919, 1093, 1104) as the element-by-element companions of the vector forms.

## Recommended actions

1. Fix the `is_accessible` bug at 1300-1309: `for i in range(n)` (1304) shadows the function's own argument `i`, so by the time `result[i,j]` is read at 1306 `i` is always `n-1` and both answers - `is_accessible(G, 2, 1)` at 1328 and `is_accessible(G, 3, 6)` at 1332 - are computed for node 7, not for the nodes asked about. Rename the loop variable to `k` and collapse the tail to `return result[i, j] > 0`.
2. The one mechanical Code finding in the drafted report is a false positive - do not 'fix' it. `qe-code-003` at line 16 reports `quantecon_book_networks` as a non-Anaconda import with no install cell, but line 20 installs it: `!pip install quantecon-book-networks==1.6`. The checker compares the import name to the distribution name without normalising `_` against `-` (see scanner_doubts). Code has no mechanical violations in this file.
3. Complete the truncated sentence at 1142 - "We apply the ideas discussed in this lecture to:" has lost whatever list or forward reference it was introducing - and correct "as measured by degree centrality" at 1009 to eigenvector centrality, which is what the preceding twenty-five lines argue for.
4. Finish the exercise 2 solution: add the in-degree computation asked for at 1219, and fix the `# computing in-degree centrality` comment at 1257, which sits above `G.out_degree`.
5. Give the two poverty-trap figures distinguishable captions (241, 251), add a caption to the empty `{image}` body at 714-717, and strip the literal `\n` from the two mystnb captions at 93 and 405 (`caption: "Commercial Aircraft Network \n"`), which renders as a stray backslash-n in the figure label.
6. Replace the invisible-legend-patch idiom with `ax.set_ylabel(...)` at 847-848, 992-993 and 1128-1129 - the last two pass no `label` at all, so they render an empty legend and no axis label - and drop the `ax.set_ylim((0, 20))` at 850, which is applied to the in-degree chart only and so makes it non-comparable with the two eigenvector charts.
7. Compute and plot Katz centrality for the credit network (1012-1057 defines it and never uses it); `` {eq}`katz_central_vec` `` is one `np.linalg.solve(np.eye(n) - beta * Z, np.ones(n))` away from a fourth bar chart on the same axes as the other three.
8. Rewrap 29-30 so the comma is not orphaned onto its own line after the link - `[world wide web](...)` then `, where web pages are connected` renders with a space before the comma - and turn the bare URL at 47 into a markdown link with text.
9. Sweep the mechanical items: the two Title Case H3s (85, 160), `\mathbf 1` at 1034, 1037 and 1049 (qe-math-004), the three `pmatrix` displays at 549, 605 and 618 recast as `bmatrix` (qe-math-003), the three narrative `{cite}` calls that want `{cite:t}` (695, 1146, 1151), the double spaces at 262, 660 and 931, and the fourteen PEP8 sites above. Add mystnb figure metadata to the seven un-named figure cells - 312, 360, 375, 575, 631, 840, 1229 - noting that 360 and 375 are figures the scanner currently cannot see (see scanner_doubts).
