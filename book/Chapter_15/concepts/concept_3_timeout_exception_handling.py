# SPDX-License-Identifier: MPL-2.0
# Concept 3: Timeout Exception Handling
# Author: Sandeep Dixit

import pytest
from typing import Dict, Any

class ForcedTimeoutError(Exception):
    pass

def execute_with_fallback(should_timeout: bool) -> Dict[str, Any]:
    try:
        if should_timeout:
            raise ForcedTimeoutError("Connection aborted!")
        return {"status": "success", "data": "shoes"}
    
    except ForcedTimeoutError as te:
        print(f"LOG: Caught timeout safely - {str(te)}")
        return {"status": "timeout", "data": "System busy. Try again."}

def test_graceful_timeout_handling() -> None:
    fallback_response = execute_with_fallback(should_timeout=True)
    
    assert fallback_response["status"] == "timeout", "Fallback status wrong!"
    assert "busy" in fallback_response["data"], "Fallback message wrong!"
    
    print("PASS: System degraded gracefully instead of crashing.")

if __name__ == "__main__":
    test_graceful_timeout_handling()
