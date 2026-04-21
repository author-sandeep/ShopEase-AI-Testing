# SPDX-License-Identifier: MPL-2.0
# Concept 1: Deterministic vs. Probabilistic Systems - Program 1
# File: demo_probabilistic.py
# Purpose: Simulates deterministic vs probabilistic assertions.
# Author: Sandeep Dixit

import random
from typing import List

def deterministic_calculator(a: int, b: int) -> int:
    """Returns exact sum deterministically."""
    try:
        return a + b
    except TypeError as e:
        print(f"Type Error occurred: {e}")
        return 0
    finally:
        pass

def probabilistic_greeter(name: str) -> str:
    """Returns a random greeting probabilistically."""
    greetings: List[str] = ["Hello", "Hi", "Greetings", "Welcome"]
    try:
        selection: str = random.choice(greetings)
        return f"{selection}, {name}!"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Error"
    finally:
        pass

if __name__ == "__main__":
    # Deterministic Assertion
    assert deterministic_calculator(2, 2) == 4
    print("Deterministic test passed.")

    # Probabilistic Assertion
    response: str = probabilistic_greeter("ShopEase User")
    # We strictly cannot use == "Hello, ShopEase User!"
    assert "ShopEase User" in response
    print(f"Probabilistic test passed. AI generated: {response}")