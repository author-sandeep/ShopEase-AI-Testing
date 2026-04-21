# SPDX-License-Identifier: MPL-2.0
# Concept 2: Exponential Backoff - Lab Integration
# File: tests/test_08_rate_limits.py
# Purpose: Core testing file for API rate limit resiliency.
# Author: Sandeep Dixit

import pytest
import random

# Custom Exceptions
class RateLimitError(Exception):
    pass

class CircuitOpenError(Exception):
    pass

# Utility Functions
def calculate_delay(attempt: int) -> float:
    base: float = float(1 * (2 ** attempt))
    jitter: float = random.uniform(0.0, 1.0)
    return base + jitter

def extract_header(headers: dict) -> int | None:
    lower_h = {k.lower(): v for k, v in headers.items()}
    if "retry-after" in lower_h:
        try:
            return int(lower_h["retry-after"])
        except ValueError:
            return None
    return None

# Circuit Breaker Class (Properly indented at module level)
class SimpleCircuitBreaker:
    def __init__(self, threshold: int = 3):
        self.threshold: int = threshold
        self.failures: int = 0
        self.state: str = "CLOSED"

    def record_failure(self) -> None:
        self.failures += 1
        if self.failures >= self.threshold:
            self.state = "OPEN"

    def check(self) -> None:
        if self.state == "OPEN":
            raise CircuitOpenError("Circuit is OPEN")

# Test Functions
def test_backoff_math() -> None:
    delay = calculate_delay(2)
    assert delay >= 4.0 and delay <= 5.0

def test_circuit_state_transition() -> None:
    cb = SimpleCircuitBreaker(threshold=2)
    cb.record_failure()
    assert cb.state == "CLOSED"

    cb.record_failure()
    assert cb.state == "OPEN"

    with pytest.raises(CircuitOpenError):
        cb.check()

def test_header_parsing() -> None:
    headers = {"Content-Type": "json", "RETRY-After": "45"}
    assert extract_header(headers) == 45