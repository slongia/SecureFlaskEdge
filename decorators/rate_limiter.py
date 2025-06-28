from flask import request, jsonify
from functools import wraps
import redis
from config import REDIS_URL

rdb = redis.from_url(REDIS_URL)


def rate_limiter(max_calls=5, window_seconds=60):
    # client_records = {}
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ip = request.remote_addr
            key = f"rate:{ip}:{func.__name__}"

            current = rdb.get(key)

            if current and int(current) >= max_calls:
                # now = time.time()
                # timestamps = client_records.get(ip, [])
                # timestamps = [t for t in timestamps if now - t < window_seconds]
                # if len(timestamps) >= max_calls:
                return jsonify({"error": "Rate limit exceeded"}), 429

            pipe = rdb.pipeline()
            pipe.incr(key, 1)
            pipe.expire(key, window_seconds)
            pipe.execute()
            return func(*args, **kwargs)

        return wrapper

    return decorator
