import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

SUPPLIER_FILE = BASE_DIR / "data" / "suppliers.csv"

def find_matches(category):

    suppliers = pd.read_csv(SUPPLIER_FILE)

    matches = suppliers[
        suppliers["Category"].str.lower()
        == category.lower()
    ]

    return matches