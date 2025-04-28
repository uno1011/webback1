from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "This is your Backend!"

@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.get_json()
    print("Recieved data:", data)


if __name__ == "__main__":
    app.run(debug=True)