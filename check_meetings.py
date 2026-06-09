import sqlite3

conn = sqlite3.connect("procurement.db")

rows = conn.execute(
    "SELECT * FROM meetings"
).fetchall()

for row in rows:
    print(row)

conn.close()