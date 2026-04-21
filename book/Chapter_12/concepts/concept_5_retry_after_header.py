# SPDX-License-Identifier: MPL-2.0
# Concept 5: Header-Based Retry Extraction
# Author: Sandeep Dixit

import pytest
from typing import Dict, Optional

def extract_retry_after(headers: Dict[str, str]) -> Optional[int]:
    lower_headers = {k.lower(): v for k, v in headers.items()}
    
    if "retry-after" in lower_headers:
        try:
            return int(lower_headers["retry-after"])
        except ValueError:
            return None
    return None

def test_retry_after_parsing() -> None:
    headers_clean: Dict[str, str] = {"Retry-After": "15", "Content-Type": "json"}
    headers_missing: Dict[str, str] = {"Content-Type": "json"}
    headers_bad: Dict[str, str] = {"retry-after": "Wait a minute"}
    
    assert extract_retry_after(headers_clean) == 15
    assert extract_retry_after(headers_missing) is None
    assert extract_retry_after(headers_bad) is None
    
    print("PASS: Header extraction logic successfully validated.")

if __name__ == "__main__":
    test_retry_after_parsing()
