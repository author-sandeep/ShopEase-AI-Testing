# SPDX-License-Identifier: MPL-2.0
# Concept 5: Fixture Scopes and Dependency Injection - Program 5
# File: test_dependency_injection.py
# Purpose: Centralizes heavy framework instantiation using strictly scoped fixtures.
# Author: Sandeep Dixit

import pytest
from typing import Generator

# Simulating the Engine from Chapter 3
class HeavyExecutionEngine:
    def __init__(self):
        self.status = "Engine Initialized securely."
    def run(self, payload: str) -> str:
        return f"[PROCESSED] {payload}"
    def shutdown(self):
        print("\n-> Engine Shutdown Sequence Complete.")

# 1. The Provider (The Fixture)
# scope="module" means this setup runs exactly ONCE for this entire Python file,
# not once per test. This drastically saves memory and time.
@pytest.fixture(scope="module")
def shopease_engine() -> Generator[HeavyExecutionEngine, None, None]:
    """Injects a centralized execution engine into test functions."""
    print("\n[SETUP] Spinning up Heavy AI Execution Engine...")
    engine = HeavyExecutionEngine()

    # Pause execution and hand the object to the test
    yield engine

    # Teardown guarantees execution after all tests in the module finish
    print("\n[TEARDOWN] Releasing Heavy AI resources...")
    engine.shutdown()

# 2. The Consumer (The Test)
# By naming the parameter 'shopease_engine', Pytest handles the injection invisibly.
def test_basic_prompt_execution(shopease_engine: HeavyExecutionEngine):
    """Test 1 requests the engine."""
    print("Executing Test 1...")
    response = shopease_engine.run("Hello AI")
    assert "PROCESSED" in response

def test_complex_prompt_execution(shopease_engine: HeavyExecutionEngine):
    """Test 2 requests the exact same engine object from memory."""
    print("Executing Test 2...")
    response = shopease_engine.run("Generate Report")
    assert response.startswith("[PROCESSED]")