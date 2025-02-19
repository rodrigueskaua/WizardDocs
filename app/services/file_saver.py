import json
import os

DATA_DIR = "pdf-data"

def save_text_to_json(filename: str, text: str) -> str:
    """Salva o texto extraído em um arquivo JSON."""
    os.makedirs(DATA_DIR, exist_ok=True)
    filepath = f"{DATA_DIR}/{filename}.json"
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump({"filename": filename, "text": text}, f, ensure_ascii=False, indent=4)
    
    return filepath
