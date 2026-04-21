# SPDX-License-Identifier: MPL-2.0
# Concept 4: Dictionary Key and Type Validation
# Author: Sandeep Dixit

import pytest
from typing import Dict, Any

def validate_shopease_schema(data: Dict[str, Any]) -> bool:
    contract: Dict[str, type] = {
        "intent": str,
        "confidence": float
    }
    
    for req_key, expected_type in contract.items():
        if req_key not in data:
            raise KeyError(f"Missing required key: '{req_key}'")
        
        actual_value = data[req_key]
        if not isinstance(actual_value, expected_type):
            if expected_type == float and isinstance(actual_value, int):
                continue
            raise TypeError(f"Key '{req_key}' expected {expected_type.__name__}, got {type(actual_value).__name__}")
    
    return True

def test_manual_schema_validation() -> None:
    good_payload: Dict[str, Any] = {"intent": "buy", "confidence": 0.85}
    bad_key_payload: Dict[str, Any] = {"action": "buy", "confidence": 0.85}
    bad_type_payload: Dict[str, Any] = {"intent": "buy", "confidence": "high"}
    
    assert validate_shopease_schema(good_payload) == True
    
    with pytest.raises(KeyError):
        validate_shopease_schema(bad_key_payload)
    
    with pytest.raises(TypeError):
        validate_shopease_schema(bad_type_payload)
    
    print("PASS: Manual schema validation works correctly.")

if __name__ == "__main__":
    test_manual_schema_validation()
