# SPDX-License-Identifier: MPL-2.0
# Concept 5: Financial Assertions (Budget Limits)
# Author: Sandeep Dixit

import pytest

class FinancialBreachError(Exception):
    pass

class SimpleTracker:
    def __init__(self):
        self.cost = 0.0
    
    def add(self, amount: float):
        self.cost += amount
    
    def get(self):
        return self.cost
    
    def reset(self):
        self.cost = 0.0

def execute_expensive_test(tracker, loops: int) -> None:
    max_budget: float = 0.50
    
    for i in range(loops):
        tracker.add(0.15)
        current_cost = tracker.get()
        
        if current_cost > max_budget:
            raise FinancialBreachError(f"ABORT! Cost ${current_cost:.2f} exceeded ${max_budget:.2f}")
        
        print(f"Loop {i+1} complete. Total: ${current_cost:.2f}")

def test_financial_budget_enforcement() -> None:
    tracker = SimpleTracker()
    tracker.reset()
    
    with pytest.raises(FinancialBreachError) as exc_info:
        execute_expensive_test(tracker, loops=10)
    
    assert "ABORT" in str(exc_info.value)
    assert tracker.get() == 0.60, "Math alignment failed!"
    
    print("PASS: Financial breach successfully intercepted and aborted.")

if __name__ == "__main__":
    test_financial_budget_enforcement()
