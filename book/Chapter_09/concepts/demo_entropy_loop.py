# SPDX-License-Identifier: MPL-2.0
# Concept 4: Stress-Testing Determinism - Program 4
# File: demo_entropy_loop.py
# Purpose: Scientifically maps the exact failure threshold of a system prompt.
# Author: Sandeep Dixit

import json
from typing import Dict, Any

def mock_entropy_execution(temp: float) -> str:
    """Simulates AI breakdown at higher temperatures."""
    if temp < 0.6:
        return '{"status": "SUCCESS"}' # Clean JSON
    elif temp < 1.0:
        return '{"status": "SUCCESS", }' # Trailing comma hallucination
    else:
        return 'The status is SUCCESS!!!' # Total structural collapse

def test_entropy_boundaries() -> None:
    """The Pytest node incrementally increasing mathematical pressure."""

    print("\n-> Initiating Entropy Loop Stress Test...")
    current_temp: float = 0.0
    step_size: float = 0.2
    max_temp: float = 1.0

    try:
        while current_temp <= max_temp:
            print(f"   [TESTING] Heat Level: {current_temp:.1f}...")

            raw_output = mock_entropy_execution(current_temp)

            try:
                # The structural assertion trap
                parsed_data = json.loads(raw_output)
                assert "status" in parsed_data

            except (json.JSONDecodeError, AssertionError) as e:
                print(f"-> [SHATTERED] Prompt structural integrity failed at Temp {current_temp:.1f}")
                print(f"   Failure Reason: {e}")
                print(f"   Final Entropy Score: {(current_temp - step_size):.1f}")
                return # We successfully found the breaking point, exit the test safely

            current_temp += step_size

        print(f"-> [INDESTRUCTIBLE] Prompt survived maximum entropy {max_temp:.1f}")

    except Exception as e:
        print(f"Framework crash: {e}")
    finally:
        pass

if __name__ == "__main__":
    test_entropy_boundaries()