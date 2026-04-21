# SPDX-License-Identifier: MPL-2.0
# Concept 2: Global Configuration (conftest.py)
# Author: Sandeep Dixit

import pytest
from typing import Generator

class DummyGlobalTracker:
    total_cost: float = 0.0
    
    @classmethod
    def reset(cls) -> None:
        cls.total_cost = 0.0
    
    @classmethod
    def add(cls, amount: float) -> None:
        cls.total_cost += amount

@pytest.fixture(scope="session", autouse=True)
def global_framework_setup() -> Generator[None, None, None]:
    print("\n[GLOBAL SETUP] Initializing ShopEase QA Framework...")
    DummyGlobalTracker.reset()
    print("[GLOBAL SETUP] Financial ledgers zeroed. Ready for testing.")
    
    yield
    
    print("\n[GLOBAL TEARDOWN] Suite execution complete.")
    print(f"[GLOBAL TEARDOWN] Total Phase 2 API Cost: ${DummyGlobalTracker.total_cost:.5f}")

def test_global_setup_works() -> None:
    DummyGlobalTracker.add(0.10)
    assert DummyGlobalTracker.total_cost == 0.10
    print("PASS: Global setup fixture is working correctly.")

if __name__ == "__main__":
    test_global_setup_works()
