from src.storage.vector_store import create_vector_store_from_pdf

if __name__ == "__main__":
  print("Starting document indexing...")
  vector_store = create_vector_store_from_pdf(
    pdf_path="data/earnings_report.pdf",
    store_path="./faiss_db"
  )
  
  print("Indexing complete!")
  results = vector_store.similarity_search("Q2 revenue", k=2)
  print(f"Test search returned {len(results)} chunks")
  if results:
    print(f"Sample result: {results[0].page_content[:150]}...")
