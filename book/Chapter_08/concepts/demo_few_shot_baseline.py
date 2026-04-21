# SPDX-License-Identifier: MPL-2.0
# Concept 1: The Few-Shot Paradigm - Program 1
# File: demo_few_shot_baseline.py
# Purpose: Demonstrates the power of pattern-matching via explicit examples.
# Author: Sandeep Dixit

from typing import Dict, Any

def generate_few_shot_prompt(user_query: str) -> str:
    """Constructs a rigid prompt template containing K=2 examples."""

    # The examples act as an unshakeable template for the AI to mimic
    prompt_template = f"""
    SYSTEM: You are the ShopEase intent routing engine.
    Classify the user intent strictly. Do not use conversational filler.
    
    --- EXAMPLES START ---
    INPUT: "I need to return my shoes."
    OUTPUT: RETURN
    
    INPUT: "How much is this laptop?"
    OUTPUT: PRICE_INQUIRY
    --- EXAMPLES END ---
    
    INPUT: "{user_query}"
    OUTPUT:
    """
    return prompt_template.strip()

def mock_llm_execution(prompt: str) -> str:
    """Simulates an AI that flawlessly mimics the provided pattern."""
    if "where is my package" in prompt.lower():
        # The AI perfectly copies the exact formatting of the examples
        return "TRACKING"
    return "UNKNOWN"

if __name__ == "__main__":
    try:
        query: str = "Where is my package?"
        final_prompt: str = generate_few_shot_prompt(query)

        print("-> Transmitting Few-Shot Prompt to AI...")
        print(f"--- Payload Preview ---\n{final_prompt}\n-----------------------")

        # The E2E execution
        ai_response: str = mock_llm_execution(final_prompt)
        print(f"\n-> AI Response: {ai_response}")

        # Exact string assertion is now safe because the pattern is locked
        assert ai_response == "TRACKING", "AI deviated from the Few-Shot pattern."
        print("-> SUCCESS: Strict pattern consistency achieved.")

    except AssertionError as ae:
        print(f"Test Failed: {ae}")
    except Exception as e:
        print(f"System Error: {e}")
    finally:
        pass