# src/query/query_schema.py
from typing import List
from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints

QuarterStr = Annotated[str, StringConstraints(pattern=r"^Q[1-4]\s\d{4}$")]

class Search(BaseModel):
  """Schema for financial search queries."""
  query: str = Field(..., description="Search query to run.")
  quarters: List[QuarterStr] = Field(
      ..., description="List of quarters like 'Q2 2024'."
  )
  contains_financial_data: bool = Field(
      ..., description="Does the query contain financial data or not?"
  )
