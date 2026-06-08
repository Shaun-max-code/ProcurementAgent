import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

FILE = BASE_DIR / "data" / "client_requests.csv"

def save_request(product, category, moq, country):

    new_request = pd.DataFrame([{
        "Product": product,
        "Category": category,
        "MOQ": moq,
        "Country": country
    }])

    if FILE.exists():

        new_request.to_csv(
            FILE,
            mode="a",
            header=False,
            index=False,
            lineterminator="\n"
        )

    else:

        new_request.to_csv(
            FILE,
            index=False,
            lineterminator="\n"
        )

    return True