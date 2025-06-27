from flask import Flask, request
from decorators.log_request import log_request

app = Flask("SecureFlaskEdge")


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
