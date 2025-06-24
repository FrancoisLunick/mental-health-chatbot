from pathlib import Path

prompts_dir = Path("resources")

def load_supportive_messages():
    
    filepath = prompts_dir / "supportive_messages.txt"
    
    with open(filepath, "r", encoding="utf-8") as file:
        lines = list(file)
        
        cleaned_lines = [line.strip() for line in lines]
        
    return cleaned_lines