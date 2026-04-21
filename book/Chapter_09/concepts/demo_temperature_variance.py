# SPDX-License-Identifier: MPL-2.0
# Concept 1: The Mathematics of Temperature - Program 1
# File: demo_temperature_variance.py
# Purpose: Proves the mathematical impact of temperature scaling on token generation.
# Author: Sandeep Dixit

import requests
import os
from typing import List, Dict

def test_temperature_impact(prompt: str, temp_value: float) -> str:
    """Executes a prompt utilizing a highly specific temperature constraint."""
    api_key = os.getenv("SHOPEASE_API_KEY", "mock")
    url = "https://httpbin.org/post" # Mock endpoint

    # The temperature parameter is injected directly into the payload
    payload: Dict[str, any] = {
        "model": "shopease-gpt",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temp_value
    }

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5.0)
        response.raise_for_status()

        # Simulating the AI's varied responses based on the temperature parameter
        if temp_value == 0.0:
            return "The product is a red shoe."
        elif temp_value == 1.5:
            return "Behold the crimson footwear of speed!"
        return "UNKNOWN"

    except Exception as e:
        return f"ERROR: {e}"

if __name__ == "__main__":
    test_prompt = "Describe the item."

    print("-> Executing at Temperature 0.0 (Argmax / Deterministic)")
    print(f"Result: {test_temperature_impact(test_prompt, 0.0)}")

    print("\n-> Executing at Temperature 1.5 (High Chaos / Creative)")
    print(f"Result: {test_temperature_impact(test_prompt, 1.5)}")