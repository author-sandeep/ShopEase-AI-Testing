# SPDX-License-Identifier: MPL-2.0
# Concept 2: Writing the First E2E LLM Test - Program 2
# File: demo_first_e2e.py
# Purpose: The architectural template for testing LLM logic via Pytest.
# Author: Sandeep Dixit

import pytest
from typing import Dict, Any

# Simulating the dependencies from our Core directory
class MockLLMClient:
    def connect(self): return True
    def execute(self, payload: dict) -> str:
        prompt = payload.get("prompt", "")
        if "buy" in prompt.lower():
            return "Intent Category: PURCHASE"
        return "UNKNOWN"
    def close(self): pass

# 1. The Setup: Injecting the client
@pytest.fixture(scope="module")
def llm_client():
    print("\n[FIXTURE] Initializing Live LLM Client...")
    client = MockLLMClient()
    client.connect()
    yield client
    print("\n[FIXTURE] Closing Live LLM Client...")
    client.close()

# 2. The Execution: The Pytest Node
def test_zero_shot_purchase_intent(llm_client):
    """E2E Test verifying the AI's ability to classify purchase intents."""

    print("\nExecuting E2E Zero-Shot Test...")

    # 3. Data Integrity: Simulating the Pydantic Schema instantiation
    test_payload: Dict[str, Any] = {
        "test_id": "TC_ZSHOT_001",
        "prompt": "I want to buy the new ShopEase headphones.",
        "temperature": 0.0
    }

    # 4. Network Transmission
    raw_response = llm_client.execute(test_payload)
    print(f"AI Raw Response: '{raw_response}'")

    # 5. The Assertion Logic
    # We defensively format the string to prevent flaky failures
    formatted_response = raw_response.strip().lower()

    # We use containment ('in') rather than strict equality ('==')
    assert "purchase" in formatted_response, \
        f"AI Failed to classify intent. Raw output: {raw_response}"

    print("Assertion Passed: Intent successfully identified.")

# Simulating Pytest running the file
if __name__ == "__main__":
    print("Run this file using: pytest -s demo_first_e2e.py")