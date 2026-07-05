function MessageBubble({

    sender,
    message,

}) {

    return (

        <div className={`message ${sender}`}>

            <strong>

                {

                    sender === "assistant"

                        ? "🤖 AI"

                        : "👤 You"

                }

            </strong>

            <p>

                {message}

            </p>

        </div>

    );

}

export default MessageBubble;