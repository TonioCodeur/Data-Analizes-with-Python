# Data import with Python using Pandas and NumPy

## Context
I am currently learning data science with Python through an IBM certified training program:
- Data analysis with Python and the Pandas and NumPy libraries
- RAG and agentic AI
- Machine learning

I completed a lab using IBM datasets, and I decided to create a Python script to download and clean the data.

## Goals
- Download the IBM dataset
- Clean the IBM dataset
- Display dataset statistics and data types

## Lab workflow

### Data download
I used the `import_auto.py` script to download the IBM dataset.

```python
import urllib.request

DATASET_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
)
DEFAULT_FILE_NAME = "auto"

def prompt_for_file_name():
    """Ask the user for an output file name, falling back to the default."""
    answer = input(f"Enter the file name to download (default: {DEFAULT_FILE_NAME}.csv): ")
    base_name = answer.strip() or DEFAULT_FILE_NAME
    return f"{base_name}.csv"

def download_dataset(url, file_name):
    """Download the dataset at ``url`` into ``file_name``."""
    urllib.request.urlretrieve(url, file_name)

def import_data():
    """Download, clean and summarize the automobile dataset."""
    file_name = prompt_for_file_name()
    download_dataset(DATASET_URL, file_name)

    df = pd.read_csv(file_name, header=None)
    df = clean_dataset(df)
    df.to_csv(file_name, index=False)

    summarize_dataset(df)

if __name__ == "__main__":
    import_data()
```

### Data cleaning
I used the `import_laptop_prices.py` script to clean the IBM dataset.

```python
import urllib.request

import numpy as np
import pandas as pd

DATASET_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"
)
DEFAULT_FILE_NAME = "laptop_pricing_dataset_base"
COLUMN_HEADERS = [
    "Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core",
    "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD",
    "Weight_kg", "Price",
]

def prompt_for_file_name():
    """Ask the user for an output file name, falling back to the default."""
    answer = input(f"Enter the file name to download (default: {DEFAULT_FILE_NAME}.csv): ")
    base_name = answer.strip() or DEFAULT_FILE_NAME
    return f"{base_name}.csv"

def download_dataset(url, file_name):
    """Download the dataset at ``url`` into ``file_name``."""
    urllib.request.urlretrieve(url, file_name)

def clean_dataset(df):
    """Clean the dataset by removing missing values and converting to float."""
    df = df.dropna(subset=COLUMN_HEADERS)
    df[COLUMN_HEADERS] = df[COLUMN_HEADERS].apply(pd.to_numeric, errors="coerce")
    return df

def summarize_dataset(df):
    """Print a summary of the dataset."""
    print(df.describe())

def import_data():
    """Download, clean and summarize the laptop pricing dataset."""
    file_name = prompt_for_file_name()
    download_dataset(DATASET_URL, file_name)

    df = pd.read_csv(file_name, header=None)
    df = clean_dataset(df)
    df.to_csv(file_name, index=False)

    summarize_dataset(df)

if __name__ == "__main__":
    import_data()
```

### Displaying statistics and data types
I used the `import_laptop_prices.py` script to display dataset statistics and data types.

```python
import urllib.request

import numpy as np
import pandas as pd

DATASET_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"
)
DEFAULT_FILE_NAME = "laptop_pricing_dataset_base"
COLUMN_HEADERS = [
    "Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core",
    "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD",
    "Weight_kg", "Price",
]

def prompt_for_file_name():
    """Ask the user for an output file name, falling back to the default."""
    answer = input(f"Enter the file name to download (default: {DEFAULT_FILE_NAME}.csv): ")
    base_name = answer.strip() or DEFAULT_FILE_NAME
    return f"{base_name}.csv"

def download_dataset(url, file_name):
    """Download the dataset at ``url`` into ``file_name``."""
    urllib.request.urlretrieve(url, file_name)

def clean_dataset(df):
    """Clean the dataset by removing missing values and converting to float."""
    df = df.dropna(subset=COLUMN_HEADERS)
    df[COLUMN_HEADERS] = df[COLUMN_HEADERS].apply(pd.to_numeric, errors="coerce")
    return df

def summarize_dataset(df):
    """Print a quick overview of the cleaned dataset."""
    print("First 10 rows:")
    print(df.head(10))
    print("\nData types:")
    print(df.dtypes)
    print("\nStatistics:")
    print(df.describe(include="all"))
    print("\nInfo:")
    df.info()

def import_data():
    """Download, clean and summarize the laptop pricing dataset."""
    file_name = prompt_for_file_name()
    download_dataset(DATASET_URL, file_name)

    df = pd.read_csv(file_name, header=None)
    df = clean_dataset(df)
    df.to_csv(file_name, index=False)

    summarize_dataset(df)

if __name__ == "__main__":
    import_data()
```
