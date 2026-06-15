import sqlite3

conn = sqlite3.connect("procurement.db")

conn.execute("""
UPDATE suppliers
SET description='Protein snacks and nutrition products'
WHERE supplier='FoodCorp'
""")

conn.commit()
conn.close()

print("Descriptions added")