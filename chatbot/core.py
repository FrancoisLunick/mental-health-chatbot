class ChatCore:
    
    def __init__(self):
        self.responses = {
            "sad" : "I'm really sorry to hear that.", 
            "anxious": "Let's take a deep breathe.", 
            "happy": "That's great to hear."
        }
    
    def detect_mood(self, user_input):
        user_input = user_input.lower()
        
        for mood in self.responses:
            if mood in user_input:
                return mood