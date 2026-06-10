import sqlite3

DB_NAME = "procurement.db"


def get_connection():

    conn = sqlite3.connect(DB_NAME)

    return conn


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        product TEXT,
        category TEXT,
        moq INTEGER,
        country TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS suppliers (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        supplier TEXT,
        category TEXT,
        moq INTEGER,
        country TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meetings (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        brand TEXT,
        supplier TEXT,
        meeting_date TEXT,
        status TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS followups (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    supplier TEXT,

    brand TEXT,

    followup_date TEXT,

    status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS escalations (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        supplier TEXT,
        issue TEXT,
        priority TEXT
    )
    """)

    conn.commit()

    conn.close()