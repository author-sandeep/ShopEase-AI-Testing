# SPDX-License-Identifier: MPL-2.0
# Concept 1: API Mocking Principle
# Author: Sandeep Dixit

import pytest
from unittest.mock import MagicMock
from typing import Dict, Any, Callable

def process_ai_response(client_func: Callable) -> str:
    response_data: Dict[str, Any] = client_func()
    return response_data.get("content", "Error")

def test_basic_magic_mock() -> None:
    fake_llm_client = MagicMock()
    fake_llm_client.return_value = {"content": "I am a fake AI response."}
    
    result: str = process_ai_response(fake_llm_client)
    
    assert result == "I am a fake AI response.", "Mock injection failed!"
    fake_llm_client.assert_called_once()
    
    print(f"PASS: Mock successfully bypassed the real logic. Result: {result}")

if __name__ == "__main__":
    test_basic_magic_mock()
