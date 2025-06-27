# Logging Decorator
from flask import request
from functools import wraps
from db import get_connection

import time


def log_request(prefix="LOG"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            method = request.method
            path = request.path

            response = func(*args, **kwargs)
            duration = round((time.time() - start_time) * 1000, 2)
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO api_logs(prefix, endpoint, method, duration_ms)
                        VALUES (%s,%s,%s,%s)
                        """,
                (prefix, path, method, duration),
            )
            conn.commit()
            cur.close()
            conn.close()

            return response

        return wrapper

    return decorator
