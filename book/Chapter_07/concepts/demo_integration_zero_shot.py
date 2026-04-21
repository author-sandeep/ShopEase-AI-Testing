# SPDX-License-Identifier: MPL-2.0
# Concept 5: Integrating Zero-Shot Logic - Program 5
# File: demo_integration_zero_shot.py
# Purpose: The final architectural unification of all framework concepts.
# Author: Sandeep Dixit

import pytest
from pydantic import BaseModel, Field

# 1. Simulating the Core Framework Imports (Chapter 5 & 6)
class StrictPayload(BaseModel):
    test_id: str
    prompt: str = Field(min_length=10)
    temperature: float = 0.0

class UnifiedClient:
    def execute(self, payload_obj: StrictPayload) -> str:
        # Pydantic guarantees this object is structurally flawless
        print(f">> Core Gateway transmitting: {payload_obj.test_id}")
        if "refund" in payload_obj.prompt.lower():
            return "Intent: REFUND_REQUEST"
        return "UNKNOWN"

# 2. Pytest Setup (Chapter 4)
@pytest.fixture(scope="module")
def unified_client():
    yield UnifiedClient()

# 3. Data-Driven Execution (Chapter 4)
@pytest.mark.parametrize(
    "tracker_id, raw_prompt, expected_intent",
    [
        ("TC_01", "I need a refund for my order immediately.", "refund"),
        ("TC_02", "When will my refund be processed?", "refund")
    ]
)
def test_zero_shot_intent(unified_client, tracker_id: str, raw_prompt: str, expected_intent: str):
    """The Ultimate Unification: Schema -> Execution -> Assertion"""

    print(f"\n--- Executing Test {tracker_id} ---")

    # Step A: Data Integrity Firewall (Fails fast locally if bad)
    secure_payload = StrictPayload(
        test_id=tracker_id,
        prompt=raw_prompt,
        temperature=0.0
    )

    # Step B: Secure Network Transmission
    response_string = unified_client.execute(secure_payload)

    # Step C: Defensive Formatting and Assertion
    formatted_response = response_string.strip().lower()

    assert expected_intent in formatted_response, \
        f"Assertion Fault: AI missed intent. Received: '{response_string}'"

    print(f"--- PASSED: {tracker_id} successfully mapped to {expected_intent} ---")

if __name__ == "__main__":
    print("Execute via terminal: pytest -s demo_integration_zero_shot.py")