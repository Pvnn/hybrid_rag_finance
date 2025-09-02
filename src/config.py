import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_llm():
  return GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key = os.getenv('GOOGLE_API_KEY')
  )

def get_gemini_embeddings():
  return GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key = os.getenv('GOOGLE_API_KEY')
  )