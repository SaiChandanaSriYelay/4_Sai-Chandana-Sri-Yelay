# SEC Filing Summarizer & Verified Q&A System (RAG-Based)

## Project Description

This project is an AI-powered **SEC filing analysis system** that allows users to ask questions on company filings such as **10-K and 10-Q reports** and receive:

- **Factually accurate answers**
- **Verified source citations from the filing**
- **Concise summaries of the retrieved information**

The system uses **Retrieval-Augmented Generation (RAG)** to ensure that all answers are grounded strictly in official SEC documents, reducing hallucinations and increasing trustworthiness.

---

## Project Objectives

- Enable easy understanding of complex SEC filings
- Provide **document-backed answers** with citations
- Generate **clear summaries** alongside verified answers
- Improve reliability of AI-generated financial insights

---

## Technology Stack

### Programming & Data Processing
- Python
- Pandas

### Document Processing
- SEC filing text extraction
- Document chunking and metadata handling

### AI & NLP
- Large Language Model (LLM) for question answering and summarization
- Text embeddings for semantic search (e.g., `text-embedding-3-small`)

### Retrieval System
- Retrieval-Augmented Generation (RAG)

### Frameworks & Tools
- LangChain (pipelines, retrieval, prompts)
- Pydantic (structured and validated outputs)

---

## Key Features

- Ask natural language questions on SEC filings
- Answers verified with source citations
- Summarized explanations for better readability
- Works with real SEC filing datasets
- Reduced hallucinations through document grounding

---

## Output Format

Each query returns:
- **Verified Answer** – generated strictly from filing content
- **Summary** – simplified explanation for the questions of the retrieved sections
- **Source Reference** – document chunk or section used
- **Claim Percentage** - tells how much percentage it is satisfied, or not satisfied, or partially satisfied.

## Dataset

SEC Filings Dataset (Kaggle):  
https://www.kaggle.com/datasets/kharanshuvalangar/sec-filings
