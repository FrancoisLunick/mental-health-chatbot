import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("GEMINI_API_KEY"))

genai.configure(api_key = os.environ['GEMINI_API_KEY'])

def gen_gemini_response(user_input: str) -> str:
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(user_input)
    print(response.text)
    
    return response.text
    
print(gen_gemini_response("tell me about love"))