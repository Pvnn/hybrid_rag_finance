from langchain_community.document_loaders import PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import re
from typing import List

def load_pdf_document(pdf_path):
  loader = PDFMinerLoader(
    pdf_path,
    mode="single",
  )
  docs = loader.load()
  return docs[0] #Return the Document Object

def detect_financial_quarters(text):
  patterns = [
    r'Q[1-4]\s*202[3-6]',
    r'Q[1-4]\s*FY\s*202[3-6]',
    r'[Ff]irst [Qq]uarter 202[3-6]',
    r'[Ss]econd [Qq]uarter 202[3-6]',
    r'[Tt]hird [Qq]uarter 202[3-6]',
    r'[Ff]ourth [Qq]uarter 202[3-6]'
  ]
  quarters=[]
  for pattern in patterns:
    matches = re.findall(pattern, text)
    quarters.extend(matches)

  return list(set(quarters))

def has_financial_indicators(text: str) -> bool:
    """
    Check if chunk contains financial metrics/discussions
    """
    financial_keywords = [
      'revenue', 'forecast', 'actual', 'variance', 'budget', 'earnings',
      'profit', 'loss', 'margin', 'growth', 'performance', 'guidance',
      '$', '%', 'million', 'billion', 'YoY', 'QoQ'
    ]
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in financial_keywords)

def chunk_document_with_context(document: Document, chunk_size=1000, chunk_overlap=200)-> List[Document]:
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size= chunk_size,
    chunk_overlap = chunk_overlap,
    separators=["\n\n", "\n", ". ", "! ", "? ", ", ", " ", ""]
  )
  chunks = []
  text_chunks = text_splitter.split_text(document.page_content)
  for i, chunk_text in enumerate(text_chunks):
    quarters = detect_financial_quarters(chunk_text)
    chunk_metadata = {
      **document.metadata,
      "chunk_index" : i,
      "chunk_size" : len(chunk_text),
      "quarters_mentioned" : ", ".join(quarters) if quarters else "Unknown",
      "document_type": "earnings_report",
      "contains_financial_data": has_financial_indicators(chunk_text)
    }

    chunk_doc = Document(page_content=chunk_text, metadata= chunk_metadata)
    chunks.append(chunk_doc)
  return chunks

def process_pdf(pdf_path:str, chunk_size=1000, chunk_overlap=200)-> List[Document]:
  try:
    document = load_pdf_document(pdf_path)
    print(f"Loaded PDF with {len(document.page_content)} characters")
    chunks = chunk_document_with_context(document, chunk_size, chunk_overlap)
    print(f"Created {len(chunks)} chunks from document")
    return chunks
  except Exception as e:
    print(f"Error processing PDF {pdf_path} : {str(e)}")
    return []

def validate_chunks(chunks: List[Document]) -> None:
  if not chunks:
    print("No chunks created")
    return
  
  print(f"\n=== Chunk Validation ===")
  print(f"Total chunks: {len(chunks)}")
  
  # Check for financial content
  financial_chunks = [c for c in chunks if c.metadata.get('contains_financial_data', False)]
  print(f"Chunks with financial data: {len(financial_chunks)}")
  
  # Sample first few chunks
  for i, chunk in enumerate(chunks[:3]):
    print(f"\nChunk {i}:")
    print(f"Content preview: {chunk.page_content[:150]}...")
    print(f"Quarters mentioned: {chunk.metadata.get('quarters_mentioned', [])}")
    print(f"Has financial data: {chunk.metadata.get('contains_financial_data', False)}")

def test_processor(pdf_path: str = "data/earnings_report.pdf"):
  chunks = process_pdf(pdf_path)
  validate_chunks(chunks)
  return chunks