from chatbot.core import ChatCore

chat_core = ChatCore()

print("Hey there welcome. \n\n")

user_input = input("Tell me how you are feeling today. \n")

while True:
    user_input = input("You: ")
    
    if user_input == "exit" or user_input == "quit":
        break
    else:
        chat_core.chat(user_input)
        print(chat_core.give_a_response())

print("Have a great day. I'll be here if you ever need me again. Goodbye.")
