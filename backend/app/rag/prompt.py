from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer ONLY from the provided context.

Rules:
1. If the answer exists in the context, explain it in a simple and detailed manner.
2. If the answer is partially available, clearly mention what is available.
3. If the answer is not available in the context, politely reply:
   "I couldn't find the answer in the uploaded document."
4. Never make up information.
5. Use easy-to-understand language.

Context:
{context}

Question:
{question}

Answer:
"""
)