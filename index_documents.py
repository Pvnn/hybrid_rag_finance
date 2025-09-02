from src.storage.vector_store import create_vector_store_from_pdf

if __name__ == "__main__":
  print("Starting document indexing...")
  vector_store = create_vector_store_from_pdf(
      pdf_path="data/earnings_report.pdf",
      collection_name="financial_docs"
  )
  
  print("Indexing complete!")
  print(f"Documents stored in: ./chroma_db")
  results = vector_store.similarity_search("Q2 revenue", k=2)
  print(f"Test search returned {len(results)} chunks")
