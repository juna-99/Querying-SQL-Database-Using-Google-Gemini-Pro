# End-to-End Text-to-SQL LLM Application with Querying SQL Database Using Google Gemini Pro

## Project Overview

This project demonstrates an end-to-end implementation of a Text-to-SQL application using a large language model (LLM). The application takes natural language queries, converts them into SQL queries using the Google Gemini Pro LLM, executes the generated queries on an SQL database, and returns the results to the user.

## Project Flow

1. Input Query: User provides a natural language query.

2. LLM Processing: The input is processed by the LLM (Google Gemini Pro) to generate an SQL query.

3. Database Interaction: The generated SQL query is executed on the SQL database.

4. Result Response: The database returns the results of the query, which are then displayed to the user.

### Flow Diagram:
Input Query ➔ LLM Application ➔ Gemini Pro ➔ SQL Query ➔ SQL Database ➔ Response

Implementation Steps

1. Set Up the SQL Database

• Use SQLite to create a sample database.

• Insert sample records into the database to simulate real-world data.

• Tools: Python for database setup and data insertion.

2. Develop the LLM Application

• Integrate Google Gemini Pro for natural language to SQL transformation.

• Handle error cases, such as incorrect or ambiguous queries.

• Ensure the system can handle various query complexities (e.g., SELECT, JOIN, AGGREGATIONS).

3. Query Execution

• Pass the generated SQL query to the database.

• Retrieve and format results for user-friendly output.

4. Build the User Interface (Optional)

• Create a simple interface (CLI, web app, or mobile app) for user interaction.

# Technology Stack

• Language Model: Google Gemini Pro

• Database: SQLite

• Programming Language: Python

• Libraries/Tools: SQLite3, OpenAI API (or Gemini Pro API), Flask/FastAPI (optional for UI development)


![image](https://github.com/user-attachments/assets/7a04d0f5-b233-4ab2-90ea-68e73f825c43)

