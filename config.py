# config.py
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

class Config:
    DB_TYPE = os.getenv("DB_TYPE", "sqlite")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "library.db")

    SQLITE_PATH = os.path.join(os.path.dirname(__file__), 'database', DB_NAME)