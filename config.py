import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

EMBEDDING_MODEL = "models/embedding-001"
LLM_MODEL = "gemini-1.5-flash"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

VECTOR_DB_DIR = os.path.join(BASE_DIR, "vector_store")
COLLECTION_NAME = "sec_filings"

TOP_K = 5
BATCH_SIZE = 50
