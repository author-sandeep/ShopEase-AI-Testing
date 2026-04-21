# SPDX-License-Identifier: MPL-2.0
# File: tests/conftest.py
# Purpose: Global pytest configuration and fixtures
# Author: Sandeep Dixit

import pytest
from typing import Generator


@pytest.fixture(scope="session", autouse=True)
def global_test_environment() -> Generator[None, None, None]:
    """Global fixture that runs once per test session."""

    print("\n[CONFTEST] Booting ShopEase QA Framework...")

    # Reset any global trackers here
    # DummyGlobalTracker.reset()

    yield  # All tests run here

    print("\n[CONFTEST] Shutting down ShopEase QA Framework...")
    # Print final summary here
    # print(f"Total cost: ${DummyGlobalTracker.total_cost}")