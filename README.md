
# Production-Level RAG

A production-style Retrieval-Augmented Generation (RAG) system that lets you upload a PDF and ask questions about it — with answers grounded in the document and backed by citations, not hallucinations.

Built with a hybrid retrieval pipeline (semantic + keyword search), cross-encoder reranking, and Gemini as the generation model, all wrapped in a simple Streamlit UI.

---

## 🚀 Features

- 📄 **PDF Upload & Parsing** — ingest any PDF document
- ✂️ **Smart Chunking** — splits documents into overlapping chunks for better context retention
- 🧠 **Semantic Embeddings** — powered by Cohere's `embed-english-v3.0`
- 🗂️ **Vector Storage** — persisted in ChromaDB
- 🔎 **Hybrid Retrieval** — combines dense vector search with BM25 keyword search
- 🎯 **Cross-Encoder Reranking** — re-scores retrieved chunks for higher precision
- 📝 **Context-Aware Prompting** — structured prompt template feeds only relevant context to the LLM
- 🤖 **LLM-Powered Answers** — generated using Gemini (`gemini-3.5-flash`)
- 📌 **Citation Generator** — every answer is traceable back to its source chunk
- 🖥️ **Streamlit UI** — clean, simple interface to upload documents and chat with them

---

## 🏗️ Architecture

```
User Upload PDF
      │
      ▼
Document Loader
      │
      ▼
Text Chunking
      │
      ▼
Embeddings (Cohere)
      │
      ▼
ChromaDB
      │
      ├──────────────┐
      ▼              ▼
Vector Search      BM25 Search
      │              │
      └──────┬───────┘
             ▼
     Hybrid Retrieval
             │
             ▼
   Cross-Encoder Reranker
             │
             ▼
      Context Builder
             │
             ▼
     Prompt Template
             │
             ▼
       Gemini LLM
             │
             ▼
    Citation Generator
             │
             ▼
      Streamlit UI
```

---

## 🛠️ Tech Stack

| Component          | Technology                               |
| ------------------ | ---------------------------------------- |
| Document Loader    | PyPDF / pdfplumber                       |
| Chunking           | Recursive text splitter                  |
| Embedding Model    | `embed-english-v3.0` (Cohere)          |
| Embedding Provider | Cohere                                   |
| Vector Database    | ChromaDB                                 |
| Sparse Retrieval   | BM25                                     |
| Reranker Model     | `cross-encoder/ms-marco-MiniLM-L-6-v2` |
| LLM                | `gemini-3.5-flash` (Google Gemini)     |
| Frontend / UI      | Streamlit                                |
| Language           | Python                                   |

---

## 📂 Project Structure

```
AD_RAG/
├── .deepeval/               # DeepEval config for RAG evaluation
├── .venv/                   # Python virtual environment
├── app/                     # Core application package
│   ├── chunking/              # Text splitting / chunking logic
│   ├── config/                 # App configuration & settings
│   ├── embeddings/               # Embedding generation (Cohere)
│   ├── llm/                        # Gemini LLM integration
│   ├── loaders/                     # Document loaders (PDF parsing)
│   ├── models/                       # Pydantic / data models
│   ├── prompts/                       # Prompt templates
│   ├── reranker/                       # Cross-encoder reranking
│   ├── retriever/                       # Hybrid retrieval (vector + BM25)
│   ├── services/                         # Business logic / orchestration
│   ├── ui/                                 # Streamlit UI components
│   ├── utils/                               # Shared utility functions
│   └── vectorstore/                          # ChromaDB integration
├── chroma_db/                # Persisted vector database
├── data/                      # Uploaded / sample documents
├── logs/                       # Application logs
├── reports/                     # Evaluation & test reports
├── tests/                         # Unit & integration tests
├── .env                             # Environment variables (API keys)
├── .gitignore
├── .python-version
├── Dockerfile                        # Containerized deployment
├── main.py                             # Application entry point
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/kunalnishad115/PRODUCTION_LEVEL_RAG.git
   cd PRODUCTION_LEVEL_RAG
   ```
2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```env
   GEMINI_API_KEY=your_gemini_api_key
   COHERE_API_KEY=your_cohere_api_key
   ```
5. **Run the app**

   ```bash
   streamlit run main.py
   ```

   Or with Docker:

   ```bash
   docker build -t production-level-rag .
   docker run -p 8501:8501 --env-file .env production-level-rag
   ```

---

## 🧪 How It Works

1. Upload a PDF through the Streamlit UI.
2. The document is split into overlapping text chunks.
3. Each chunk is embedded using Cohere's `embed-english-v3.0` model and stored in ChromaDB.
4. When you ask a question, the system runs **hybrid retrieval** — combining vector similarity search with BM25 keyword search — to fetch the most relevant chunks.
5. Retrieved chunks are passed through a **cross-encoder reranker** (`ms-marco-MiniLM-L-6-v2`) to refine relevance ranking.
6. The top chunks are assembled into context and sent to **Gemini (`gemini-3.5-flash`)** using a structured prompt template.
7. The final answer is returned along with **citations** pointing back to the exact source chunk(s).

---

## 📊 Why Hybrid Retrieval?

- **Vector search** captures semantic meaning — great for paraphrased or conceptual questions.
- **BM25** captures exact keyword matches — great for names, numbers, and specific terms.
- Combining both, followed by reranking, consistently improves retrieval accuracy over either method alone.

---

## 🔮 Future Improvements

- [ ] Support for multiple document uploads and cross-document Q&A
- [ ] Add evaluation pipeline (e.g., RAGAS) for measuring retrieval & answer quality
- [ ] Add caching layer for repeated queries
- [ ] Deploy as a hosted web app

---

## 🙏 Acknowledgements

Inspired by a RAG project ideas video by [Aishwarya Srinivasan](https://www.linkedin.com/in/aishwarya-srinivasan), whose explanation made this concept approachable enough to build end-to-end.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📬 Contact

Built by **Kunal Nishad**
🔗 GitHub: [kunalnishad115](https://github.com/kunalnishad115)

If you found this useful, consider ⭐ starring the repo!
