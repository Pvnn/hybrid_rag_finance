from langchain_chroma import Chroma
from ..config import get_gemini_embeddings
from ..processors.pdf_processor import process_pdf

def create_vector_store_from_pdf(pdf_path: str, collection_name: str = "financial_docs"):
  chunks = process_pdf(pdf_path)
  vector_store = Chroma(
      collection_name="collection_name",
      embedding_function=get_gemini_embeddings(),
      persist_directory="./chroma_db" 
  )
  document_ids = vector_store.add_documents(chunks)
  return vector_store