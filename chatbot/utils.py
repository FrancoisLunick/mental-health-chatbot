from datetime import datetime

def clean_text(text):
    text = text.lower()
    text = "".join(text.splitlines())
    
    return text

def log_user_and_bot_chat(user_input, bot_input):
    with open("logs/chat_log.txt", "a") as file:
        file.write(f"User: {user_input}\n")
        file.write(f"Bot: {bot_input}\n\n")
    
def get_timestamp():
    current_datetime = datetime.now()
    
    formatted_timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    return formatted_timestamp