from langgraph.graph import START, StateGraph
from src.graphs.state import State
from langchain import hub
from src.config import get_gemini_llm
from src.storage.vector_store import load_vector_store
from src.query.query_schema import Search
from google import genai

try:
	vector_store = load_vector_store("./faiss_db")
except Exception as e:
	print(f"Error loading FAISS store: {e}")


prompt = hub.pull("rlm/rag-prompt")

llm = get_gemini_llm()

def analyze_query(state: State):
	client = genai.Client()
	resp = client.models.generate_content(
		model="gemini-2.5-flash",
		contents=state["question"],
		config={
				"response_mime_type": "application/json",
				"response_schema": Search, 
		},
	)
	query: dict = resp.parsed.model_dump()
	print(query)
	return {"query": query}

def retrieve(state: State):
	query = state["query"]

	def metadata_filter(md: dict) -> bool:
		if not md:
			return False
		doc_quarters = md.get("quarters_mentioned")

		if isinstance(doc_quarters, list):
			quarters_match = any(q in query["quarters"] for q in doc_quarters)
		else:
			quarters_match = (doc_quarters in query["quarters"])

		contains_match = md.get("contains_financial_data") == query["contains_financial_data"]

		return quarters_match and contains_match

	retrieved_docs = vector_store.similarity_search(
			query["query"],
			filter=metadata_filter,
	)
	return {"context": retrieved_docs}



def generate(state: State):
	docs_content = "\n\n".join(doc.page_content for doc in state["context"])
	messages = prompt.invoke({"question": state["question"], "context": docs_content})
	response = llm.invoke(messages)
	return {"answer": response}

def create_graph():
  graph_builder = StateGraph(State).add_sequence([analyze_query, retrieve, generate])
  graph_builder.add_edge(START, "analyze_query")
  graph = graph_builder.compile()
  return graph 

if __name__ == "__main__":
  graph:StateGraph = create_graph()
  result = graph.invoke({"question": "Summarize the results for Q2 2024."})
  print(f"Answer: {result['answer']}")