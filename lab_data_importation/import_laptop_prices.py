"""Download the IBM laptop pricing dataset, label its columns and clean it."""

import urllib.request

import numpy as np
import pandas as pd

DATASET_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"
)
OUTPUT_FILE_NAME = "laptop_pricing_dataset_base.csv"
COLUMN_HEADERS = [
    "Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core",
    "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD",
    "Weight_kg", "Price",
]


def download_dataset(url, file_name):
    """Download the dataset at ``url`` into ``file_name``."""
    urllib.request.urlretrieve(url, file_name)


def clean_dataset(df):
    """Apply headers and replace missing-value markers with NaN."""
    df.columns = COLUMN_HEADERS
    return df.replace("?", np.nan)


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


def import_laptop_data():
    """Download, clean and summarize the laptop pricing dataset."""
    download_dataset(DATASET_URL, OUTPUT_FILE_NAME)

    df = pd.read_csv(OUTPUT_FILE_NAME, header=None)
    df = clean_dataset(df)
    df.to_csv(OUTPUT_FILE_NAME, index=False)

    summarize_dataset(df)


if __name__ == "__main__":
    import_laptop_data()
