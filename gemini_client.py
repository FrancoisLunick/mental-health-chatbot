"""
This is the module for when generating the responses using the Google Gemini API.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the a .env file
load_dotenv()

# Configure the gemini API with the API key from the environment variables
genai.configure(api_key = os.environ['GEMINI_API_KEY'])

def gen_gemini_response(user_input: list[dict]) -> str:
    """
    Generates a response using the Google Gemini API based on the chat history.

    Args:
        user_input (list[dict]): A list of dictionaries that represents a chat history.

    Returns:
        str: The AI-generated response text from the model.
    """
    
    # Convert the chat history into a string prompt
    prompt = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in user_input])
    # Initialize the generative model
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    # Generate a response based on the prompt
    response = model.generate_content(prompt)
    # Print the response text
    print(response.text)
    # Returns the response text
    return response.text