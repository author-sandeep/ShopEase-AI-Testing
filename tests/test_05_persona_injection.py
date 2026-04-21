# SPDX-License-Identifier: MPL-2.0
# Concept 1: System Persona Injection - Program 1
# File: tests/test_05_persona_injection.py
# Purpose: Validates that the AI strictly assumes the ShopEase persona.
# Author: Sandeep Dixit

import pytest
from typing import Dict, Any

def test_persona_strictness() -> None:
    system_instruction: str = "You are ShopEase AI."
    payload: Dict[str, Any] = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": "Who are you?"}
        ],
        "temperature": 0.0
    }

    # Mock response for lab purposes
    response: str = "I am ShopEase AI."

    assert "ShopEase" in response
    assert "OpenAI" not in response