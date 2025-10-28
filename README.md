# 📊 Hybrid RAG Financial Analysis System

## Overview  
This project is a **hybrid intelligent system** that combines **Retrieval-Augmented Generation (RAG)** for document analysis with **Agent-based querying** for structured data. It's designed to answer complex financial questions by intelligently routing between unstructured PDF documents (earnings reports) and structured CSV data (financial forecasts).

The system demonstrates advanced skills in **LangChain**, **LangGraph workflow orchestration**, **vector databases**, and **LLM-powered data analysis** for real-world financial planning scenarios.

***

## Key Highlights  
- **Hybrid Architecture**  
  - **PDF RAG Pipeline** – Semantic search through earnings reports using FAISS vector store with metadata filtering  
  - **CSV Agent** – Pandas-powered agent for structured data queries and calculations  
  - **Smart Routing** – Automatic query classification to route between document analysis and data operations  
 

- **Intelligent Query Processing**  
  - Query analysis with structured output parsing  
  - Metadata-based filtering (quarters, financial content flags)  
  - Context-preserving document chunking  
  - Multi-source context aggregation  

***

## Architecture  

### **System Flow**
```
User Query
    ↓
Query Analysis (Gemini Structured Output)
    ↓
Smart Router (Keyword-based)
    ↓
┌─────────────────┬──────────────────┐
│   PDF Pipeline  │   CSV Pipeline   │
│    (RAG)        │    (Agent)       │
│                 │                  │
│ 1. Embed Query  │ 1. Load DataFrame│
│ 2. Vector Search│ 2. Pandas Agent  │
│ 3. Filter by    │ 3. Execute Code  │
│    Metadata     │ 4. Return Result │
│ 4. Retrieve     │                  │
│    Context      │                  │
└─────────────────┴──────────────────┘
    ↓
Context Aggregation
    ↓
LLM Response Generation
    ↓
Final Answer with Source Attribution
```
***

## Technical Implementation

### **PDF Processing Pipeline**
- **LangChain PDFMinerLoader** with page concatenation for context preservation
- **RecursiveCharacterTextSplitter** for intelligent chunking
- **Metadata Enrichment**: Quarter detection, financial content flagging, chunk indexing
- **FAISS Storage**: Local persistence with Gemini embeddings

### **CSV Agent System**
- **LangChain Pandas DataFrame Agent** with Gemini 2.5 Flash
- **Dynamic Query Execution**: Generates and runs pandas code on-the-fly
- **Flexible Schema**: Works with any CSV structure without validation
- **Error Handling**: Graceful fallback for complex queries

### **Query Routing Logic**
```python
CSV Indicators:
- calculate, total, sum, average, variance
- forecast, actual, revenue, department
- Q1, Q2, Q3, Q4, year

PDF Indicators:
- why, how, explain, strategy, commentary
- management, challenges, analysis
- Default for ambiguous queries
```

***

## 🎯 Capabilities  

### **PDF Document Queries (RAG)**
- "Why did Q2 2024 performance disappoint?"
- "What challenges did management mention in the earnings call?"
- "Summarize the revenue commentary for Q2 2024"
- Metadata filtering by quarter and financial content type

### **CSV Data Queries (Agent)**
- "What was Q2 2024 total forecast revenue?"
- "Calculate variance between forecast and actual for all departments"
- "Which quarter had the highest revenue in 2024?"
- Dynamic pandas operations without predefined schemas

### **Hybrid Queries** *(Future Enhancement)*
- "Analyze Q2 2024 revenue performance with supporting numbers and management commentary"

***

## Tech Stack  
- **Framework:** LangChain, LangGraph  
- **LLM:** Google Gemini 2.5 Flash  
- **Embeddings:** Google Generative AI Embeddings  
- **Vector Store:** FAISS with local persistence  
- **Agent:** LangChain Experimental Pandas DataFrame Agent  
- **Core Libraries:** PDFMiner.six, Pandas, Pydantic  

***

## Learnings & Takeaways  
- Built a **production-ready hybrid AI system** combining RAG and agents  
- Implemented **intelligent query routing** for multi-modal data sources  
- Designed **metadata-rich document processing** for financial documents  
- Gained expertise in **LangGraph state management** for complex workflows  
- Learned **FAISS vector store optimization** and persistence patterns  
- Handled **LLM API limitations** with model selection and token optimization  
- Understood **agent limitations** and query decomposition strategies  

***

## Acknowledgments
Built as part of a hands-on RAG learning journey focusing on real-world financial analysis applications. Special thanks to the LangChain and Google Gemini communities for excellent documentation and tools.

***

**Note:** This project is under active development. The interface and advanced features are being incrementally added. The core hybrid RAG-Agent architecture is functional.