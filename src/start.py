import os

from flask import Flask, jsonify

secret_key = os.environ.get("SECRET_KEY")
if not secret_key:
    raise ValueError("Missing SECRET_KEY environment variable")

app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key
app.config["DEBUG"] = os.environ.get("DEBUG", default=True)

PORT = os.environ.get("PORT", default=5000)


@app.route("/healthz")
def healthz():
    response = {
        "Status": "OK",
    }

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(port=PORT)
