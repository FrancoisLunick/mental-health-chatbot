"""
This is the main script where the mental health chatbot will run.
The script initializes the chatbot core and also handles the conversation loop with the user.
"""
from chatbot import ChatCore

# Initialize the bot's core functionality
chat_core = ChatCore()

# Prints the welcome message
print("Hey there welcome. Tell me how you are feeling today.\n\n")

# Starts the loop to interact with the user
while True:
    user_input = input("You: ")
    
    if user_input == "exit" or user_input == "quit":
        # Breaks the look if the user types "exit" or "quit"
        break
    else:
        # Process the input from the user and print the bot's response
        chat_core.chat(user_input)
        print(chat_core.give_a_response(user_input))

# Prints a closing message when the user ends the chat
print("Have a great day. I'll be here if you ever need me again. Goodbye.")
