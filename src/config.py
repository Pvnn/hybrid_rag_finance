import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  
PROJECT_ROOT = os.path.dirname(BASE_DIR)              

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

def get_gemini_chat_llm():
  return ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
  )