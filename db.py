import sqlite3
from config import DATABASE_URL

def execute_query(sql_query):
    """
    Execute an SQL query against the SQLite database and return results with cursor description.
    """
    try:
        db_path = DATABASE_URL.replace("sqlite:///", "")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        description = cursor.description  # Store column metadata
        conn.commit()
        conn.close()
        return results, description if results else (None, None)
    except sqlite3.Error as e:
        raise Exception(f"Database error: {str(e)}")