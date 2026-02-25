import json
import pandas as pd


def load_raw_data(path: str = "data/raw_credit_applications.json") -> pd.DataFrame:
    """Load raw credit application data from json and flatten it."""
    with open(path, "r", encoding="utf8") as f:
        data = json.load(f)

    df = pd.json_normalize(data, sep=".")
    return df
