# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from responses import get_bot_response

app = Flask(__name__)
CORS(app)  # Allow cross-origin access from frontend

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = (data.get("message") or "").strip()
        if not user_message:
            return jsonify({"reply": "Please type something so I can help."})
        
        bot_reply = get_bot_response(user_message)
        return jsonify({"reply": bot_reply})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": "Sorry, there was a server error."}), 500

if __name__ == "__main__":
    app.run(debug=True)
