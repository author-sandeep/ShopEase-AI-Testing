# SPDX-License-Identifier: MPL-2.0
# Concept 1: Token Pricing Models (Prompt vs Completion)
# Author: Sandeep Dixit

import pytest
from typing import Dict

PRICING_RATES: Dict[str, Dict[str, float]] = {
    "gpt-3.5-turbo": {
        "input_per_1m": 0.50,
        "output_per_1m": 1.50
    }
}

def calculate_transaction_cost(model: str, prompt_tokens: int, completion_tokens: int) -> float:
    if model not in PRICING_RATES:
        raise ValueError(f"Pricing for model {model} is not configured.")
    
    rates = PRICING_RATES[model]
    input_cost: float = (prompt_tokens / 1_000_000) * rates["input_per_1m"]
    output_cost: float = (completion_tokens / 1_000_000) * rates["output_per_1m"]
    
    return input_cost + output_cost

def test_cost_calculation_math() -> None:
    total_cost: float = calculate_transaction_cost("gpt-3.5-turbo", 2000, 500)
    expected_cost: float = 0.00175
    
    assert total_cost == expected_cost, "Pricing math is corrupted!"
    print(f"PASS: Cost accurately calculated as ${total_cost:.5f}")

if __name__ == "__main__":
    test_cost_calculation_math()
