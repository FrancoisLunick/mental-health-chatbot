from pathlib import Path

prompts_dir = Path("prompts")

def load_supportive_messages():
    
    filepath = prompts_dir / "supportive_messages.txt"
    
    with open(filepath, "r") as file:
        lines = list(file)
        
        cleaned_lines = [line.strip() for line in lines]
        
    return cleaned_lines

load_supportive_messages()