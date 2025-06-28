from flask import request, jsonify
import time


def rate_limiter(max_calls=5, window_seconds=60):
    client_records = {}

    def decorator(func):
        def wrapper(*args, **kwargs):
            ip = request.remote_addr
            now = time.time()
            timestamps = client_records.get(ip, [])
            timestamps = [t for t in timestamps if now - t < window_seconds]
            if len(timestamps) >= max_calls:
                return jsonify({"error": "Rate limit exceeded"}), 429
            timestamps.append(now)
            client_records[ip] = timestamps
            return func(*args, **kwargs)

        return wrapper

    return decorator
