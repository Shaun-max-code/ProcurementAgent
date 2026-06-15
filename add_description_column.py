import sqlite3

conn = sqlite3.connect("procurement.db")

conn.execute("""
ALTER TABLE suppliers
ADD COLUMN description TEXT
""")

conn.commit()
conn.close()

print("Description column added successfully")