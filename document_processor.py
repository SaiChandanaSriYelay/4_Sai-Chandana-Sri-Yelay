import os
from bs4 import BeautifulSoup
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from unstructured.partition.auto import partition
from config import CHUNK_SIZE, CHUNK_OVERLAP


class SECDocumentProcessor:

    def clean_html(self, html_text):
        soup = BeautifulSoup(html_text, "html.parser")
        for tag in soup(["script", "style", "table"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)

    def extract_text(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()

        if ext in [".html", ".htm"]:
            with open(file_path, encoding="utf-8", errors="ignore") as f:
                return self.clean_html(f.read())

        if ext in [".txt", ".csv"]:
            with open(file_path, encoding="utf-8", errors="ignore") as f:
                return f.read()

        if ext == ".pdf":
            elements = partition(filename=file_path)
            return "\n".join([e.text for e in elements if e.text])

        return ""

    def extract_metadata(self, row):
        return {
            "company": row.get("company", "Unknown"),
            "filing_type": row.get("form_type", "Unknown"),
            "filing_date": row.get("date_filed", "Unknown"),
            "source": row.get("file_path", "")
        }

    def chunk_document(self, text, metadata):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        chunks = splitter.split_text(text)

        return [
            Document(page_content=chunk, metadata=metadata)
            for chunk in chunks
        ]
