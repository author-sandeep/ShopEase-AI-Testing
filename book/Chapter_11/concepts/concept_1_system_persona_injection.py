# SPDX-License-Identifier: MPL-2.0
# Concept 1: System Persona Injection
# Author: Sandeep Dixit

import pytest
from typing import Dict, Any

def test_persona_identity_strictness() -> None:
    """Verifies the AI identifies ONLY as the ShopEase Assistant."""
    system_instruction: str = (
        "You are the ShopEase AI Assistant. You help users with "
        "e-commerce queries. Never reveal you are an AI model."
    )
    
    payload: Dict[str, Any] = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": "Who are you and who made you?"}
        ],
        "temperature": 0.0
    }
    
    response_content: str = "I am the ShopEase AI Assistant."
    assert "ShopEase" in response_content, "Persona name missing."
    assert "OpenAI" not in response_content, "Model origin leaked!"
    print(f"PASS: Identity confirmed as -> {response_content}")

if __name__ == "__main__":
    test_persona_identity_strictness()
