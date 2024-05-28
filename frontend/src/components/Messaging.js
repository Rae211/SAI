// src/components/Messaging.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Messaging() {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');

  useEffect(() => {
    axios.get('/api/messages')
      .then(response => setMessages(response.data))
      .catch(error => console.error('Error fetching messages:', error));
  }, []);

  const handleSendMessage = () => {
    axios.post('/api/messages', { text: newMessage })
      .then(response => setMessages([...messages, response.data]))
      .catch(error => console.error('Error sending message:', error));
  };

  return (
    <div>
      <h2>Messages</h2>
      <ul>
        {messages.map((msg, index) => (
          <li key={index}>{msg.text}</li>
        ))}
      </ul>
      <input
        type="text"
        value={newMessage}
        onChange={(e) => setNewMessage(e.target.value)}
      />
      <button onClick={handleSendMessage}>Send</button>
    </div>
  );
}

export default Messaging;
