# SPDX-License-Identifier: MPL-2.0
# Concept 5: Pydantic Schema Enforcement
# Author: Sandeep Dixit

import pytest
from pydantic import BaseModel, ValidationError

class AIResponseSchema(BaseModel):
    intent: str
    confidence: float
    is_actionable: bool

def test_pydantic_json_enforcement() -> None:
    raw_good_json: str = '{"intent": "buy", "confidence": 0.99, "is_actionable": true}'
    raw_bad_json: str = '{"intent": "buy", "confidence": "high"}'
    
    obj = AIResponseSchema.model_validate_json(raw_good_json)
    assert obj.intent == "buy", "Object mapping failed!"
    
    with pytest.raises(ValidationError) as exc_info:
        AIResponseSchema.model_validate_json(raw_bad_json)
    
    error_details = str(exc_info.value)
    assert "is_actionable" in error_details, "Failed to flag missing key!"
    assert "confidence" in error_details, "Failed to flag type mismatch!"
    
    print("PASS: Pydantic successfully intercepted the bad schema.")

if __name__ == "__main__":
    test_pydantic_json_enforcement()
