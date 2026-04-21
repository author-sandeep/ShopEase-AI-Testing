# SPDX-License-Identifier: MPL-2.0
# Concept 3: Frequency and Presence Penalties - Program 3
# File: demo_penalties.py
# Purpose: Mathematically disrupts AI repetition loops using token penalization.
# Author: Sandeep Dixit

from typing import Dict, Any

def execute_penalized_generation(prompt: str, freq_pen: float, pres_pen: float) -> str:
    """Constructs a payload with strict repetition guardrails."""

    payload: Dict[str, Any] = {
        "model": "shopease-gpt",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5,
        "frequency_penalty": freq_pen, # Penalizes repetitive word counts
        "presence_penalty": pres_pen   # Penalizes hovering on old topics
    }

    print(f"-> Executing | Freq: {freq_pen} | Pres: {pres_pen}")

    try:
        # Simulating the AI execution and loop disruption
        if freq_pen == 0.0 and pres_pen == 0.0:
            return "Buy shoes. Shoes are good. Good shoes are shoes." # Infinite loop simulation
        elif freq_pen > 0.5:
            return "Purchase our footwear. It provides excellent comfort." # Diversified output
        return "UNKNOWN"

    except Exception as e:
        return f"CRITICAL FAULT: {e}"
    finally:
        pass

if __name__ == "__main__":
    test_prompt = "Write a quick ad for our shoes."

    print("--- Test: No Penalties (Risk of Looping) ---")
    print(f"Output: {execute_penalized_generation(test_prompt, 0.0, 0.0)}")

    print("\n--- Test: Strict Penalties (Forced Diversity) ---")
    print(f"Output: {execute_penalized_generation(test_prompt, 1.0, 1.0)}")