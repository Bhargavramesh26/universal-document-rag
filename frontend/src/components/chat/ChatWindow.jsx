import { useContext, useEffect, useRef, useState } from "react";

import api from "../../services/api";
import { SessionContext } from "../../context/SessionContext";
import { ModelContext } from "../../context/ModelContext";

import MessageBubble from "./MessageBubble";

function ChatWindow() {

    const { sessionId } = useContext(SessionContext);
    const { selectedModel } = useContext(ModelContext);

    const [question, setQuestion] = useState("");
    const [loading, setLoading] = useState(false);
    const [status, setStatus] = useState("");

    const [messages, setMessages] = useState([
        {
            sender: "assistant",
            message: "Hello! Upload a document and ask me anything."
        }
    ]);

    const bottomRef = useRef(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages]);

    const sendMessage = async () => {

        if (!question.trim()) return;

        if (loading) return;

        if (!sessionId) {
            setStatus("Please upload a document first.");
            return;
        }

        setStatus("");

        const userQuestion = question;

        setMessages((prev) => [
            ...prev,
            {
                sender: "user",
                message: userQuestion,
            },
        ]);

        setQuestion("");

        setLoading(true);

        try {

            const response = await api.post("/chat", {
                session_id: sessionId,
                question: userQuestion,
                model: selectedModel,
            });

            setMessages((prev) => [
                ...prev,
                {
                    sender: "assistant",
                    message: response.data.answer,
                },
            ]);

        } catch (error) {

            setStatus("Unable to contact the server.");
            if (import.meta.env.DEV) {
                console.error(error);
            }
            setMessages((prev) => [
                ...prev,
                {
                    sender: "assistant",
                    message: "Failed to get response from server.",
                },
            ]);


        } finally {

            setLoading(false);

        }
    };

    return (

        <div className="chat-container">

            <div className="chat-messages">

                {messages.map((msg, index) => (

                    <MessageBubble
                        key={index}
                        sender={msg.sender}
                        message={msg.message}
                    />

                ))}

                <div ref={bottomRef}></div>

            </div>

            {status && (
                <div className="chat-status">
                    {status}
                </div>
            )}

            <div className="chat-input">

                <input
                    type="text"
                    placeholder="Ask a question..."
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    onKeyDown={(e) => {

                        if (e.key === "Enter" && !loading) {
                            sendMessage();
                        }

                    }}
                />

                <button
                    onClick={sendMessage}
                    disabled={loading}
                >
                    {loading ? "Thinking..." : "Send"}
                </button>

            </div>

        </div>
    );
}

export default ChatWindow;