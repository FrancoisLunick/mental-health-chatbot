from datetime import datetime

def clean_text(text):
    text = text.lower()
    text = "".join(text.splitlines())
    
    return text

clean_user_text = clean_text("testing\n text\n")

print(clean_user_text)

def log_user_and_bot_chat(user_input, bot_input):
    with open("logs/chat_log.txt", "a") as file:
        file.write(f"User: {user_input}\n")
        file.write(f"Bot: {bot_input}\n\n")
    
def get_timestamp():
    current_datetime = datetime.now()
    
    print(f"The current date time is: {current_datetime}")
    
    formatted_timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    print(formatted_timestamp)
    
    return formatted_timestamp
    

get_timestamp()

def load_supportive_messages():
    
    with open("prompts/supportive_messages.txt", "r") as file:
        lines = list(file)
        
        cleaned_lines = [line.strip() for line in lines]
        
    return cleaned_lines

load_supportive_messages()