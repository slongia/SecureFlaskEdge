from flask import request, jsonify


def auth_required(valid_tokens):
    def decorator(func):
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token or token not in valid_tokens:
                return jsonify({"error": "Unauthorized"}), 401
            return func(*args, **kwargs)

        return wrapper

    return decorator
