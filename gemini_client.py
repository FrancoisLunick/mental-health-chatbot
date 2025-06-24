import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("GEMINI_API_KEY"))

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)