# SPDX-License-Identifier: MPL-2.0
# Concept 1: The Peril of Untyped Data - Program 1
# File: demo_weak_dataclass.py
# Purpose: Demonstrates how standard Python type hinting fails at runtime.
# Author: Sandeep Dixit

from dataclasses import dataclass
from typing import Optional

@dataclass
class WeakAIPayload:
    """A standard dataclass that suggests types but does not enforce them."""
    test_id: str
    user_prompt: str
    temperature: float

def execute_flawed_logic() -> None:
    """Executes code proving the weakness of standard type hints."""
    try:
        # We explicitly violate the type hints (int instead of str/float)
        # Python will not stop this natively at runtime!
        bad_payload = WeakAIPayload(
            test_id=123,
            user_prompt=["Find", "Shoes"],
            temperature="Hot"
        )
        print("-> DANGER: Weak Dataclass accepted entirely invalid data types!")
        print(f"Payload created: {bad_payload}")
    except TypeError as e:
        print(f"Safe: Type Error caught: {e}")
    except Exception as e:
        print(f"Unknown framework crash: {e}")
    finally:
        pass

if __name__ == "__main__":
    execute_flawed_logic()