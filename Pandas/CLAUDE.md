# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A learning module for the **Pandas** library, part of an IBM-certified "Data Analysis with Python" training. It sits alongside sibling study folders under `Data_analyse/` (`NumPy/`, `lab_data_importation/`, `premieres_analyses_avec_pandas/`) and follows the same conventions. This folder is currently empty — new work should match the patterns below.

Each folder is a **standalone collection of single-topic scripts**, not an installable package. There is no `src/` layout, no `pyproject.toml`, no test suite. A script demonstrates one concept (importing, cleaning, indexing, grouping…) and is run directly.

## Environment & commands

Windows + PowerShell. Python 3.12 and 3.14 are both installed (`py --version`, `python --version`). Each folder gets its own virtual environment — the siblings use either `venv/` or `.venv/`; either name is fine but be consistent within the folder.

```powershell
# One-time setup for this folder
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt   # dépendances du projet : pandas, numpy
# or
python -m pip install pandas numpy

# Run a script (venv activated)
python <script>.py
```

There is no build, lint, or test tooling configured. "Running" a script means executing it and reading its `print()` output.

After creating a venv, mirror the sibling `.vscode/settings.json` so the editor picks up the interpreter:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
  "python.analysis.extraPaths": ["${workspaceFolder}\\.venv\\Lib\\site-packages"]
}
```

Add a `.gitignore` that excludes `.venv/`, `venv/`, `__pycache__/`, `*.py[cod]`, and any CSV files the scripts download (downloaded datasets are artifacts, not source).

## Script conventions (follow the existing style)

Two script shapes exist in the sibling folders; pick the one that fits:

1. **Exploration scripts** (e.g. `NumPy/discover.py`): top-level code, heavy on `print()` with aligned labels, French inline comments explaining what each line demonstrates. No functions needed.

2. **Import/clean pipeline scripts** (e.g. `lab_data_importation/import_auto.py`): small single-purpose functions (`download_dataset`, `clean_dataset`, `summarize_dataset`, an orchestrating `import_data`/`import_*`) guarded by `if __name__ == "__main__":`. English docstrings.

Shared conventions across both:
- `import numpy as np`, `import pandas as pd`.
- Module-level constants in `UPPER_SNAKE_CASE` (dataset URLs, column-header lists, default file names).
- Datasets come from IBM Skills Network / archive URLs, loaded with `pd.read_csv(...)`, and written back with `df.to_csv(path, index=False)` (drop the pandas index).
- Missing-value markers (`"?"`) are replaced with `np.nan`; rows are cleaned with `dropna`, types coerced with `pd.to_numeric(..., errors="coerce")`.
- **Prose (comments, print output, README narration) is in French; code identifiers and docstrings are in English.** This is a French-speaking learner's project — preserve that split.
- Download failures raise `SystemExit` with a clear message rather than crashing with a traceback.
