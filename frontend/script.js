const API_URL = "http://backend-service:5000/messages"; // internal cluster name

async function sendMessage() {
  const message = document.getElementById("message").value;
  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });
  loadMessages();
}

async function loadMessages() {
  const res = await fetch(API_URL);
  const messages = await res.json();
  document.getElementById("messages").innerHTML = messages.map(
    msg => `<li>${msg}</li>`
  ).join("");
}

loadMessages();
