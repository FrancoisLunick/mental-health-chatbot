def clean_text(text):
    text = text.lower()
    text = "".join(text.split())
    
    return text

clean_user_text = clean_text("testing text")

print(clean_user_text)