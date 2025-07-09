from flask import Flask
from decorators.log_request import log_request
from decorators.auth_required import auth_required
from decorators.rate_limiter import rate_limiter

app = Flask(__name__)


@app.route("/secure")
@rate_limiter()
@auth_required()
@log_request(prefix="SECURE")
def secure():
    return {"message": "Authenticated and Logged."}


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
