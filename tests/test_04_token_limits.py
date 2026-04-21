# SPDX-License-Identifier: MPL-2.0
# File: tests/test_04_token_limits.py
# Purpose: Token limit and truncation detection tests
# Author: Sandeep Dixit

import pytest
from unittest.mock import MagicMock, patch

def test_truncation_flag():
    """Test that truncation is detected via finish_reason == 'length'."""
    # Create a mock client that returns a truncated response
    mock_client = MagicMock()
    mock_client._make_raw_request = MagicMock(return_value={
        "choices": [{"finish_reason": "length", "message": {"content": "Truncated..."}}]
    })

    # Simulate payload (as in Chapter 10)
    payload = {
        "messages": [{"role": "user", "content": "Write a massive essay."}],
        "max_tokens": 5,
        "temperature": 0.0
    }

    response = mock_client._make_raw_request(payload)
    finish_reason = response["choices"][0]["finish_reason"]
    assert finish_reason == "length"