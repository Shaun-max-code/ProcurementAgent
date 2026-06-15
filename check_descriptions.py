import sqlite3

conn = sqlite3.connect("procurement.db")

rows = conn.execute(
    "SELECT supplier, description FROM suppliers"
).fetchall()

print(rows)

conn.close()