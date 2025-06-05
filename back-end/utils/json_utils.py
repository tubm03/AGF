import json

def is_valid_json(text):
    try:
        json.loads(text)
        return True
    except json.JSONDecodeError:
        return False
    
def clean_json_response(text):
    if text.strip().startswith("```json"):
        text = text.strip().removeprefix("```json").removesuffix("```").strip()
    return text