# SPDX-License-Identifier: MPL-2.0
# Concept 2: Structural Assertions for AI - Program 2
# File: test_structural_assertions.py
# Purpose: Validates probabilistic AI outputs using strict shape and schema constraints.
# Author: Sandeep Dixit

from typing import Dict, Any

def get_mock_ai_recommendation() -> Dict[str, Any]:
    """Simulates an unpredictable but structurally sound AI response."""
    return {
        "intent": "purchase",
        "item_id": 105,
        "reasoning": "The user frequently searches for running gear.",
        "confidence": 0.92
    }

def test_ai_recommendation_structure():
    """Validates the shape of the AI payload, completely ignoring exact text."""

    response = get_mock_ai_recommendation()

    # 1. Type Assertion (Must be a dictionary to prevent frontend crashes)
    assert isinstance(response, dict), "AI failed to return a JSON/Dict payload."

    # 2. Key Existence Assertion (Must contain critical routing data)
    required_keys = {"intent", "item_id", "confidence"}
    for key in required_keys:
        assert key in response, f"CRITICAL: Missing structural key '{key}'"

    # 3. Boundary Assertion (Confidence must be a float and logically sound)
    assert isinstance(response["confidence"], float), "Confidence must be a decimal."
    assert 0.0 <= response["confidence"] <= 1.0, "Confidence mathematically invalid."

    # 4. Containment Assertion (Semantic matching over exact equality)
    assert "running" in response["reasoning"].lower(), "AI missed core user context."