# SPDX-License-Identifier: MPL-2.0
# Concept 2: Top-P (Nucleus Sampling) - Program 2
# File: demo_top_p_sampling.py
# Purpose: Enforces creative safety limits using probability mass constraints.
# Author: Sandeep Dixit

import requests
from typing import Dict, Any

def execute_nucleus_sampling(prompt: str, p_value: float) -> str:
    """Executes an AI call with a strict Top-P boundary applied."""

    payload: Dict[str, Any] = {
        "model": "shopease-gpt",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 1.0, # High creativity enabled
        "top_p": p_value    # Mathematical safety net applied
    }

    print(f"-> Executing Payload | Temp: 1.0 | Top-P: {p_value}")

    try:
        # Simulating the network execution layer
        if p_value == 1.0:
            return "The shoes are fantastic, fast, squishy, xylophone!" # Gibberish at 1.0
        elif p_value == 0.1:
            return "The shoes are very comfortable." # Logical, bounded at 0.1
        return "UNKNOWN"

    except Exception as e:
        return f"FAULT: {e}"
    finally:
        pass

if __name__ == "__main__":
    prompt = "Describe these running shoes creatively."

    print("--- Test: No Guardrails ---")
    print(f"Response: {execute_nucleus_sampling(prompt, 1.0)}")

    print("\n--- Test: Strict Top-P Guardrails ---")
    print(f"Response: {execute_nucleus_sampling(prompt, 0.1)}")