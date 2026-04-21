# SPDX-License-Identifier: MPL-2.0
# Concept 3: Parameterized Test Loops - Program 3
# File: test_parameterization.py
# Purpose: Executes a single test logic block against multiple disparate data sets.
# Author: Sandeep Dixit

import pytest
from typing import Optional

def analyze_intent(user_prompt: str) -> Optional[str]:
    """Mock application logic categorizing user input."""
    prompt_lower = user_prompt.lower()
    if "buy" in prompt_lower or "price" in prompt_lower:
        return "purchase_intent"
    elif "help" in prompt_lower or "broken" in prompt_lower:
        return "support_intent"
    return "unknown_intent"

# The decorator defines the variable names, then provides a list of data tuples
@pytest.mark.parametrize(
    "input_prompt, expected_intent",
    [
        ("I want to buy a laptop", "purchase_intent"),
        ("What is the price of this?", "purchase_intent"),
        ("My account is broken, please help", "support_intent"),
        ("Hello, how are you today?", "unknown_intent")
    ]
)
def test_ai_intent_categorization(input_prompt: str, expected_intent: str):
    """A single function executing four highly distinct test scenarios."""

    print(f"\n-> Testing Prompt: '{input_prompt}'")

    actual_intent = analyze_intent(input_prompt)

    assert actual_intent == expected_intent, \
        f"Intent Mismatch! Expected {expected_intent}, got {actual_intent}"