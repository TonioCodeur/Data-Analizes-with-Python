# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

A collection of standalone Python learning scripts exploring **NumPy** fundamentals and image processing. Each script is self-contained and illustrates one specific concept. There is no shared module, entry point, or build system.

## Environment setup

```powershell
# Activate the included virtual environment (Windows PowerShell)
venv\Scripts\Activate.ps1

# Or install dependencies fresh
pip install -r requirements.txt
```

Dependencies: `numpy==2.5.0`, `matplotlib==3.11.0`, `scikit-learn==1.9.0`

## Running scripts

```bash
python discover.py
python concatenate.py
python math_opertors.py   # note: intentional typo in filename
python reshape.py
python iteration.py        # opens a matplotlib image window
python iteration_clean.py  # opens a matplotlib image window
```

Scripts that call `plt.imshow` open a blocking GUI window — close it to exit.

## Script map

| File | Concept |
|------|---------|
| `discover.py` | Array creation, attributes (`dtype`, `ndim`, `shape`), vectorization, ufuncs |
| `concatenate.py` | `np.concatenate` with `axis=0` (vertical) and `axis=1` (horizontal) |
| `math_opertors.py` | Scalar/element-wise ops, dot product and matrix multiply via `@` |
| `reshape.py` | `.reshape()` (element count must be preserved), boolean masks |
| `iteration.py` | Grayscale conversion via nested Python loops — the slow, pedagogical approach |
| `iteration_clean.py` | Same conversion vectorized with `np.mean(axis=2)` — the fast NumPy way |

## Key contrast

`iteration.py` vs `iteration_clean.py` is the pedagogical core of the project: Python loops pixel-by-pixel (slow) vs `np.mean(flower, axis=2)` on the whole 3D array at once (fast). The image `flower.jpg` is loaded from scikit-learn's sample data (`sklearn.datasets.load_sample_image`).

## Architecture note

The user has described an intent to build a SaaS half-life measurement app (molecules/drugs in blood) with a strict 3-layer architecture: **display → service → persistence**, where each layer may only communicate with its immediate neighbor. That codebase does not yet exist in this directory — this repo is currently a NumPy learning sandbox.
