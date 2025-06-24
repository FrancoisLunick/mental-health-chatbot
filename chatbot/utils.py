def clean_text(text):
    text = text.lower()
    text = "".join(text.split())
    
    return text

clean_user_text = clean_text("testing text")

print(clean_user_text)

def log_user_and_bot_chat(user_input, bot_input):
    with open("logs/chat_log.txt", "a") as file:
        file.write(f"User: {user_input}\n")
        file.write(f"Bot: {bot_input}\n\n")
    
    file.close