from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from config import EMBEDDING_MODEL, VECTOR_DB_DIR, COLLECTION_NAME


class SECVectorStore:

    def __init__(self):
        self.embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)

        self.db = Chroma(
            collection_name="sec_filings",
            embedding_function=self.embeddings,
            persist_directory="vector_store"
        )

    def add_documents(self, documents):
        self.db.add_documents(documents)
        self.db.persist()

    def search(self, query, k):
        return self.db.similarity_search_with_score(query, k=k)

    def get_info(self):
        return {
            "collection": COLLECTION_NAME,
            "count": self.db._collection.count()
        }
