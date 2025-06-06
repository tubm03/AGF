import React, { useState, useEffect, useRef } from "react";
import io, { Socket } from "socket.io-client";
import type { Message } from "../types";

const Chat: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState<string>("");
  const [user] = useState<string>("User" + Math.floor(Math.random() * 1000));
  const [isTyping, setIsTyping] = useState<boolean>(false);
  const socketRef = useRef<Socket | null>(null);

  useEffect(() => {
    // Khởi tạo kết nối Socket.IO
    socketRef.current = io("http://localhost:5000", {
      transports: ["websocket"],
    });

    const socket = socketRef.current;

    // Xử lý sự kiện kết nối
    socket.on("connect", () => {
      console.log("Connected to WebSocket server");
    });

    // Nhận lịch sử tin nhắn
    socket.on("messages", (msgHistory: Message[]) => {
      setMessages(msgHistory);
    });

    // Nhận tin nhắn mới
    socket.on("new_message", (newMsg: Message) => {
      setMessages((prev) => [...prev, newMsg]);
    });

    // Xử lý typing indicator
    socket.on("user_typing", (typing: boolean) => {
      setIsTyping(typing);
    });

    // Kiểm tra kết nối HTTP
    const checkConnection = async () => {
      try {
        const response = await fetch("http://localhost:5000/ping");
        const data = await response.json();
        console.log("Backend status:", data);
      } catch (error) {
        console.error("Backend connection error:", error);
      }
    };

    checkConnection();

    // Dọn dẹp khi component unmount
    return () => {
      socket.disconnect();
    };
  }, []);

  const sendMessage = () => {
    if (input.trim() && socketRef.current) {
      const newMessage: Omit<Message, "id"> = {
        text: input,
        user: user,
      };
      socketRef.current.emit("new_message", newMessage);
      setInput("");
      notifyTyping(false);
    }
  };

  const notifyTyping = (typing: boolean) => {
    if (socketRef.current) {
      socketRef.current.emit("user_typing", typing);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInput(e.target.value);
    notifyTyping(e.target.value.length > 0);
  };

  return (
    <div className="chat-container">
      <div className="user-info">
        Logged in as: <strong>{user}</strong>
      </div>

      <div className="messages">
        {messages.map((msg) => (
          <div key={msg.id} className="message">
            <span className="message-user">{msg.user}:</span>
            <span className="message-text">{msg.text}</span>
            {msg.timestamp && (
              <span className="message-time">
                {new Date(msg.timestamp).toLocaleTimeString()}
              </span>
            )}
          </div>
        ))}
      </div>

      {isTyping && <div className="typing-indicator">Someone is typing...</div>}

      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          onKeyPress={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Type a message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chat;
