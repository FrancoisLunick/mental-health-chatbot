"""
This module handles loading pre-written messages from a text file.
"""

from pathlib import Path

# Define the dir where the supportive message file is.
prompts_dir = Path("resources")

def load_supportive_messages():
    """
    Loads supportive messages from a file.

    Returns:
        _type_: A list of cleaned supportive messages.
    """
    
    # Build the full path to the file
    filepath = prompts_dir / "supportive_messages.txt"
    
    # Open the file and read all lines.
    with open(filepath, "r", encoding="utf-8") as file:
        lines = list(file)
        
        cleaned_lines = [line.strip() for line in lines]
    
    # Return the list of messages    
    return cleaned_lines