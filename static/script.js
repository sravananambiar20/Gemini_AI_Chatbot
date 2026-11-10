
// Create a unique conversation ID for this browser session
const conversationId = "chat-" + Date.now();

// Get HTML elements
const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-btn");

// Display a message in the chat
function displayMessage(message, sender) {
    const messageDiv = document.createElement("div");

    messageDiv.classList.add(sender + "-message");
    messageDiv.textContent = message;

    chatBox.appendChild(messageDiv);

    // Automatically scroll to the latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send message to Flask backend
async function sendMessage() {

    const message = userInput.value.trim();

    if (message === "") {
        return;
    }

    // Display user message
    displayMessage(message, "user");

    userInput.value = "";
    sendButton.disabled = true;

    // Show loading message
    const loadingDiv = document.createElement("div");
    loadingDiv.classList.add("bot-message");
    loadingDiv.textContent = "Gemini is thinking...";
    chatBox.appendChild(loadingDiv);

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        // Send request to Flask
        const response = await fetch("/chat", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message,
                conversation_id: conversationId
            })
        });

        const data = await response.json();

        // Remove loading message
        loadingDiv.remove();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        // Display Gemini response
        displayMessage(data.bot_response, "bot");

    } catch (error) {

        loadingDiv.remove();

        displayMessage(
            "Sorry! " + error.message,
            "bot"
        );

        console.error("Chat error:", error);

    } finally {

        sendButton.disabled = false;
        userInput.focus();

    }
}

// Send message when Enter is pressed
userInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});
