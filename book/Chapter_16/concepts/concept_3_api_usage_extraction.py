# SPDX-License-Identifier: MPL-2.0
# Concept 3: API Usage Metric Extraction
# Author: Sandeep Dixit

import pytest
from typing import Dict, Any

def extract_api_usage(api_response: Dict[str, Any]) -> Dict[str, int]:
    fallback_metrics: Dict[str, int] = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0
    }
    
    usage_data = api_response.get("usage")
    
    if not usage_data:
        print("WARNING: Usage block missing. Fallback metrics applied.")
        return fallback_metrics
    
    try:
        return {
            "prompt_tokens": int(usage_data.get("prompt_tokens", 0)),
            "completion_tokens": int(usage_data.get("completion_tokens", 0)),
            "total_tokens": int(usage_data.get("total_tokens", 0))
        }
    except (ValueError, TypeError):
        return fallback_metrics

def test_usage_metric_extraction() -> None:
    mock_api_response: Dict[str, Any] = {
        "choices": [{"message": {"content": "Hello"}}],
        "usage": {
            "prompt_tokens": 25,
            "completion_tokens": 10,
            "total_tokens": 35
        }
    }
    
    metrics: Dict[str, int] = extract_api_usage(mock_api_response)
    
    assert metrics["prompt_tokens"] == 25, "Prompt extraction failed!"
    assert metrics["total_tokens"] == 35, "Total extraction failed!"
    
    print(f"PASS: Usage safely extracted -> {metrics}")

if __name__ == "__main__":
    test_usage_metric_extraction()
