import tiktoken
import usage
from urllib3 import response


# CODING EXERCISES
#
# Q5. Write a Python function calc_cost(prompt, completion) that charges $1 per 1M prompt tokens and $2 per 1M completion tokens.
#
# Q6. Complete the Tiktoken estimation code:
#
# import tiktoken
# def count_tokens(text: str) -> int:
#     encoder = tiktoken.get_encoding("cl100k_base")
#     # return the length of the encoded text
#
# Q7. Debug this Singleton initialization:
#
# class Tracker:
#     _instance = None
#     def __init__(self):
#         if not Tracker._instance:
#             Tracker._instance = self
#
# Why is doing this in __init__ fundamentally flawed for a Singleton?
#
# Q8. Write an assertion that checks if a dictionary usage contains the key "total_tokens".
#
# Q9. Write a try/except block that safely extracts response["usage"]["prompt_tokens"], returning 0 if a KeyError occurs.
#
# Q10. Extend the ShopEase project by writing a function that accepts an input string and a max token limit. If the local Tiktoken estimate exceeds the limit, raise ValueError("Payload too large").
# SOLUTIONS FOR CHAPTER 16



# Q5:
def calc_cost(prompt: int, completion: int) -> float:
    return (prompt / 1_000_000) * 1.0 + (completion / 1_000_000) * 2.0

# Q6:
def count_tokens(text: str) -> int:
    encoder = tiktoken.get_encoding("cl100k_base")
    return len(encoder.encode(text))

# Q7: __init__ is called after memory already allocated; multiple objects still created. Must override __new__.

# Q8:
assert "total_tokens" in usage

# Q9:
try:
    tokens = response["usage"]["prompt_tokens"]
except KeyError:
    tokens = 0

# Q10:
def check_token_limit(text: str, limit: int) -> None:
    import tiktoken
    enc = tiktoken.get_encoding("cl100k_base")
    if len(enc.encode(text)) > limit:
        raise ValueError("Payload too large")