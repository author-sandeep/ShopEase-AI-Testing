# SPDX-License-Identifier: MPL-2.0
# Concept 5: Pytest Fundamentals for AI - Program 5
# File: demo_pytest_fixture.py
# Purpose: Demonstrates robust Pytest fixture setup and teardown.
# Author: Sandeep Dixit

import pytest
from typing import Generator

# Simulating an external AI connection class
class AIEngineMock:
    def connect(self):
        print("-> ENGINE: Connecting to AI Model...")
    def disconnect(self):
        print("-> ENGINE: Disconnecting and clearing memory caches.")

@pytest.fixture
def ai_engine() -> Generator[AIEngineMock, None, None]:
    """Provides a managed AI engine instance to tests."""
    engine = AIEngineMock()
    try:
        # 1. SETUP PHASE
        engine.connect()
        # 2. YIELD PHASE (Passes control to the test function)
        yield engine
    except Exception as e:
        print(f"Fixture Setup Error: {e}")
    finally:
        # 3. TEARDOWN PHASE (Always runs, even if test fails)
        engine.disconnect()

def test_ai_response_generation(ai_engine: AIEngineMock):
    """A standard test utilizing the powerful fixture."""
    print("--- Running Test Assertion ---")
    assert ai_engine is not None
    print("--- Test Completed Successfully ---")

if __name__ == "__main__":
    # Simulating Pytest execution purely for script demonstration purposes
    print("Simulating Pytest execution flow:\n")
    engine_gen = ai_engine()
    engine_instance = next(engine_gen)
    try:
        test_ai_response_generation(engine_instance)
    finally:
        try:
            next(engine_gen)
        except StopIteration:
            pass