from pathlib import Path

import pandas as pd

URL = "https://archive.ics.edu/dataset/10/automobile"
OUTPUT_PATH = Path("data/automobile.csv")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

try:
    df = pd.read_csv(URL, header=None, na_values="?")
    print(f"Dataset downloaded successfully from {URL}")
except Exception as error:
    raise SystemExit(f"Failed to download dataset from {URL}: {error}") from error

# Save without the pandas index column.
df.to_csv(OUTPUT_PATH, index=False)
print(f"Dataset saved to {OUTPUT_PATH}")