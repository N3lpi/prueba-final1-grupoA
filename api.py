from flask import Flask
from flask import request

from aemet_metereologico import racha


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/estacion/<ticker>", methods=["GET"])
def get_ticker(ticker):
    return indi(ticker)


@app.route("/estacion/<ticker>", methods=["POST"])
def post_ticker(ticker):
    document = racha(ticker)
    return racha(document)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)