"""
This module have the core logic for handling user interaction, mood detection, internet checks, and integrating 
AI responses.
"""

from .prompts import load_supportive_messages
import random
from gemini_client import gen_gemini_response
import socket

# Main class responsible for chatbot behavior.
class ChatCore:
    
    def __init__(self):
        # predefined mood-based responses.
        self.responses = {
            "sad" : "I'm really sorry to hear that.", 
            "anxious": "Let's take a deep breathe.", 
            "happy": "That's great to hear."
        }
        
        # Stores chat history and loads offline supportive messages.
        self.convo_history = []
        self.supportive_messages = load_supportive_messages()
    
    def detect_mood(self, user_input):
        """
        Analyzes the user input to detect emotional tone.

        Args:
            user_input (str): The text entered by the user.

        Returns:
            str: The detected mood keyword or "neutral" if none is matched.
        """
        
        user_input = user_input.lower()
        
        for mood in self.responses:
            if mood in user_input:
                return mood
        return "neutral"
    
    def give_a_response(self, user_input):
        """
        Returns a response based on detected mood or randomly selects a supportive message.

        Args:
            user_input (str): The user's message.

        Returns:
            str: A response either based on mood or a fallback supportive message.
        """
        
        mood = self.detect_mood(user_input)
        
        self.convo_history.append({"role": "user", "content": user_input})
        
        if mood in self.responses:
            return self.responses[mood]
        else:
            return random.choice(self.supportive_messages)
        
    def is_there_internet(self):
        """
        Checks for internet connectivity by attempting to reach a known ip address.

        Returns:
            bool: if the internet is reachable it returns True, if not it returns False.
        """
        
        target_ip = '8.8.8.8'
        target_port = 53
        
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            client_socket.connect((target_ip, target_port))
            
            return True
        except socket.timeout:
            return False
        
    def chat(self, user_input):
        """
        Main method to handle user message. It appends the message to the chat history only if online.

        Args:
            user_input (str): The user's message.

        Returns:
            str: AI-generated or supportive fallback responses.
        """
        
        if user_input == "":
            return "What? is wrong? Let me help."
        
        if self.is_there_internet():
            try:
                self.convo_history.append({"role": "user", "content": user_input})
                
                response = gen_gemini_response(self.convo_history)
                self.convo_history.append({"role": "AI", "content": response})
                
                return response
            except Exception as e:
                print(f"There's an error generating AI response: {e}")
                return self.give_a_response(user_input)
        else:
            return self.give_a_response(user_input)
            
            