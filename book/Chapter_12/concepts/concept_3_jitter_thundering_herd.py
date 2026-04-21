# SPDX-License-Identifier: MPL-2.0
# Concept 3: Jitter and Thundering Herd Prevention
# Author: Sandeep Dixit

import random
import pytest

def calculate_jittered_delay(attempt: int, base_delay: int = 1) -> float:
    exponential_wait: float = float(base_delay * (2 ** attempt))
    jitter: float = random.uniform(0.0, 1.0)
    return exponential_wait + jitter

def test_jittered_delay_bounds() -> None:
    attempt_number: int = 2
    calculated_delay: float = calculate_jittered_delay(attempt_number)
    
    assert calculated_delay >= 4.0, "Delay is too short!"
    assert calculated_delay <= 5.0, "Jitter exceeded maximum bounds!"
    assert isinstance(calculated_delay, float), "Jitter must be fractional."
    
    print(f"PASS: Jitter applied successfully: {calculated_delay:.3f}s")

if __name__ == "__main__":
    test_jittered_delay_bounds()
