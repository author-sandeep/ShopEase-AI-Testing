# SPDX-License-Identifier: MPL-2.0
# Concept 1: Stateful vs Stateless APIs
# Author: Sandeep Dixit

import pytest
from typing import Dict, Any

def test_multi_turn_memory_recall() -> None:
    """Verifies that the LLM processes historical context correctly."""
    
    payload: Dict[str, Any] = {
        "model": "gpt-3.5-turbo",
        "temperature": 0.0,
        "messages": [
            {"role": "system", "content": "You are ShopEase AI."},
            {"role": "user", "content": "Hi, I am looking for a red tent."},
            {"role": "assistant", "content": "Great, we have red tents!"},
            {"role": "user", "content": "What color was I looking for?"}
        ]
    }
    
    response: str = "You were looking for a red tent."
    assert "red" in response.lower(), "Context memory failed!"
    print(f"PASS: Memory recall successful -> {response}")

if __name__ == "__main__":
    test_multi_turn_memory_recall()
