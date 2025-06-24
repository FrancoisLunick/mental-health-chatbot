from chatbot import ChatCore

chat_core = ChatCore()

print("Hey there welcome. Tell me how you are feeling today.\n\n")

while True:
    user_input = input("You: ")
    
    if user_input == "exit" or user_input == "quit":
        break
    else:
        chat_core.chat(user_input)
        print(chat_core.give_a_response(user_input))

print("Have a great day. I'll be here if you ever need me again. Goodbye.")
