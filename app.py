from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "This is your Backend!"

@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.get_json()
    print("Recieved data:", data)


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  
    app.run(host='0.0.0.0', port=port)


from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
