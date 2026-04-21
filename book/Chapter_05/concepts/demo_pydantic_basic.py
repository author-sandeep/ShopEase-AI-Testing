# SPDX-License-Identifier: MPL-2.0
# Concept 2: Declarative Schemas with Pydantic - Program 2
# File: demo_pydantic_basic.py
# Purpose: Enforces absolute data integrity at runtime using BaseModel.
# Author: Sandeep Dixit

import os
from pydantic import BaseModel, ValidationError
from typing import Optional

class StrictAIPayload(BaseModel):
    """Pydantic schema enforcing flawless test data instantiation."""
    test_id: str
    user_prompt: str
    temperature: float = 0.0 # Default value logic natively supported
    expected_intent: Optional[str] = None

def run_pydantic_validation() -> None:
    """Demonstrates Pydantic's aggressive type casting and rejection."""
    print("--- Attempting Valid Instantiation ---")
    try:
        # Pydantic will cast the string "0.5" safely to a float 0.5
        valid_payload = StrictAIPayload(
            test_id="TC_001",
            user_prompt="Find shoes.",
            temperature="0.5"
        )
        print(f"Success: {valid_payload.test_id} | Temp: {valid_payload.temperature}")
    except ValidationError as e:
        print(f"Validation Error: {e}")

    print("\n--- Attempting Invalid Instantiation ---")
    try:
        # We pass a pure string to a float field that cannot be cast
        invalid_payload = StrictAIPayload(
            test_id="TC_002",
            user_prompt="Find shirts.",
            temperature="HOT"
        )
        print("This line will never execute.")
    except ValidationError as e:
        print(f"-> PYDANTIC CAUGHT IT: {e.errors()[0]['msg']}")
    except Exception as e:
        print(f"System crash: {e}")
    finally:
        pass

if __name__ == "__main__":
    run_pydantic_validation()