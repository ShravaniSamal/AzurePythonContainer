from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify(status="pong")

@app.route("/hello")
def hello():
    return "Hello from Azure App Service container!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
