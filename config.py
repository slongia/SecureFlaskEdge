import os
from dotenv import load_dotenv
load_dotenv()

POSTGRESQL_CONFIG = {
    "dbname": os.getenv("DB_NAME", "SecureFlaskEdge"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "postgres"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
}

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
VALID_TOKENS = {"secrettoken123"}
