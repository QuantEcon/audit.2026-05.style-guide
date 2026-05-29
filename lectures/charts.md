---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Charts

Visual summary of the May 2026 audit across 5 lecture series and 7 in-scope rule categories. All figures are generated at build time from the audit data below.

```{code-cell} ipython3
:tags: [hide-input]

import matplotlib.pyplot as plt
import numpy as np

# --- Audit data (May 2026) ---------------------------------------------
series       = ['intro', 'programming', 'python.myst', 'advanced', 'dp']
categories   = ['Writing', 'Math', 'Code', 'Figures', 'References', 'Links', 'Admonitions']

# Per-series, per-category average scores (np.nan = category not applicable)
scores = np.array([
    [8.0, 7.8, 8.1, 6.4, 7.0, 7.9,  9.0],   # intro
    [7.2, 7.3, 8.5, 6.5, np.nan, 9.1, 8.7], # programming (no citations -> References N/A)
    [8.0, 9.0, 9.2, 8.7, 9.0, 9.7, 10.0],   # python.myst
    [8.2, 5.6, 7.0, 6.5, 7.9, 7.5,  7.8],   # advanced
    [7.5, 6.7, 7.3, 6.9, 7.8, 7.7,  8.7],   # dp
])

# Priority distribution per series: HIGH, MEDIUM, LOW, NONE
priority = {
    'intro':        [1, 9, 36, 5],
    'programming':  [3, 0, 19, 4],
    'python.myst':  [2, 0, 13, 95],
    'advanced':     [6, 27, 25, 4],
    'dp':           [17, 5, 21, 7],
}

# Top systemic issues (rule -> lectures affected across the corpus)
systemic_rules  = ['qe-writing-006', 'qe-code-002', 'qe-fig-001', 'qe-fig-005',
                   'qe-fig-003', 'qe-math-010*', 'qe-link-002', 'qe-fig-006',
                   'qe-math-002', 'qe-ref-001', 'qe-math-011*', 'qe-writing-009*',
                   'qe-fig-007']
systemic_counts = [170, 150, 125, 120, 90, 60, 60, 50, 46, 37, 30, 30, 30]
```

## Score heatmap — series × category

Darker red marks weaker categories. The two clear weak spots are **Math in `lecture-python-advanced.myst`** (5.6) and **Figures across every series** (6.4–6.9 except `python.myst`).

```{code-cell} ipython3
:tags: [hide-input]

fig, ax = plt.subplots(figsize=(9, 4))
masked = np.ma.masked_invalid(scores)
cmap = plt.cm.RdYlGn
cmap.set_bad(color='lightgray')
im = ax.imshow(masked, cmap=cmap, vmin=4, vmax=10, aspect='auto')

ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories, rotation=30, ha='right')
ax.set_yticks(range(len(series)))
ax.set_yticklabels(series)

for i in range(len(series)):
    for j in range(len(categories)):
        val = scores[i, j]
        txt = 'N/A' if np.isnan(val) else f'{val:.1f}'
        ax.text(j, i, txt, ha='center', va='center', fontsize=9)

ax.set_title('Average score by series and category (0–10)')
fig.colorbar(im, ax=ax, shrink=0.8, label='score')
plt.tight_layout()
plt.show()
```

## Top systemic issues — lectures affected

Across all 299 lectures, these rules are violated most often. Figures and Code now sit alongside the long-standing heading-case issue. Rules marked `*` are proposed additions to the rule registry (not yet coded).

```{code-cell} ipython3
:tags: [hide-input]

order = np.argsort(systemic_counts)
fig, ax = plt.subplots(figsize=(9, 5))
ax.barh([systemic_rules[i] for i in order],
        [systemic_counts[i] for i in order],
        color='steelblue')
ax.set_xlabel('lectures affected (of 299)')
ax.set_title('Most frequently violated rules')
for i, idx in enumerate(order):
    ax.text(systemic_counts[idx] + 2, i, str(systemic_counts[idx]),
            va='center', fontsize=8)
plt.tight_layout()
plt.show()
```

## Priority distribution by series

`lecture-python.myst` is overwhelmingly NONE/LOW; `lecture-dp` and `lecture-python-advanced.myst` carry most of the HIGH-priority work.

```{code-cell} ipython3
:tags: [hide-input]

labels = ['HIGH', 'MEDIUM', 'LOW', 'NONE']
colors = ['#d73027', '#fc8d59', '#fee090', '#91cf60']
names = list(priority.keys())
data = np.array([priority[s] for s in names])

fig, ax = plt.subplots(figsize=(9, 4))
left = np.zeros(len(names))
for k in range(4):
    ax.barh(names, data[:, k], left=left, color=colors[k], label=labels[k])
    left += data[:, k]
ax.set_xlabel('number of lectures')
ax.set_title('Priority distribution by series')
ax.legend(ncol=4, loc='lower right', fontsize=8)
plt.tight_layout()
plt.show()
```

## Corpus-weighted category averages

Where the corpus is strongest (Admonitions, Links) and weakest (Figures, Math).

```{code-cell} ipython3
:tags: [hide-input]

weights = np.array([51, 26, 110, 62, 50], dtype=float)
cat_avgs = []
for j in range(len(categories)):
    col = scores[:, j]
    mask = ~np.isnan(col)
    cat_avgs.append(np.average(col[mask], weights=weights[mask]))

fig, ax = plt.subplots(figsize=(9, 4))
bars = ax.bar(categories, cat_avgs, color='slateblue')
ax.set_ylim(0, 10)
ax.set_ylabel('weighted average score')
ax.set_title('Corpus-weighted average by category')
ax.axhline(8.6, color='green', ls='--', lw=1, label='NONE threshold (8.6)')
ax.axhline(5.0, color='red', ls='--', lw=1, label='HIGH threshold (5.0)')
for b, v in zip(bars, cat_avgs):
    ax.text(b.get_x() + b.get_width()/2, v + 0.1, f'{v:.1f}',
            ha='center', fontsize=8)
ax.legend(fontsize=8)
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.show()
```

```{note}
These figures are generated from inline data for the 2026-05 audit. When this becomes a recurring monthly pass (see the project roadmap), the data should move to a versioned `data/scores.csv` so trends can be charted across audit dates.
```
