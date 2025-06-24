def load_supportive_messages():
    
    with open("prompts/supportive_messages.txt", "r") as file:
        lines = list(file)
        
        cleaned_lines = [line.strip() for line in lines]
        
    return cleaned_lines

load_supportive_messages()