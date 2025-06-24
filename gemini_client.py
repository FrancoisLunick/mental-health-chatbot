import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.environ['GEMINI_API_KEY'])

def gen_gemini_response(user_input: list[dict]) -> str:
    prompt = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in user_input])
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(prompt)
    print(response.text)
    
    return response.text