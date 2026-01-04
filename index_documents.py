import pandas as pd
from tqdm import tqdm

from document_processor import SECDocumentProcessor
from vector_store import SECVectorStore
from config import BATCH_SIZE

CSV_PATH = "data/sec_filings.csv"


def main():
    print("Starting SEC filings indexing pipeline...")

    # Initialize processor and vector store
    processor = SECDocumentProcessor()
    vector_store = SECVectorStore(
        persist_directory="vector_store",
        collection_name="sec_filings"
    )

    # Load CSV
    df = pd.read_csv(CSV_PATH)
    print(f"Total rows in CSV: {len(df)}")

    all_docs = []

    # Step 1: Process each filing
    for _, row in tqdm(df.iterrows(), total=len(df)):
        file_path = row.get("file_path")

        if not isinstance(file_path, str):
            continue

        try:
            # Extract raw text
            text = processor.extract_text(file_path)

            # Skip very small documents
            if not text or len(text.strip()) < 200:
                continue

            # Extract metadata
            metadata = processor.extract_metadata(row)

            # Chunk document into LangChain Documents
            chunks = processor.chunk_document(text, metadata)

            all_docs.extend(chunks)

        except Exception as e:
            print(f"Skipping {file_path}: {e}")

    print(f"Total chunks created: {len(all_docs)}")

    if len(all_docs) == 0:
        print("❌ No documents generated. Exiting.")
        return

    # Step 2: Batch index documents
    print("Indexing documents into Chroma...")

    for i in range(0, len(all_docs), BATCH_SIZE):
        batch = all_docs[i:i + BATCH_SIZE]
        vector_store.db.add_documents(batch)

    # Step 3: Persist to disk
    vector_store.db.persist()

    # Step 4: Verify count
    count = vector_store.db._collection.count()
    print(f"✅ Indexing completed successfully!")
    print(f"📊 Total documents in vector store: {count}")


if __name__ == "__main__":
    main()
