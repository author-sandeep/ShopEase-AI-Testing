# SPDX-License-Identifier: MPL-2.0
# Concept 1: HTTP 429 Error Simulation
# Author: Sandeep Dixit

import pytest

class RateLimitError(Exception):
    pass

def mock_llm_call(payload: dict):
    raise RateLimitError("HTTP 429: Rate limit exceeded.")

def test_simulate_429_error() -> None:
    test_payload: dict = {"prompt": "Buy shoes"}
    
    with pytest.raises(RateLimitError) as exc_info:
        mock_llm_call(test_payload)
    
    assert "HTTP 429" in str(exc_info.value)
    print("PASS: System successfully identified Rate Limit Error.")

if __name__ == "__main__":
    test_simulate_429_error()
