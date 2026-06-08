import pandas as pd

CLIENT_FILE = "data/client_requests.csv"
SUPPLIER_FILE = "data/suppliers.csv"
MEETING_FILE = "data/meetings.csv"


def get_requests():
    return pd.read_csv(CLIENT_FILE)


def get_suppliers():
    return pd.read_csv(SUPPLIER_FILE)


def get_meetings():
    return pd.read_csv(MEETING_FILE)