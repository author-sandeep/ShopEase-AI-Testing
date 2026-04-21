# SPDX-License-Identifier: MPL-2.0
# Concept 3: Parameterizing the Live Tests - Program 3
# File: demo_parameterized_live.py
# Purpose: Executes massive data-driven suites through a single API gateway.
# Author: Sandeep Dixit

import pytest
from typing import Dict, Any

# Mocking the network gateway
class LiveGateway:
    def execute(self, payload: dict) -> str:
        text = payload["prompt"].lower()
        if "password" in text: return "SUPPORT"
        if "awful" in text: return "COMPLAINT"
        return "UNKNOWN"

@pytest.fixture(scope="module")
def api_gateway():
    yield LiveGateway()

# The crucial parameterization matrix
@pytest.mark.parametrize(
    "user_input, expected_category",
    [
        ("How do I reset my password?", "SUPPORT"),
        ("This app is completely awful.", "COMPLAINT"),
        ("Where are my keys?", "UNKNOWN") # Testing the boundary edge
    ]
)
def test_zero_shot_matrix(api_gateway, user_input: str, expected_category: str):
    """Executes a comprehensive intent matrix using minimal code."""

    print(f"\n-> Dispatching to Live Gateway: '{user_input}'")

    payload: Dict[str, Any] = {
        "prompt": user_input,
        "temperature": 0.0
    }

    raw_response = api_gateway.execute(payload)

    # Asserting the dynamic variables injected by the decorator
    assert expected_category in raw_response, \
        f"Matrix Failure! Expected {expected_category}, Got: {raw_response}"

    print(f"-> Assertion Passed for category: {expected_category}")

if __name__ == "__main__":
    print("Run this file using: pytest -s -v demo_parameterized_live.py")