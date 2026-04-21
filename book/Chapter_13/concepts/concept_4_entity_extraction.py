# SPDX-License-Identifier: MPL-2.0
# Concept 4: Entity Extraction and Summarization
# Author: Sandeep Dixit

import json
import pytest
from typing import Dict

def inject_memory_state(base_system: str, extracted_json: str) -> str:
    try:
        entities = json.loads(extracted_json)
        state_string = ", ".join([f"{k}: {v}" for k, v in entities.items()])
        return f"{base_system} Memory State: [{state_string}]"
    except json.JSONDecodeError:
        return base_system

def test_entity_state_injection() -> None:
    base_prompt = "You are ShopEase AI."
    mock_extraction_output = '{"user_name": "Alice", "cart_item": "Red Boots"}'
    
    updated_system = inject_memory_state(base_prompt, mock_extraction_output)
    
    assert "Alice" in updated_system, "Entity Name lost!"
    assert "Red Boots" in updated_system, "Entity Item lost!"
    assert updated_system.startswith("You are"), "Base prompt corrupted!"
    
    print(f"PASS: Memory state injected correctly -> {updated_system}")

if __name__ == "__main__":
    test_entity_state_injection()
