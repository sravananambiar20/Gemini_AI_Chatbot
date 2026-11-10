
import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

# Initialize Flask
app = Flask(__name__)

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Store conversation history
conversations = {}

# Bot personality
SYSTEM_PROMPT = """
You are a friendly and helpful AI assistant.
Answer questions clearly and politely.
Keep your answers simple and easy to understand.
"""

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():

    try:
        data = request.get_json()

        message = data.get("message", "").strip()
        conversation_id = data.get("conversation_id", "default")

        if not message:
            return jsonify({"error": "Message cannot be empty"}), 400

        # Get or create conversation history
        if conversation_id not in conversations:
            conversations[conversation_id] = []

        history = conversations[conversation_id]

        # Add user message
        history.append({
            "role": "user",
            "parts": [{"text": message}]
        })

        # Keep only the last 10 messages
        context = history[-10:]

        # Generate Gemini response
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=context,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        bot_reply = response.text

        if not bot_reply:
            raise ValueError("Gemini returned an empty response")

        # Save assistant response
        history.append({
            "role": "model",
            "parts": [{"text": bot_reply}]
        })

        return jsonify({
            "conversation_id": conversation_id,
            "user_message": message,
            "bot_response": bot_reply
        })

    except Exception as e:
        # Remove the unsent user message if generation failed
        if "history" in locals() and history and history[-1]["role"] == "user":
            history.pop()

        print("Error:", str(e))

        return jsonify({
            "error": "Unable to generate a response. Please try again."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
