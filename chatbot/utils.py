"""
This Module contains utility functions that are used across the entire Mental Health Chatbot application.
"""

from datetime import datetime

def clean_text(text):
    """
    Convert text to lowercase and remove all line breaks.
    
    Args:
        text (_type_): The input string from the user.

    Returns:
        _type_: A cleaned, single line lowercase string.
    """
    text = text.lower()
    
    # Removes line breaks
    text = "".join(text.splitlines())
    
    return text

def log_user_and_bot_chat(user_input, bot_input):
    """
    Append a user and bot interaction to the chat log file.

    Args:
        user_input (_type_): Message sent by the user
        bot_input (_type_): Response generated by the bot
    """
    
    # Open the log file in append mode and write out the conversation
    with open("logs/chat_log.txt", "a") as file:
        file.write(f"User: {user_input}\n")
        file.write(f"Bot: {bot_input}\n\n")
    
def get_timestamp():
    """
    Get the current date and time in a formatted string.

    Returns:
        str: Current timestamp in the format of "YYYY-MM-DD HH:MM:SS"
    """
    
    current_datetime = datetime.now()
    formatted_timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_timestamp