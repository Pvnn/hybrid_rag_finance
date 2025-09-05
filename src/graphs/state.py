from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from src.query.query_schema import Search


class State(TypedDict):
    question: str
    query: Search
    context: List[Document]
    answer: str