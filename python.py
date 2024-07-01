#!C:\Users\Admin\AppData\Local\Programs\Python\Python310\python.exe
 
print("Content-type: text/html\n\n")
import cgi
import sqlite3
 
# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
 
# Function to execute SQL query and retrieve results
def execute_query(query, params=None):
    try:
        if query:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
 
            result = cursor.fetchall()
            return result
        else:
            return "No query provided."
    except Exception as e:
        return f"Error executing query: {str(e)}"
     
# Create a table and insert two users into the database
create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
'''
 
insert_users_query = '''
    INSERT INTO users (username, email) VALUES
    ('user1', 'user1@example.com'),
    ('user2', 'user2@example.com')
'''
 
# Execute the table creation and user insertion queries
execute_query(create_table_query)
execute_query(insert_users_query)
 
# Get form data
form = cgi.FieldStorage()
 
# Retrieve SQL query from the form
sql_query = form.getvalue('sql_query')
 
# HTML and CSS for the form and result display
html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGI Database Query</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            margin: 20px;
        }}
 
        h1 {{
            color: #333;
            text-align: center;
        }}
 
        form {{
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: 20px auto;
        }}
 
        label {{
            display: block;
            margin-bottom: 8px;
        }}
 
        textarea {{
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }}
 
        input[type="submit"] {{
            background-color: #4caf50;
            color: #fff;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }}
 
        input[type="submit"]:hover {{
            background-color: #45a049;
        }}
 
        h2 {{
            color: #333;
            margin-top: 20px;
        }}
 
        pre {{
            white-space: pre-wrap;
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
 
        p.error {{
            color: #ff0000;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>CGI Database Query</h1>
    <form method="post" action="/database/python.py"> <!-- Corrected form action -->
        <label for="sql_query">Enter SQL Query:</label>
        <textarea name="sql_query" rows="4" cols="10" required>{sql_query}</textarea><br>
        <input type="submit" value="Execute Query">
    </form>
 
    <h2>Query Results:</h2>
"""
 
# Execute the SQL query and handle errors
try:
    result = execute_query(sql_query)
    html += f"<pre>{result}</pre>"
except Exception as e:
    html += f"<p class='error'>Error: {str(e)}</p>"
 
html += """
</body>
</html>
"""
 
# Display the HTML
print(html)
 
# Close the database connection
conn.close()