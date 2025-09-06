import streamlit as st
from agent import process_query
from db import execute_query
import pandas as pd

st.title("Intelligent AI Assistant for Student Records")

# Input query
query = st.text_input("Enter your query (e.g., 'Show me the grades for student John Doe'):")

if st.button("Submit Query"):
    if query:
        try:
            # Process the query to generate SQL
            sql_query = process_query(query)
            st.write("**Generated SQL Query:**")
            st.code(sql_query, language="sql")

            # Execute the query and fetch results with description
            results, description = execute_query(sql_query)

            if results:
                # Get column names from description
                columns = [desc[0] for desc in description]
                # Convert results to DataFrame for display
                df = pd.DataFrame(results, columns=columns)
                st.write("**Results:**")
                st.dataframe(df)
            else:
                st.write("No results found.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a query.")