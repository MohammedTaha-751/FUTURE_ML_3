from flask import Flask, request, jsonify, render_template # type: ignore
import os
from chatbot.model import Chatbot

app = Flask(__name__)
chatbot = Chatbot()

# Home page route
@app.route("/")
def index():
    return render_template("index.html")

# API to get chatbot response
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"response": "Please enter a question.", "confidence": 0.0})

    response, confidence = chatbot.get_response(user_input)
    return jsonify({"response": response, "confidence": confidence})

# API for insights (placeholder)
@app.route("/api/insights", methods=["GET"])
def insights():
    return jsonify({"message": "Insights API is not implemented in this version."})

if __name__ == "__main__":
    app.run(debug=True)
