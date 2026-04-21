# SPDX-License-Identifier: MPL-2.0
# Concept: Pytest Architecture and Structural Assertions
# File: tests/test_ai_wrapper.py
# Purpose: Validates the core BaseWrapper interface structurally.
# Author: Sandeep Dixit

import pytest
from core.base_wrapper import BaseShopEaseWrapper

class DummyMockWrapper(BaseShopEaseWrapper):
    """A concrete implementation strictly for unit testing the ABC."""
    def connect(self) -> bool:
        self.is_connected = True
        return True

    def execute(self, payload: dict) -> str:
        return f"Mock received intent: {payload.get('intent', 'none')}"

    def close(self) -> None:
        self.is_connected = False

@pytest.fixture
def mock_wrapper():
    """Injects the test wrapper instantly."""
    wrapper = DummyMockWrapper("MockService")
    wrapper.connect()
    yield wrapper
    wrapper.close()

@pytest.mark.smoke
@pytest.mark.parametrize(
    "test_payload, expected_substring",
    [
        ({"intent": "purchase"}, "Mock received intent: purchase"),
        ({"intent": "support"}, "Mock received intent: support"),
        ({}, "Mock received intent: none")
    ]
)
def test_wrapper_execution_structural(mock_wrapper, test_payload, expected_substring):
    """Surgically tests the execution mechanics via parameterized loops."""
    # Execute through the injected fixture
    response = mock_wrapper.execute(test_payload)

    # 1. Structural Boundary checks
    assert isinstance(response, str), "Wrapper violated the string return contract."

    # 2. Containment Logic check
    assert expected_substring in response, "Wrapper logic translation failed."