from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenAI API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide SQL queries as responses
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text.strip()  # Remove any extra whitespace from the response

# Function to execute SQL query and fetch results from the database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally:
        conn.commit()
        conn.close()

# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION. For example:
    - Example 1: "How many entries of records are present?"
      SQL: SELECT COUNT(*) FROM STUDENT;
    - Example 2: "Tell me all the students studying in Data Science class."
      SQL: SELECT * FROM STUDENT WHERE CLASS='Data Science';
    
    Ensure that the output SQL query:
    1. Does not include ``` or sql markers.
    2. Is valid and executable for the given schema.
    """
]

# Streamlit App Configuration
st.set_page_config(page_title="Retrieve SQL Queries with Gemini")
st.header("Gemini App to Retrieve SQL Data")

# User input
question = st.text_input("Enter your question:", key="input")

# Button to submit the question
if st.button("Ask the question"):
    # Generate the SQL query using Gemini
    raw_response = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query")
    st.code(raw_response, language="sql")

    # Execute the SQL query and display results
    st.subheader("Query Results")
    try:
        result = read_sql_query(raw_response, "student.db")
        if result:
            for row in result:
                st.write(row)
        else:
            st.write("No results found.")
    except Exception as e:
        st.error(f"Error executing query: {e}")
