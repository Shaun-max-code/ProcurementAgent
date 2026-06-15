import sqlite3

conn = sqlite3.connect("procurement.db")

conn.execute("""
UPDATE suppliers
SET description='Protein snacks and nutrition products'
WHERE supplier='FoodCorp'
""")

conn.execute("""
UPDATE suppliers
SET description='Health supplements and protein manufacturing'
WHERE supplier='NutriFoods'
""")

conn.execute("""
UPDATE suppliers
SET description='Organic food production and healthy snacks'
WHERE supplier='FreshFactory'
""")

conn.execute("""
UPDATE suppliers
SET description='Cosmetics and skincare manufacturing'
WHERE supplier='BeautyLabs'
""")

conn.commit()
conn.close()

print("Descriptions updated")