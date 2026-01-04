from langchain_google_genai import ChatGoogleGenerativeAI
from vector_store import SECVectorStore
from config import LLM_MODEL, TOP_K


class SECRAGChain:

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=LLM_MODEL,
            temperature=0.2
        )
        self.vector_store = SECVectorStore()

    def ask(self, question, top_k=TOP_K):
        results = self.vector_store.search(question, top_k)

        context = ""
        sources = []

        for doc, score in results:
            context += f"\nSOURCE: {doc.metadata}\n{doc.page_content}\n"
            sources.append(doc.metadata)

        prompt = f"""
Answer STRICTLY from the context below.
If answer is not present, say "Information not found in SEC filings".

CONTEXT:
{context}

QUESTION:
{question}
"""

        answer = self.llm.invoke(prompt).content

        summary_prompt = f"""
Summarize the answer below in 2-3 simple sentences for investors:

{answer}
"""
        summary = self.llm.invoke(summary_prompt).content

        claim_prompt = """
Rate from 0-100 how well the context answers the question.
Only return a number.
"""
        claim_percentage = float(self.llm.invoke(claim_prompt).content.strip())

        return {
            "answer": answer,
            "summary": summary,
            "sources": sources,
            "claim_percentage": claim_percentage,
            "retrieved_chunks": len(results)
        }
