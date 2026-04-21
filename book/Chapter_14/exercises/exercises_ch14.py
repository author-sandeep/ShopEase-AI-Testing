# THEORETICAL EXERCISES
#
# Q1. Why is telling an AI to "Output JSON" often insufficient without a schema template in the prompt?
#
# Q2. Explain why an AI outputting markdown backticks causes standard parsers to crash.
#
# Q3. What is "Conversational Bleed" and how does it break data extraction?
#
# Q4. Why is a Schema Model superior to a manual loop checking dictionary keys?
#
# CODING EXERCISES
#
# Q5. Write a Python try/except block that catches a JSONDecodeError and prints a syntax error message.
#
# Q6. Complete the function to validate a required dictionary key:
#
# def check_required_key(data: dict, key: str) -> bool:
# # return True if the key exists, otherwise raise a KeyError
#
# Q7. Debug this logic:
#
# data = json.loads('{"age": 25}')
# user = UserSchema.model_validate_json(data)
#
# Why does this crash with a validation error?
#
# Q8. Write a one-line string slice that removes the first 3 characters and the last 3 characters from a variable text.
#
# Q9. Write an assertion verifying that a parsed variable is strictly a floating-point number.
#
# Q10. Extend the ShopEase project by writing a Python function that accepts a string, strips markdown, attempts Pydantic validation, and returns None if an error occurs.
# SOLUTIONS FOR CHAPTER 14



# Q5:
import json
try:
    json.loads(text)
except json.JSONDecodeError:
    print("Syntax Error")

# Q6:
def check_required_key(data: dict, key: str) -> bool:
    if key not in data:
        raise KeyError
    return True

# Q7: model_validate_json expects a raw string, not a dict. Use model_validate(data).

# Q8:
stripped = text[3:-3]

# Q9:
assert isinstance(score, float)

# Q10:
from pydantic import ValidationError
def safe_extract(text: str, model):
    cleaned = text.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    try:
        return model.model_validate_json(cleaned)
    except (ValidationError, json.JSONDecodeError):
        return None