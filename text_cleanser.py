import re

def clean_text(text):
    # Remove all non-alphabetic characters and digits (except spaces)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove excessive spaces (replace multiple spaces with one space)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Correct weird spacings like "W hat" → "what" and "O f" → "of"
    text = re.sub(r'\bW\s*hat\b', 'what', text)
    text = re.sub(r'\bO\s*f\b', 'of', text)
    
    # Convert all uppercase words to lowercase
    #text = text.lower()
    
    return text

def cleanse_file(input_filepath, output_filepath):
    with open(input_filepath, 'r', encoding='utf-8') as file:
        text = file.read()

    # Clean the text
    cleaned_text = clean_text(text)

    # Save the cleaned text to a new file
    with open(output_filepath, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print(f"File cleaned successfully and saved to {output_filepath}")

#Usage:
cleanse_file('chirstinedepizan.txt', 'cleansedpizan.txt')
