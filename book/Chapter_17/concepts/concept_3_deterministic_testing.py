# SPDX-License-Identifier: MPL-2.0
# Concept 3: Deterministic Testing (Golden Fixtures)
# Author: Sandeep Dixit

import json
import pytest
from unittest.mock import MagicMock
from typing import Dict, Any

def process_checkout_intent(ai_client: MagicMock) -> bool:
    raw_response: str = ai_client()
    data: Dict[str, Any] = json.loads(raw_response)
    return data.get("intent") == "checkout"

def test_deterministic_logic_routing() -> None:
    deterministic_ai_output: str = '{"intent": "checkout", "confidence": 0.99}'
    
    mock_client = MagicMock()
    mock_client.return_value = deterministic_ai_output
    
    routing_success: bool = process_checkout_intent(mock_client)
    
    assert routing_success is True, "Backend failed to route checkout!"
    print("PASS: Deterministic mock guaranteed reliable execution.")

if __name__ == "__main__":
    test_deterministic_logic_routing()
