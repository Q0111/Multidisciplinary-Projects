function handleKeyPress(event) {
  if (event.keyCode === 13) {
    sendMessage();
    event.preventDefault();
  }
}

function displayMessage(sender, content) {
  const messageDiv = document.createElement('div');
  messageDiv.className = `chat-message ${sender}-message`;
  messageDiv.textContent = content;
  document.querySelector('.chat-messages').appendChild(messageDiv);
}

function sendMessage() {
  const input = document.querySelector('.chat-input');
  const message = input.value.trim();

  if (message !== '') {
    // Display user message on the webpage
    displayMessage('user', message);

    // Make a POST request to the Rasa server to get the chatbot's response
    fetch('http://localhost:5005/webhooks/rest/webhook', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        sender: 'user',
        message: message,
      }),
    })
      .then(response => response.json())
      .then(data => {
        // Display the chatbot's response on the webpage
        const chatbotResponse = data[0]?.text || 'Sorry, I couldn\'t understand that.';
        displayMessage('chatbot', chatbotResponse);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });

    input.value = ''; // Clear the input after sending the message
  }
}

document.querySelector('.chat-input').addEventListener('keypress', handleKeyPress);
