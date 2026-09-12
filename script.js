console.log("Portfolio website loaded successfully!");

function toggleMenu() {
    document.getElementById("nav-menu").classList.toggle("active");
}
function openChatbot() {
    document.getElementById("chatbot-window").style.display = "flex";
}

function closeChatbot() {
    document.getElementById("chatbot-window").style.display = "none";
}

async function sendChatMessage() {

    const input = document.getElementById("chatbot-input");
    const chatMessages = document.getElementById("chatbot-messages");

    const message = input.value.trim();

    console.log("Message:", message);

    if (message === "") {
        return;
    }

    // Show user message
    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.textContent = message;

    chatMessages.appendChild(userMessage);

    // Clear input
    input.value = "";

    // Show thinking message
    const botMessage = document.createElement("div");
    botMessage.className = "bot-message";
    botMessage.textContent = "Thinking... 🤖";

    chatMessages.appendChild(botMessage);

    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        botMessage.textContent = data.reply;

    } catch (error) {

        console.error("Chat error:", error);

        botMessage.textContent =
            "Sorry, I couldn't connect to the AI server. 😔";
    }

    chatMessages.scrollTop = chatMessages.scrollHeight;
}
