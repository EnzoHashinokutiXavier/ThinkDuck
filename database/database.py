import sqlite3
import os

# Define constant with relative path to database.db file
DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

# Database initialization function
def init_db():
    # Initializes database and creates tables from schema.sql
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql') # Gets directory of this file and looks for 'schema.sql'
    if not os.path.exists(schema_path): # Checks if schema.sql exists
        raise FileNotFoundError(f"schema.sql not found in {schema_path}")
    with sqlite3.connect(DB_PATH) as conn: # Connects to database as 'conn'
        with open(schema_path, 'r') as file: # Opens schema for reading as 'file'
            conn.executescript(file.read()) # Executes read script

# Reusable connection function
def get_db():
    conn = sqlite3.connect(DB_PATH)
    # Configures row_factory to return results as dictionaries
    conn.row_factory = sqlite3.Row
    # Returns a database connection
    return conn

# Helper function for common operations
def execute_query(query, params=None, fetch=False): # fetch = true when needing to return data
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        if fetch:
            return cursor.fetchall()
        else:
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()


# Operations for 4 main entities
# Use ? parameter to prevent SQL injection

# Users: create, search by ID, search by username, validate password

# Create user
def create_user(username, password_hash):
    # Use INSERT and capture returned ID (lastrowid)
    query = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    return execute_query(query, (username, password_hash))

# Search by ID
def get_user_by_id(user_id):
    # Use SELECT with WHERE, fetch = true
    query = "SELECT * FROM users WHERE id = ?"
    return execute_query(query, (user_id,), fetch = True)

# Search user by username
def get_user_by_username(username):
    # Filter by username
    query = "SELECT * FROM users WHERE username = ?"
    return execute_query(query, (username,), fetch = True)

# Validate password
def validate_password(user_id, password_hash):
    # Find user_id, compare password_hash
    user = get_user_by_id(user_id)
    if user and len(user) > 0:
        return user[0]['password_hash'] == password_hash
    return False

# Projects: create, list by user, search by ID, delete

# Create project
def create_project(user_id, name):
    # Creates a new project linked to the user
    return

# List projects
def get_projects_by_user(user_id):
    # Lists all user projects
    return

# Search projects
def get_project_by_id(project_id):
    # Search a specific project
    return

# Delete project
def delete_project(project_id):
    # Deletes a project
    return

# Sessions: create, list by project, search by ID, update status

# Create session
def create_session(project_id, title):
    # Create session within a project, remember that session starts with status = 'open'
    return

# List sessions
def get_sessions_by_project(project_id):
    # List all sessions of a project
    return

# Search session
def get_session_by_id(session_id):
    # Search specific session
    return

# Update status
def update_session_status(session_id, status):
    # Updates status open -> resolved
    return

# Entries: create, list by session, search by ID

# Create entry
def create_entry(session_id, entry_type, content):
    # Creates entry (type: problem, hypothesis, test, solution)
    return

# List entries
def get_entries_by_session(session_id):
    # Lists all entries of a session
    return

# Search entry
def get_entry_by_id(entry_id):
    # Search specific entry
    return