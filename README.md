# Gemini AI Chatbot – LLM API Integration

## Project Overview
Gemini AI Chatbot is a web-based conversational AI application built using Python, Flask, and Google's Gemini API. It allows users to interact with an AI assistant through a simple chat interface.

## Features
- Integration with Google Gemini API.
- Multi-turn conversational memory.
- Maintains the last 10 messages as conversation context.
- Custom system prompt defining the assistant's personality.
- Flask backend with a `/chat` API endpoint.
- Interactive web interface using HTML, CSS, and JavaScript.
- Basic error handling for failed API requests.
- API key securely stored using environment variables.

## Technologies Used
- Python 3.12
- Flask
- Google Gen AI SDK
- Gemini 3.1 Flash Lite
- HTML
- CSS
- JavaScript
- python-dotenv

## Project Structure

```text
Gemini_AI_Chatbot/
│
├── app.py
├── test_api.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Gemini_AI_Chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_actual_api_key
```

Obtain an API key from Google AI Studio.

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## API Endpoint

**POST `/chat`**

Example request:

```json
{
  "message": "Hello!",
  "conversation_id": "test-1"
}
```

The backend sends the message and recent conversation history to Gemini and returns the AI-generated response.

## Context Management

The application stores conversation history separately using a conversation ID. It sends the last 10 messages as context for each new request, allowing Gemini to maintain multi-turn conversations.

Conversation history is stored in application memory and resets when the Flask server restarts.

## Security

- API credentials are stored in `.env`.
- `.env` and the virtual environment are excluded using `.gitignore`.
- API keys should never be committed to GitHub.

## Testing

The application was manually tested for:
- Gemini API connectivity.
- Flask backend functionality.
- Message submission and response generation.
- Multi-turn conversation memory.
- Five consecutive conversational turns.

## Future Improvements
- Persistent conversation storage.
- User authentication.
- Multiple conversation management.
- Improved response formatting.
