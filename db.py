import psycopg2
from config import POSTGRESQL_CONFIG


def get_connection():
    return psycopg2.connect(
        # dbname="SecureFlaskEdge",
        # user="postgres",
        # password="postgres",
        # host="localhost",
        # port="5432",
        **POSTGRESQL_CONFIG
    )
