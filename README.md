# Intelligent-AI-Assistant-for-Student-Records

**Problem Statement**

Educational institutions manage vast amounts of student data, such as grades, enrollment details, and contact information, typically stored in relational databases. Querying this data often requires technical knowledge of SQL, which can be a barrier for non-technical users like administrators or educators. Existing interfaces may be rigid or complex, leading to inefficiencies and errors. There is a need for an intuitive, user-friendly system that allows users to retrieve student records using plain English, without requiring knowledge of database query languages.

The Intelligent AI Assistant solves this problem by enabling users to query student records in natural language (e.g., "Show me the grades for student John Doe"). The system uses AI to translate these queries into SQL, execute them against a database, and present the results in a clear, readable format, streamlining data access for educational institutions.

**Overview**

This project is an AI-powered assistant designed to simplify the retrieval of student records from a database. Users can input queries in plain English, and the AI agent, powered by Google’s Gemini API, converts them into SQL queries, executes them using SQLite, and displays results via a Streamlit web interface. The system is ideal for educational institutions, administrators, or developers building user-friendly database interfaces.

Features

- Natural Language Querying: Users can input queries in plain English (e.g., "List students with grades below 70").
- AI-to-SQL Conversion: Leverages Google’s Gemini API to translate natural language into accurate SQL queries.
- Database Integration: Uses SQLite for lightweight, local database management.
- Interactive Interface: Streamlit provides a web-based UI for inputting queries and viewing results.
- Formatted Results: Returns data in tables or JSON for easy readability.
- Error Handling: Manages invalid queries or database errors with user-friendly feedback.

**Prerequisites**

- Python 3.8 or higher
- SQLite (included with Python)
- Google Cloud account with Gemini API access
- Streamlit for the web interface
- Bash shell (for environment variable setup)

**Installation**

Clone the repository:
  - git clone https://github.com/your-username/Intelligent-AI-Assistant-for-Student-Records.git
  - cd Intelligent-AI-Assistant-for-Student-Records

Replace your-username with your actual GitHub username.

Create a virtual environment and install dependencies:
``python -m venv venv``
``source venv/bin/activate  # On Windows: venv\Scripts\activate``
``pip install -r requirements.txt``


Initialize the database:
``python init_db.py``


Configure environment variables:

- Create a .env file in the project root:echo "GOOGLE_API_KEY=your-google-api-key" > .env
- echo "DATABASE_URL=sqlite:///students.db" >> .env

Replace your-google-api-key with a valid Google Gemini API key.
Alternatively, add to ~/.bashrc (or ~/.zshrc):nano ~/.bashrc

Add:export GOOGLE_API_KEY="your-google-api-key"
export DATABASE_URL="sqlite:///students.db"

Apply changes:source ~/.bashrc





Usage

Run the Streamlit app:
streamlit run app.py


Access the web interface:

Open your browser and navigate to http://localhost:8501 (or the forwarded URL in GitHub Codespaces).
Enter a natural language query (e.g., "Show me the grades for student John Doe").


The AI assistant will:

Use Google’s Gemini API to generate SQL.
Execute the query against the SQLite database.
Display results in a table via Streamlit.

Sample interaction:
Input: "Show me the grades for student John Doe"
SQL Generated: SELECT course, grade FROM grades JOIN students ON grades.student_id = students.id WHERE students.name = 'John Doe';
Output:
``| course    | grade |
|-----------|-------|
| Math 101  | 85    |
| CS 201    | 92    |``



Project Structure

``intelligent-ai-assistant/
├── app.py               # Streamlit app for the web interface
├── agent.py             # AI logic for query-to-SQL conversion
├── db.py                # Database connection and query execution
├── config.py            # Configuration loading
├── init_db.py           # Script to initialize the SQLite database
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
├── tests/               # Directory for unit tests
│   └── test_agent.py    # Unit tests for query conversion
└── README.md            # Project documentation``

app.py: Streamlit application for the web interface.
agent.py: Logic for processing queries and generating SQL using Google’s Gemini API.
db.py: SQLite database connection and query execution utilities.
init_db.py: Script to initialize the database with sample data.
config.py: Configuration for API keys and database settings.
.env: Environment variables (loaded via python-dotenv).
tests/: Unit tests for query conversion.
requirements.txt: Python dependencies.
.gitignore: Excludes sensitive files (e.g., .env, students.db).

Technologies Used

Programming Language:
