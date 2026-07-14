# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`Data_analyse/` is a **learning sandbox** for an IBM-certified "Data Analysis with Python" training (NumPy, Pandas, then RAG/agentic AI and machine learning). It is **not** an installable package: no `src/` layout, no `pyproject.toml`, no test suite, no build/lint tooling. Each top-level folder is a standalone collection of single-topic scripts run directly with `python <script>.py`, where "running" means executing and reading the `print()` output.

Sub-folders each carry their own `README.md` and `CLAUDE.md` — read the folder's own docs before working inside it. `NumPy/` and `Pandas/` are the most developed.

| Folder | Topic |
|--------|-------|
| `NumPy/` | NumPy fundamentals + image processing (loops vs vectorization) |
| `Pandas/` | DataFrame indexing/selection (`dataframe.py`) |
| `lab_data_importation/` | IBM lab: download + clean CSV datasets (`import_auto.py`, `import_laptop_prices.py`) |
| `premieres_analyses_avec_pandas/` | First pandas import experiments (`import_data.py`) |
| `perf.py` | Root benchmark: pure-Python `for` sum vs `np.sum` via `timeit` |

## Environment

Windows + PowerShell. Python **3.14** (`.venv` was created with pythoncore-3.14). Both 3.12 and 3.14 are installed on the machine — check with `py --version` / `python --version`.

There is a **root `.venv/`** (created but empty of project deps) and some sub-folders also have their own venv (`premieres_analyses_avec_pandas/.venv/`, `NumPy/venv/`). The simplest path is a single root venv installed from the root `requirements.txt`, which covers every folder.

### One-time install (root venv, recommended)

```powershell
# From the repo root: D:\Disque dur\Sandbox\Data_Sciences\Data_analyse
python -m venv .venv                       # skip — .venv already exists
.\.venv\Scripts\Activate.ps1               # activate it
python -m pip install --upgrade pip
python -m pip install -r requirements.txt  # numpy, pandas, matplotlib, scikit-learn
```

On macOS / Linux: `source .venv/bin/activate` instead of the `Activate.ps1` line.

If PowerShell blocks activation with an execution-policy error, run once:
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

### Running scripts

```powershell
python perf.py
python NumPy\discover.py
python Pandas\dataframe.py
python lab_data_importation\import_auto.py   # prompts via input() then downloads
```

Scripts calling `plt.imshow` (`NumPy/iteration*.py`) open a **blocking GUI window** — close it to exit. Scripts in `lab_data_importation/` are **interactive**: they `input()` a filename, download from an IBM Skills Network URL, then write a cleaned CSV.

Sub-folders keep their own `requirements.txt` too (e.g. `NumPy/requirements.txt` pins exact versions). The root `requirements.txt` is the superset for the whole project; a per-folder file wins if you only want that folder's deps.

## Conventions (match the existing style)

- **Prose is French, code is English.** Comments, `print()` labels and README narration are written in French; identifiers and docstrings in English. Preserve this split — it is a French-speaking learner's project.
- `import numpy as np`, `import pandas as pd`. Module-level constants in `UPPER_SNAKE_CASE` (dataset URLs, column-header lists, default filenames).
- Two script shapes exist, pick the fitting one:
  1. **Exploration** (e.g. `NumPy/discover.py`, `Pandas/dataframe.py`): top-level code, heavy `print()` with aligned labels, French inline comments. No functions needed.
  2. **Import/clean pipeline** (e.g. `lab_data_importation/import_auto.py`): small single-purpose functions (`download_dataset`, `clean_dataset`, `summarize_dataset`, an orchestrating `import_data`) guarded by `if __name__ == "__main__":`.
- Datasets come from IBM Skills Network / archive URLs, read with `pd.read_csv(...)`, written back with `df.to_csv(path, index=False)` (drop the pandas index). Missing markers (`"?"`) → `np.nan`; clean with `dropna`, coerce with `pd.to_numeric(..., errors="coerce")`.
- Download failures should `raise SystemExit("clear message")` rather than crash with a traceback.
- `.gitignore` excludes venvs, `__pycache__/`, `*.py[cod]`, and downloaded CSVs (datasets are artifacts, not source).
