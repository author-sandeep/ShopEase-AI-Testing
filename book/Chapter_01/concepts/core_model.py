# SPDX-License-Identifier: MPL-2.0
# Concept 3: The ShopEase Core Architecture - Program 3
# File: core_model.py
# Purpose: Foundational data structure for AI payloads.
# Author: Sandeep Dixit

from dataclasses import dataclass
from typing import Optional

@dataclass
class AITestPayload:
    """Secure blueprint for all ShopEase AI test requests."""
    test_id: str
    user_prompt: str
    expected_intent: str
    temperature: float = 0.0
    context: Optional[str] = None

def generate_payload(test_id: str, prompt: str) -> AITestPayload:
    """Safely generates an AI test payload."""
    try:
        payload = AITestPayload(
            test_id=test_id,
            user_prompt=prompt,
            expected_intent="search_product"
        )
        return payload
    except TypeError as e:
        print(f"Data mapping error: {e}")
        # Return a safe fallback or raise depending on framework strictness
        raise
    finally:
        pass

if __name__ == "__main__":
    try:
        sample_payload = generate_payload("TC_001", "Find me red shoes.")
        print(f"Successfully generated Test Payload: {sample_payload.test_id}")
        print(f"Prompt Data: {sample_payload.user_prompt}")
    except Exception as e:
        print(f"System failure: {e}")