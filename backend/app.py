from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_response, load_faq_data
import os

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    if "message" not in data:
        return jsonify({"response": "Invalid request"}), 400
    user_message = data["message"]
    response = get_response(user_message)
    return jsonify({"response": response})

@app.route("/faqs", methods=["GET"])
def faqs():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(debug=True)
