import pandas as pd
from langchain_core.prompts import ChatPromptTemplate
from langchain_experimental.tools import PythonAstREPLTool
from langchain_experimental.agents import create_pandas_dataframe_agent
from typing import Dict, Any

def load_csv(csv_path : str)-> pd.DataFrame:
  try:
    df = pd.read_csv(csv_path)
    print(f"Loaded CSV with {len(df)} rows, {len(df.columns)} columns")
    return df
  except Exception as e:
    print("Failed to read csv file :", e)
    raise

def create_csv_agent(df: pd.DataFrame, llm):
  agent = create_pandas_dataframe_agent(
    llm = llm,
    df = df,
    agent_type="openai-tools",
    verbose= True,
    allow_dangerous_code= True,
    return_intermediate_steps= True,
  )
  return agent

def query_csv_data(agent, question: str, csv_path:str =None) -> Dict[str, Any]:
  try:
    result = agent.invoke({"input": question})
    return {
      "answer" : result["output"],
      "source_type": "structured",
      "source_file": csv_path or "CSV data",
      "success": True,
      "intermediate_steps": result.get("intermediate_steps", [])
    }
  except Exception as e:
    return {
      "error": f"CSV query failed: {str(e)}",
      "answer": "Unable to process CSV query",
      "source_type": "structured",
      "success": False
    }

def setup_csv_agent(csv_path:str, llm):
  df = load_csv(csv_path=csv_path)
  agent = create_csv_agent(df, llm)
  return agent, df

from src.config import get_gemini_chat_llm
llm = get_gemini_chat_llm()
agent, df = setup_csv_agent("data/forecast.csv", llm)
result = query_csv_data(agent, "What columns are available in this data?")
print(result["answer"])
result = query_csv_data(agent, "Looking at the forecast revenue data, calculate the total forecast for each year (extract year from Quarter column), then tell me which year had the highest total forecast revenue.")
print(result["answer"])
result = query_csv_data(agent, "What's the total revenue for Q2?") 
print(result["answer"])
