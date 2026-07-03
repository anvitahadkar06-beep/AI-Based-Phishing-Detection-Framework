from flask import Flask, request, jsonify
from flask_cors import CORS

from decision_engine import decide
from logger import log_scan

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI-Based Phishing Detection Backend",
        "status": "Running"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/predict", methods=["POST"])
def predict():

    # Read JSON request
    data = request.get_json()

    # Check if JSON exists
    if not data:
        return jsonify({
            "error": "No JSON data received."
        }), 400

    # Get URL
    url = data.get("url")

    # Check if URL is provided
    if not url:
        return jsonify({
            "error": "URL is required."
        }), 400

    try:
        # AI Prediction
        result = decide(url)

        # Save scan history
        log_scan(result)

        # Return result
        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)

   