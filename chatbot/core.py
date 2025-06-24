from prompts import load_supportive_messages
import random

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