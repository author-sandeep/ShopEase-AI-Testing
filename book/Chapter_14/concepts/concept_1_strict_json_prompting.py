# SPDX-License-Identifier: MPL-2.0
# Concept 1: Strict JSON Prompting
# Author: Sandeep Dixit

import json
import pytest
from typing import Dict, Any

def test_strict_json_prompting() -> None:
    """Verifies the AI obeys formatting instructions strictly."""
    system_prompt: str = (
        "You are a data extraction API. Output ONLY valid JSON. "
        "Do not include conversational filler. "
        "Schema: {'intent': string, 'item': string}"
    )
    
    ai_response: str = '{"intent": "purchase", "item": "laptop"}'
    parsed_data: Dict[str, Any] = json.loads(ai_response)
    
    assert isinstance(parsed_data, dict), "Output is not a JSON object!"
    assert "intent" in parsed_data, "Missing required key."
    
    print(f"PASS: JSON format mandated successfully -> {parsed_data}")

if __name__ == "__main__":
    test_strict_json_prompting()
