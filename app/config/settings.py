from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()


# Project Paths

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
CHROMA_DB_DIR = BASE_DIR / "chroma_db"
LOG_DIR = BASE_DIR / "logs"
VECTOR_DB = "chroma"
COLLECTION_NAME = "ask_my_docs"


# API Keys


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")


# Embedding Settings


EMBEDDING_MODEL = "embed-english-v3.0"
EMBEDDING_PROVIDER = "cohere"

# LLM Settings

LLM_MODEL = "gemini-3.5-flash"

# Chunk Settings


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


# Retrieval


TOP_K = 15
RETRIEVAL_TYPE = "hybrid"


# Reranker


RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
RERANK_TOP_K = 5


# Evaluation


EVALUATION_DIR = BASE_DIR / "evaluation"
DATASET_PATH = EVALUATION_DIR / "dataset.json"
REPORT_DIR = BASE_DIR / "reports"