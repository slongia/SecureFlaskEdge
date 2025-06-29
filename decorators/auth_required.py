from flask import request, jsonify
from config import VALID_TOKENS


def auth_required(tokens=VALID_TOKENS):
    def decorator(func):
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token or token not in tokens:
                return jsonify({"error": "Unauthorized"}), 401
            return func(*args, **kwargs)

        return wrapper

    return decorator
