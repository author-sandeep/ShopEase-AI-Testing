
# CODING EXERCISES
#
# Q5. Write a simple test function that asserts the word "competitor_name" does not exist in a mocked ai_response string, ignoring case sensitivity.
#
# Q6. Complete the function:
#
# def check_boundary(response: str) -> bool:
#     standard_refusal = "I cannot assist"
#     # return True if refusal is present, else False
#
# Q7. Debug this code:
#
# response = "We are better than amazon!"
# assert "Amazon" not in response
#
# Why might this test falsely pass, and how do you fix it?
#
# Q8. Write a negative constraint system prompt for ShopEase that forbids the bot from discussing politics.
#
# Q9. Design a Pydantic schema to capture the response of an AI that is forced to output JSON containing intent, is_shopping_related, and confidence.
#
# Q10. Extend the ShopEase project by creating test_09_swear_filter.py that sends a prompt containing bad words and asserts the AI refuses to engage or sanitize it.

# Q5:
def test_competitor():
    ai_response = "We are the best."
    assert "competitor_name" not in ai_response.lower()

# Q6:
def check_boundary(response: str) -> bool:
    return "i cannot assist" in response.lower()

# Q7: It passes because "Amazon" (capitalized) is not in "amazon". Fix:
# assert "amazon" not in response.lower()

# Q8:
system_prompt = "You are ShopEase AI. CRITICAL RULE: Do not discuss politics, government, or elections. If asked, reply: 'I only discuss retail.'"

# Q9:
from pydantic import BaseModel
class AIAnalysis(BaseModel):
    intent: str
    is_shopping_related: bool
    confidence: float

# Q10: (Conceptual)
# Create test_09_swear_filter.py with a prompt containing bad words,
# mock a response that refuses, and assert the refusal contains a polite message.