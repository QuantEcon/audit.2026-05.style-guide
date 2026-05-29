# Style Audit — workspace

- **Series:** lecture-python-programming
- **File:** `lectures/workspace.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Most headings already sentence case. |
| Math         | N/A   | No math content. |
| Code         | 7/10  | Two `plt.title('Sine Wave')` / `plt.title(title)` in demo scripts (lines 69, 96) — these are demo `sine_wave.py` files but rendered in code cells; minor PEP8 in `def plot_wave(title : str = 'Sine Wave')` (space before `:` is non-PEP8); no non-Anaconda packages. |
| JAX          | out of scope | — |
| Figures      | 4/10  | Two `plt.title(...)` calls embed titles in the demo sine_wave.py code (lines 69, 96) — qe-fig-003 violations even though pedagogical. Many static `{figure}` directives (lines 141, 149, 164, 169, 185, 199, 221, 227, 232, 237, 248, 254, 267, 290, 296, 309) for IDE screenshots — none with `name:` metadata. |
| References   | N/A   | No citations. |
| Links        | 9/10  | External docs and tool links only; no improper cross-series URLs. |
| Admonitions  | 9/10  | Three `{note}` and one `{figure}` per section — clean usage; no exercises. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — `plt.title('Sine Wave')` (line 69) and `plt.title(title)` (line 96) embed titles in matplotlib figures, outside any exercise/solution. *Context:* part of a `sine_wave.py` demo script being written via `%%writefile`. *Count:* 2 occurrences.

### Medium severity
- **[qe-fig-005]** — All ~16 `{figure}` directives for IDE screenshots lack `name:` metadata.

### Low severity
- **[qe-writing-001]** *(carry-forward W1)* — A few multi-sentence paragraphs (e.g., lines 31–33 span two ideas).
- **[qe-writing-006]** *(carry-forward W3)* — One H2 heading edge-case: line 319 `## Git your hands dirty` — sentence case but a pun; harmless.
- **[qe-code-001]** — `def plot_wave(title : str = 'Sine Wave')` on line 89: PEP8 disallows the space before `:` in annotations; should be `title: str`.

## Strengths
- Lecture title "Writing Longer Programs" follows qe-writing-006.
- All major H2 sections use sentence case ("Overview", "Working with Python files", "Development environments", "A step forward from Jupyter Notebooks: JupyterLab", "A walk through Visual Studio Code", "Git your hands dirty").
- H3 sections also follow sentence case ("Using magic commands", "Using the terminal", "Using the run button").
- Good use of `{figure}`, `{note}` admonitions.
- Uses `:caption: sine_wave.py` and `:lineno-start: 1` cell options idiomatically.

## Recommended actions
1. Replace `plt.title('Sine Wave')` / `plt.title(title)` in the demo with figure-directive captions, or annotate as deliberately demonstrating a deprecated pattern.
2. Add `name:` metadata (e.g., `fig-jupyter-lab-cmd`, `fig-vs-code-home`) to each `{figure}` directive.
3. Fix `title : str` → `title: str` per PEP8.
4. Optional: tighten the few multi-sentence paragraphs.
