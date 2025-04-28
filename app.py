from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # allows all origins — simple for testing

@app.route("/")
def home():
    return "This is your Backend!"

@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.get_json()
    print("Received data:", data)
    return jsonify({"message": "Data received successfully!"})  # You must return something!

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # For Render
    app.run(host='0.0.0.0', port=port)
