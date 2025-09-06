import sqlite3

def initialize_database():
    """
    Initialize the SQLite database with students and grades tables.
    """
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            major TEXT
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            student_id INTEGER,
            course TEXT,
            grade INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
        """)

        # Insert sample data
        cursor.execute("INSERT OR IGNORE INTO students (id, name, major) VALUES (1, 'John Doe', 'Computer Science')")
        cursor.execute("INSERT OR IGNORE INTO students (id, name, major) VALUES (2, 'Jane Smith', 'Mathematics')")
        cursor.execute("INSERT OR IGNORE INTO grades (student_id, course, grade) VALUES (1, 'Math 101', 85)")
        cursor.execute("INSERT OR IGNORE INTO grades (student_id, course, grade) VALUES (1, 'CS 201', 92)")
        cursor.execute("INSERT OR IGNORE INTO grades (student_id, course, grade) VALUES (2, 'Math 101', 78)")

        conn.commit()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing database: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_database()