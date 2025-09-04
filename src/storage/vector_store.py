from langchain_community.vectorstores import FAISS
from ..config import get_gemini_embeddings
from ..processors.pdf_processor import process_pdf
import os

def create_vector_store_from_pdf(pdf_path: str, store_path: str = "./faiss_db"):
  chunks = process_pdf(pdf_path)
  vector_store = FAISS.from_documents(
      documents=chunks,
      embedding=get_gemini_embeddings()
  )
  vector_store.save_local(store_path)
  return vector_store

def load_vector_store(store_path: str = "./faiss_db"):
  if not os.path.exists(store_path):
    raise FileNotFoundError(f"Vector store not found at {store_path}")
  
  vector_store = FAISS.load_local(
    store_path,
    embeddings=get_gemini_embeddings(),
    allow_dangerous_deserialization=True
  )
  
  return vector_store

def search_with_metadata_filter(vector_store, query: str, filter_dict: dict = None, k: int = 5):
  if filter_dict:
    return vector_store.similarity_search(
      query, 
      k=k,
      filter=lambda metadata: all(
        metadata.get(key) == value for key, value in filter_dict.items()
      )
    )
  else:
    return vector_store.similarity_search(query, k=k)