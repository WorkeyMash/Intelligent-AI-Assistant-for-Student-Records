import google.generativeai as genai
from config import GOOGLE_API_KEY
import re

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Database schema context for the AI
SCHEMA_CONTEXT = """
The database has the following tables:
- students (id: INTEGER, name: TEXT, major: TEXT)
- grades (student_id: INTEGER, course: TEXT, grade: INTEGER)
Primary key: students.id
Foreign key: grades.student_id references students.id
"""

def process_query(natural_language_query):
    """
    Convert a natural language query to an SQL query using Gemini API.
    """
    try:
        prompt = f"""
        {SCHEMA_CONTEXT}
        Convert the following natural language query to an SQL query:
        '{natural_language_query}'
        Provide only the SQL query as output, without any explanations or Markdown formatting (e.g., no ```sql or ```).
        For queries asking for grades, include both the course and grade columns unless specified otherwise.
        """
        response = model.generate_content(prompt)
        sql_query = response.text.strip()
        # Remove any Markdown code block syntax
        sql_query = re.sub(r'```sql\n|```', '', sql_query).strip()
        return sql_query
    except Exception as e:
        raise Exception(f"Failed to process query: {str(e)}")