"""Download the IBM automobile dataset, label its columns and clean it."""

import urllib.request

import numpy as np
import pandas as pd

DATASET_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
)
OUTPUT_FILE_NAME = "auto_dataset.csv"
COLUMN_HEADERS = [
    "symboling", "normalized-losses", "make", "fuel-type", "aspiration",
    "num-of-doors", "body-style", "drive-wheels", "engine-location",
    "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
    "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke",
    "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg",
    "price",
]


def download_dataset(url, file_name):
    """Download the dataset at ``url`` into ``file_name``."""
    urllib.request.urlretrieve(url, file_name)


def clean_dataset(df):
    """Apply headers, replace missing markers and drop rows without a price."""
    df.columns = COLUMN_HEADERS
    df = df.replace("?", np.nan)
    return df.dropna(subset=["price"], axis=0)


def summarize_dataset(df):
    """Print a quick overview of the cleaned dataset."""
    print("First 5 rows:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)
    print("\nStatistics:")
    print(df.describe(include="all"))
    print("\nInfo:")
    df.info()


def import_automobile():
    """Download, clean and summarize the automobile dataset."""
    download_dataset(DATASET_URL, OUTPUT_FILE_NAME)

    df = pd.read_csv(OUTPUT_FILE_NAME, header=None)
    df = clean_dataset(df)
    df.to_csv(OUTPUT_FILE_NAME, index=False)

    summarize_dataset(df)


if __name__ == "__main__":
    import_automobile()
