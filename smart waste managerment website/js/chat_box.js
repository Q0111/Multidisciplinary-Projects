function handleKeyPress(event) {
    if (event.keyCode === 13) { // Enter key has keycode 13
      sendMessage();
      event.preventDefault(); // Prevent default Enter key behavior (new line)
    }
  }

  function sendMessage() {
    const input = document.querySelector('.chat-input');
    const message = input.value.trim();

    if (message !== '') {
      const messageDiv = document.createElement('div');
      messageDiv.className = 'chat-message user-message';
      messageDiv.textContent = message;
      document.querySelector('.chat-messages').appendChild(messageDiv);
      input.value = ''; // Clear the input after sending the message
    }
  }