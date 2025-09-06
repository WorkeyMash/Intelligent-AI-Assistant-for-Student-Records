import unittest
from agent import process_query

class TestAgent(unittest.TestCase):
    def test_query_conversion(self):
        query = "Show me the grades for student John Doe"
        sql_query = process_query(query)
        expected = "SELECT grade FROM grades WHERE student_id = (SELECT id FROM students WHERE name = 'John Doe')"
        self.assertIn("SELECT", sql_query, "SQL query should contain SELECT statement")
        self.assertIn("John Doe", sql_query, "SQL query should reference John Doe")

if __name__ == "__main__":
    unittest.main()