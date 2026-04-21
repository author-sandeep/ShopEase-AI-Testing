# SPDX-License-Identifier: MPL-2.0
# Concept 4: Catastrophe Simulation (side_effect)
# Author: Sandeep Dixit

import pytest
from unittest.mock import MagicMock
from typing import Dict, Any

class LLMTimeoutError(Exception):
    pass

def resilient_api_caller(mock_network: MagicMock) -> Dict[str, Any]:
    try:
        raw_data: str = mock_network()
        return {"status": "success", "data": raw_data}
    except LLMTimeoutError as te:
        print(f"LOG: Disaster caught - {str(te)}")
        return {"status": "degraded", "fallback": "Human agent routing..."}

def test_catastrophic_failure_recovery() -> None:
    disaster_mock = MagicMock()
    disaster_mock.side_effect = LLMTimeoutError("Simulated Network Blackout")
    
    survival_response: Dict[str, Any] = resilient_api_caller(disaster_mock)
    
    assert survival_response["status"] == "degraded", "Fallback state missed!"
    assert "Human" in survival_response["fallback"], "Wrong fallback action!"
    
    print("PASS: System survived the catastrophe and executed fallback.")

if __name__ == "__main__":
    test_catastrophic_failure_recovery()
