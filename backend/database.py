import sqlite3

DB_NAME = "procurement.db"


def get_connection():

    conn = sqlite3.connect(DB_NAME)

    return conn


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    # ==========================================
    # REQUESTS
    # ==========================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        product TEXT,
        category TEXT,
        moq INTEGER,
        country TEXT
    )
    """)

    # ==========================================
    # SUPPLIERS
    # ==========================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS suppliers (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    supplier TEXT,
    category TEXT,
    moq INTEGER,
    country TEXT,

    can_do TEXT,

    cannot_do TEXT,

    last_response TEXT
)
""")
    # ==========================================
    # MEETINGS
    # ==========================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meetings (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        brand TEXT,
        supplier TEXT,
        meeting_date TEXT,
        status TEXT
    )
    """)

    # ==========================================
    # FOLLOWUPS
    # ==========================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS followups (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        supplier TEXT,
        brand TEXT,
        followup_date TEXT,
        status TEXT
    )
    """)

    # ==========================================
    # ESCALATIONS
    # ==========================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS escalations (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        supplier TEXT,
        issue TEXT,
        priority TEXT
    )
    """)

    # ==========================================
    # YES / NO / MAYBE RESPONSES
    # ==========================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS supplier_responses (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    supplier TEXT,
    request_id INTEGER,

    response TEXT,

    notes TEXT,

    response_date TEXT,

    status TEXT,

    client_answer TEXT
     )
    """)

    # ==========================================
    # PARTNER DATABASE
    # ==========================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS partners (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        supplier TEXT,
        commission_partner TEXT
    )
    """)
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS human_handoffs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    supplier TEXT,

    request_id INTEGER,

    status TEXT,

    notes TEXT
  )
 """)
       # ==========================================
    # EMAIL HISTORY
    # ==========================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        supplier TEXT,

        product TEXT,

        email_type TEXT,

        email_content TEXT,

        created_date TEXT
    )
    """)

    # ==========================================
    # COMPETITOR DATABASE
    # ==========================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS competitors (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        competitor TEXT,

        manufacturer TEXT,

        confidence_score INTEGER
    )
    """)

    conn.commit()

    conn.close()


if __name__ == "__main__":

    create_tables()

    print("Tables Created Successfully")