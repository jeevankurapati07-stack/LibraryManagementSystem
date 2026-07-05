# database.py
import sqlite3
import os
from config import Config

def get_connection():
    """Returns a database connection based on .env config."""
    if Config.DB_TYPE == 'sqlite':
        os.makedirs(os.path.dirname(Config.SQLITE_PATH), exist_ok=True)
        return sqlite3.connect(Config.SQLITE_PATH)
    else:
        print(f"Connecting to remote {Config.DB_TYPE} database...")
        return None

def initialize_database():
    """Initializes tables using schema.sql without overwriting existing data."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        schema_path = os.path.join(os.path.dirname(__file__), 'database', 'schema.sql')
        if os.path.exists(schema_path):
            with open(schema_path, 'r') as file:
                cursor.executescript(file.read())
                conn.commit()
                print("[SUCCESS] Database initialized successfully.")
        conn.close()