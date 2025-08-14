function addMessage(sender, text) {
    const chatbox = document.getElementById("chatbox");
    const msgDiv = document.createElement("div");
    msgDiv.className = sender === "You" ? "user" : "bot";
    msgDiv.innerHTML = `<strong>${sender}:</strong> ${text}`;
    chatbox.appendChild(msgDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById("userInput");
    const msg = input.value.trim();
    if (!msg) {
        alert("Please type a message.");
        return;
    }

    addMessage("You", msg);
    input.value = "";

    const typing = document.getElementById("typingIndicator");
    typing.style.display = "flex";

    try {
        const res = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: msg })
        });

        const data = await res.json();
        typing.style.display = "none";
        addMessage("Bot", data.reply);

    } catch (err) {
        typing.style.display = "none";
        console.error("Error:", err);
        addMessage("Bot", "⚠ Sorry, could not connect to server.");
    }
}
