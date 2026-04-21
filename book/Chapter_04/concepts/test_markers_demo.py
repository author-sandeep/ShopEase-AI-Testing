# SPDX-License-Identifier: MPL-2.0
# Concept 4: Pytest Markers and Categorization - Program 4
# File: test_markers_demo.py
# Purpose: Utilizes metadata tags to surgically filter test execution scope.
# Author: Sandeep Dixit

import pytest
import time

# To prevent warnings, these should ideally be registered in pytest.ini
# Example pytest.ini content:
# [pytest]
# markers =
#     smoke: Fast, critical path tests.
#     ai_heavy: Slow tests requiring external API calls.

@pytest.mark.smoke
def test_local_configuration():
    """A lightning-fast test ensuring basic logic is sound."""
    print("Executing SMOKE test: Validating local memory.")
    assert True

@pytest.mark.ai_heavy
def test_deep_llm_reasoning():
    """A slow test that reaches out to external APIs."""
    print("Executing HEAVY test: Establishing remote connection...")
    # Simulating a heavy network call
    time.sleep(1)
    assert True, "Remote LLM reasoning valid."

@pytest.mark.smoke
@pytest.mark.ai_heavy
def test_critical_remote_auth():
    """A test possessing multiple overlapping categories."""
    print("Executing OVERLAPPING test: Remote Authentication.")
    assert True