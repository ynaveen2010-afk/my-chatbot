from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    reply = f"You said: {user_msg}"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
