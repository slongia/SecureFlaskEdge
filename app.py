from flask import Flask, request
from functools import wraps
import time

app = Flask("SecureFlaskEdge")


def log_request(prefix="LOG"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            method = request.method
            endpoint = request.endpoint

            print(f"{prefix} {method} {endpoint} - calling {func.__name__}.")

            result = func(*args, **kwargs)

            duration = round((time.time() - start_time) * 1000, 2)

            print(f"{prefix} {method} {endpoint} - done in {duration} ms.")
            return result

        return wrapper

    return decorator


@app.route("/", methods=["GET"])
@log_request(prefix="API")
def index():
    return "hello world"


@app.route("/add/<int:a>/<int:b>", methods=["GET"])
@log_request(prefix="MATH")
def add(a, b):
    return str(a + b)


if __name__ == "__main__":
    app.run()
