# SPDX-License-Identifier: MPL-2.0
# Concept 2: Exponential Backoff Strategy
# Author: Sandeep Dixit

import time
import pytest

class RateLimitError(Exception):
    pass

def execute_with_backoff(func, max_retries: int = 3):
    base_delay: int = 1
    
    for attempt in range(max_retries):
        try:
            return func()
        except RateLimitError:
            if attempt == max_retries - 1:
                raise
            wait_time: int = base_delay * (2 ** attempt)
            print(f"Attempt {attempt + 1} failed. Waiting {wait_time}s...")
            time.sleep(wait_time)
    return None

def test_exponential_backoff_timing() -> None:
    failure_count: int = 0
    
    def mock_flaky_api():
        nonlocal failure_count
        failure_count += 1
        if failure_count < 3:
            raise RateLimitError("Too Many Requests")
        return "Success on attempt 3"
    
    result = execute_with_backoff(mock_flaky_api)
    assert result == "Success on attempt 3"
    assert failure_count == 3
    print("PASS: Backoff succeeded.")

if __name__ == "__main__":
    test_exponential_backoff_timing()
