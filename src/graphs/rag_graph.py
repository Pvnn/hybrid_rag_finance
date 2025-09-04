from langgraph.graph import START, StateGraph
from src.graphs.state import State
from langchain import hub
from src.config import get_gemini_llm
from src.storage.vector_store import load_vector_store

try:
    vector_store = load_vector_store("./faiss_db")
except Exception as e:
    print(f"Error loading FAISS store: {e}")


prompt = hub.pull("rlm/rag-prompt")

llm = get_gemini_llm()

def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"], k=4)
    return {"context": retrieved_docs}


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response}

def create_graph():
  graph_builder = StateGraph(State).add_sequence([retrieve, generate])
  graph_builder.add_edge(START, "retrieve")
  graph = graph_builder.compile()
  return graph 

if __name__ == "__main__":
  graph:StateGraph = create_graph()
  result = graph.invoke({"question": "Summarize the results for Q2 2024."})
  print(f"Answer: {result['answer']}")