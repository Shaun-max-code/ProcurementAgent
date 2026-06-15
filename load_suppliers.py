import pandas as pd
from backend.database import get_connection

df = pd.read_csv("data/suppliers.csv")

conn = get_connection()

for _, row in df.iterrows():

    conn.execute(
        """
        INSERT INTO suppliers
        (supplier, category, moq, country)
        VALUES (?, ?, ?, ?)
        """,
        (
            row["Supplier"],
            row["Category"],
            row["MOQ"],
            row["Country"]
        )
    )

conn.commit()
conn.close()

print("Suppliers Imported")