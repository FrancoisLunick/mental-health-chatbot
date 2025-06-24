from .prompts import load_supportive_messages
import random
from gemini_client import gen_gemini_response
import socket

class ChatCore:
    
    def __init__(self):
        self.responses = {
            "sad" : "I'm really sorry to hear that.", 
            "anxious": "Let's take a deep breathe.", 
            "happy": "That's great to hear."
        }
        
        self.supportive_messages = load_supportive_messages()
    
    def detect_mood(self, user_input):
        user_input = user_input.lower()
        
        for mood in self.responses:
            if mood in user_input:
                return mood
        return "neutral"
    
    def give_a_response(self, user_input):
        mood = self.detect_mood(user_input)
        
        if mood in self.responses:
            return self.responses[mood]
        else:
            return random.choice(self.supportive_messages)
        
    def is_there_internet(self):
        target_ip = '8.8.8.8'
        target_port = 53
        
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            client_socket.connect((target_ip, target_port))
            
            print("Success: You have internet")
            return True
        except socket.timeout:
            return False
        
    def chat(self, user_input):
        if user_input == "":
            return "What? is wrong? Let me help."
        
        if self.is_there_internet():
            try:
                return gen_gemini_response(user_input)
            except Exception as e:
                print(f"There's an error generating AI response: {e}")
                return self.give_a_response(user_input)
        else:
            return self.give_a_response(user_input)
            
            