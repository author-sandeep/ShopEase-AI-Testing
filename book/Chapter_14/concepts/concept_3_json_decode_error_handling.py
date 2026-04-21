# SPDX-License-Identifier: MPL-2.0
# Concept 3: JSONDecodeError Graceful Handling
# Author: Sandeep Dixit

import json
import pytest
from typing import Dict, Any

def safe_json_parse(raw_string: str) -> Dict[str, Any]:
    try:
        return json.loads(raw_string)
    except json.JSONDecodeError as e:
        print(f"LOG: Parsing failed due to syntax - {str(e)}")
        return {"status": "error", "message": "unparseable"}
    except TypeError as e:
        print(f"LOG: Parsing failed due to bad type - {str(e)}")
        return {"status": "error", "message": "invalid_input"}

def test_graceful_error_handling() -> None:
    broken_payload: str = '{intent: purchase, item: "laptop"'
    
    result: Dict[str, Any] = safe_json_parse(broken_payload)
    
    assert "error" in result["status"], "Failed to trigger fallback state!"
    assert result["message"] == "unparseable", "Wrong fallback returned."
    
    print("PASS: System survived broken JSON and returned safe fallback.")

if __name__ == "__main__":
    test_graceful_error_handling()
