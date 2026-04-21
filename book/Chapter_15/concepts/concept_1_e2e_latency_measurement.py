# SPDX-License-Identifier: MPL-2.0
# Concept 1: End-to-End Latency Measurement
# Author: Sandeep Dixit

import time
import pytest

def simulate_llm_call() -> str:
    time.sleep(1.5)
    return '{"status": "success"}'

def test_api_latency_sla() -> None:
    max_allowed_latency: float = 3.0
    
    start_time: float = time.perf_counter()
    response: str = simulate_llm_call()
    end_time: float = time.perf_counter()
    
    duration: float = end_time - start_time
    
    assert duration < max_allowed_latency, f"SLA Breach! Took {duration:.2f}s"
    print(f"PASS: API latency is {duration:.2f}s (Limit: {max_allowed_latency}s)")

if __name__ == "__main__":
    test_api_latency_sla()
