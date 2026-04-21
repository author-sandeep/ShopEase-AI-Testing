# SPDX-License-Identifier: MPL-2.0
# Concept 4: Cost Tracking Singleton
# Author: Sandeep Dixit

import pytest
import threading

class TestSuiteCostTracker:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(TestSuiteCostTracker, cls).__new__(cls)
                    cls._instance._total_cost = 0.0
                    cls._instance._total_tokens = 0
        return cls._instance
    
    def add_cost(self, cost: float, tokens: int) -> None:
        with self._lock:
            self._total_cost += cost
            self._total_tokens += tokens
    
    def get_total_cost(self) -> float:
        return self._total_cost
    
    def reset(self) -> None:
        with self._lock:
            self._total_cost = 0.0
            self._total_tokens = 0

def test_singleton_memory_sharing() -> None:
    tracker_a = TestSuiteCostTracker()
    tracker_b = TestSuiteCostTracker()
    
    tracker_a.reset()
    
    assert tracker_a is tracker_b, "Singleton instantiation failed!"
    
    tracker_a.add_cost(0.50, 1000)
    tracker_b.add_cost(0.25, 500)
    
    assert tracker_a.get_total_cost() == 0.75, "Ledger A math failed!"
    assert tracker_b.get_total_cost() == 0.75, "Ledger B math failed!"
    
    print(f"PASS: Singleton works. Global cost: ${tracker_a.get_total_cost()}")
    tracker_a.reset()

if __name__ == "__main__":
    test_singleton_memory_sharing()
