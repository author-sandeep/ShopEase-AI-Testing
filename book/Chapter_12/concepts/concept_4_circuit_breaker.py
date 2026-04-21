# SPDX-License-Identifier: MPL-2.0
# Concept 4: Circuit Breaker Pattern
# Author: Sandeep Dixit

import pytest

class CircuitOpenError(Exception):
    pass

class SimpleCircuitBreaker:
    def __init__(self, failure_threshold: int = 3):
        self.failure_threshold: int = failure_threshold
        self.failures: int = 0
        self.state: str = "CLOSED"
    
    def record_failure(self) -> None:
        self.failures += 1
        if self.failures >= self.failure_threshold:
            self.state = "OPEN"
    
    def check_state(self) -> None:
        if self.state == "OPEN":
            raise CircuitOpenError("Circuit is OPEN. Fast failing.")

def test_circuit_breaker_trips() -> None:
    breaker = SimpleCircuitBreaker(failure_threshold=3)
    
    breaker.record_failure()
    breaker.record_failure()
    breaker.record_failure()
    
    assert breaker.state == "OPEN"
    
    with pytest.raises(CircuitOpenError):
        breaker.check_state()
    
    print("PASS: Circuit Breaker tripped and fast-failed correctly.")

if __name__ == "__main__":
    test_circuit_breaker_trips()
