# 📄 Universal Document RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload documents and ask questions based on their contents using Large Language Models (LLMs). The application retrieves relevant document context from a vector database before generating accurate responses.

---

# 🚀 Features

- Upload PDF, DOCX, and TXT documents
- Automatic document processing and chunking
- Vector embedding generation using HuggingFace Embeddings
- ChromaDB vector database for semantic search
- Retrieval-Augmented Generation (RAG)
- Multiple LLM support
  - Ollama
  - Google Gemini
  - Groq
- Session-based document management
- Modern React frontend
- FastAPI backend
- Responsive user interface

---

# 🛠 Technology Stack

## Backend

- Python 3.12
- FastAPI
- Uvicorn
- LangChain
- LangChain Community
- LangChain Chroma
- LangChain HuggingFace
- LangChain Ollama
- LangChain Google Generative AI
- LangChain Groq
- ChromaDB
- HuggingFace Sentence Transformers
- PyMuPDF
- Docx2txt
- Pydantic
- Pydantic Settings
- Python-dotenv

---

## Frontend

- React
- Vite
- Axios
- React Context API
- React Icons
- HTML5
- CSS3
- JavaScript (ES6+)

---

# 📁 Project Structure

```
Universal-document-rag
│
├── backend
│   ├── app
│   ├── storage
│   ├── requirements.txt
│   ├── .env
│   └── ...
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   ├── .env
│   └── ...
│
├── README.md
└── .gitignore
```

---

# ⚙️ Backend Setup

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Universal-document-rag.git

cd Universal-document-rag
```

---

## 2. Navigate to Backend

```bash
cd backend
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create a `.env` file inside the `backend` folder.

```env
APP_NAME=Universal Document RAG Assistant
APP_VERSION=1.0.0

API_PREFIX=/api/v1

HOST=127.0.0.1
PORT=8000

DEBUG=True

ALLOWED_ORIGINS=http://localhost:5173

OLLAMA_MODEL=llama3.2

GEMINI_MODEL=gemini-2.5-flash
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

GROQ_MODEL=llama-3.3-70b-versatile
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## 6. Install and Run Ollama (Optional)

Download Ollama:

https://ollama.com/download

Pull the model:

```bash
ollama pull llama3.2
```

Start Ollama:

```bash
ollama serve
```

---

## 7. Run Backend

```bash
uvicorn app.main:app --reload --reload-dir app
```

Backend API:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 💻 Frontend Setup

## 1. Open a New Terminal

Navigate to the frontend directory.

```bash
cd frontend
```

---

## 2. Install Dependencies

```bash
npm install
```

---

## 3. Configure Environment Variables

Create a `.env` file inside the `frontend` folder.

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api/v1
```

---

## 4. Run Frontend

```bash
npm run dev
```

Frontend URL:

```
http://localhost:5173
```

---

# ▶️ How to Use

1. Start the backend.
2. Start the frontend.
3. Open the frontend in your browser.
4. Upload a supported document.
5. Select the preferred LLM.
6. Ask questions related to the uploaded document.
7. Receive context-aware responses generated using Retrieval-Augmented Generation (RAG).

---

# 📌 Supported File Types

- PDF (.pdf)
- Microsoft Word (.docx)
- Text (.txt)

---

# 🤖 Supported LLM Providers

- Ollama
- Google Gemini
- Groq

---

# 📷 Screenshots

Add screenshots of:

- Home Page
- Upload Document
- Model Selection
- Chat Interface
- Generated Response

---

# 📄 License

This project is intended for educational and learning purposes.
