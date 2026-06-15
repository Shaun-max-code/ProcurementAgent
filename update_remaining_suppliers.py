import sqlite3

conn = sqlite3.connect("procurement.db")

conn.execute("""
UPDATE suppliers
SET description =
'Snack manufacturing and packaged food products'
WHERE supplier='SnackWorks'
""")

conn.execute("""
UPDATE suppliers
SET description =
'Beauty and skincare product manufacturing'
WHERE supplier='GlowManufacturing'
""")

conn.commit()
conn.close()

print("Remaining descriptions added")