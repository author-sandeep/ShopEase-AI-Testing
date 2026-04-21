# SPDX-License-Identifier: MPL-2.0
# Concept 1 & 3: Deterministic Mocking - Lab Integration
# File: tests/test_13_mocking.py
# Purpose: Proves backend resilience using simulated AI payloads.
# Author: Sandeep Dixit

import pytest
import json
from unittest.mock import MagicMock

def app_json_parser(ai_client: MagicMock) -> dict:
    raw = ai_client()
    return json.loads(raw)

def test_deterministic_parsing() -> None:
    # 1. Create the Golden Fixture
    golden_json = '{"intent": "refund", "amount": 50}'

    # 2. Build and configure the Mock
    mock_llm = MagicMock()
    mock_llm.return_value = golden_json

    # 3. Execute application logic
    parsed_data = app_json_parser(mock_llm)

    # 4. Verify structural logic
    assert parsed_data["intent"] == "refund"
    assert parsed_data["amount"] == 50
    mock_llm.assert_called_once()

class MockTimeout(Exception): pass

def safe_app_caller(ai_client: MagicMock) -> str:
    try:
        return ai_client()
    except MockTimeout:
        return "Graceful Fallback"

def test_catastrophe_simulation() -> None:
    # 1. Build the Disaster Mock
    disaster_llm = MagicMock()

    # 2. Pull the fire alarm
    disaster_llm.side_effect = MockTimeout("Server Destroyed")

    # 3. Execute safety net
    result = safe_app_caller(disaster_llm)

    # 4. Verify survival
    assert result == "Graceful Fallback"
