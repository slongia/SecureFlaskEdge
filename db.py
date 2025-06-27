import psycopg2
from psycopg2.extras import RealDictCursor


def get_connection():
    return psycopg2.connect(
        dbname="SecureFlaskEdge",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432",
    )
