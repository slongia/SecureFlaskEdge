from flask import Flask
from decorators.log_request import log_request
from decorators.auth_required import auth_required
from decorators.rate_limiter import rate_limiter

app = Flask("SecureFlaskEdge")


@app.route("/secure-data")
@rate_limiter(max_calls=3, window_seconds=30)
@auth_required()
@log_request(prefix="SECURE")
def secure_data():
    return {"status": "success", "data": "top secret info"}


@app.route("/", methods=["GET"])
@log_request(prefix="API")
def index():
    return "hello world"


@app.route("/public", methods=["GET"])
@log_request(prefix="PUBLIC")
def public():
    return "Public Access"


if __name__ == "__main__":
    app.run(debug=True)
