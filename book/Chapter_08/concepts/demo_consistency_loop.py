# SPDX-License-Identifier: MPL-2.0
# Concept 5: Validating Few-Shot Consistency - Program 5
# File: demo_consistency_loop.py
# Purpose: Mathematically proves the stability of a prompt across multiple evaluations.
# Author: Sandeep Dixit

import time
from typing import List, Set

def mock_unstable_ai_execution(iteration: int) -> str:
    """Simulates an LLM that occasionally drifts from the expected format."""
    # Iteration 4 simulates a hallucination drift due to model probability
    if iteration == 4:
        return "SUCCESS." # Notice the unexpected period
    return "SUCCESS"

def test_few_shot_consistency() -> None:
    """The Halo Loop: Executing N iterations to prove absolute stability."""

    total_iterations: int = 5
    execution_results: List[str] = []

    print(f"\n-> Commencing {total_iterations}-Pass Consistency Loop...")

    try:
        for i in range(1, total_iterations + 1):
            # 1. Execute the LLM Call
            print(f"   Executing Pass {i}...")
            raw_response = mock_unstable_ai_execution(i)

            # 2. Defensively normalize the response
            # NOTE: Without .strip(), invisible spaces will cause false consistency failures
            clean_response = raw_response.strip().upper()

            # 3. Store the result
            execution_results.append(clean_response)

            # Simulating minimal delay to prevent rate limits
            time.sleep(0.1)

        # 4. Mathematical Consistency Assertion
        # Converting a list to a Python set automatically removes all duplicate values
        unique_answers: Set[str] = set(execution_results)

        # If the set length is exactly 1, all 5 passes were identical
        assert len(unique_answers) == 1, \
            f"Consistency Fault! AI drifted across iterations. Unique outputs: {unique_answers}"

        # Structural Verification
        expected_output = "SUCCESS"
        assert expected_output in unique_answers, "AI was consistent, but consistently wrong."

        print("-> ASSERTION PASSED: 100% Few-Shot Stability Proven.")

    except AssertionError as ae:
        print(f"-> ASSERTION FAILED: {ae}")
    except Exception as e:
        print(f"System Error: {e}")
    finally:
        pass

if __name__ == "__main__":
    test_few_shot_consistency()