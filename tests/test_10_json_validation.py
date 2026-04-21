# SPDX-License-Identifier: MPL-2.0
# Concept 2 & 3: Extractor Utility - Lab Integration
# File: tests/test_10_json_validation.py
# Purpose: Core logical suite for stripping and validation.
# Author: Sandeep Dixit

import json
import pytest
from pydantic import BaseModel, ValidationError


# ============================================
# PART 1: Markdown Stripping Utility
# ============================================

def clean_and_extract_algorithm(raw_ai_text: str) -> dict | None:
    cleaned = raw_ai_text.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]

    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return None


def test_cleaning_logic() -> None:
    dirty = '```json\n{"bot": "ready"}\n```'
    result = clean_and_extract_algorithm(dirty)

    assert result is not None
    assert result["bot"] == "ready"
    print("PASS: Cleaning logic works perfectly!")


# ============================================
# PART 2: Pydantic Schema Validation
# ============================================

class ShopEaseActionSchema(BaseModel):
    action_type: str
    target_item: str
    confidence: float


def test_schema_enforcement_logic() -> None:
    # Clean raw JSON string
    clean_string = '{"action_type": "refund", "target_item": "shoes", "confidence": 0.9}'

    # Action: Validate
    action_obj = ShopEaseActionSchema.model_validate_json(clean_string)

    assert action_obj.action_type == "refund"
    print("PASS: Schema enforcement works!")


def test_hallucination_catch_logic() -> None:
    # Missing action_type, wrong type for confidence
    bad_string = '{"target_item": "shoes", "confidence": "high"}'

    try:
        ShopEaseActionSchema.model_validate_json(bad_string)
        pytest.fail("Error not thrown")
    except ValidationError as error_msg:
        error_details = str(error_msg)
        assert "action_type" in error_details
        assert "confidence" in error_details
        print("PASS: Hallucination caught successfully!")