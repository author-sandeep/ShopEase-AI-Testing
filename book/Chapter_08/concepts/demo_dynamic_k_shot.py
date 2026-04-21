# SPDX-License-Identifier: MPL-2.0
# Concept 4: Dynamic Example Injection (K-Shot) - Program 4
# File: demo_dynamic_k_shot.py
# Purpose: Intelligently limits context window bloat by injecting targeted examples.
# Author: Sandeep Dixit

from typing import List, Dict

# The Master Database of Examples (Usually loaded from a JSON file in Production)
MASTER_EXAMPLES: List[Dict[str, str]] = [
    {"category": "refund", "input": "I want my money back.", "output": "REFUND"},
    {"category": "refund", "input": "Cancel this order and credit me.", "output": "REFUND"},
    {"category": "tech", "input": "The app crashed on login.", "output": "BUG"},
    {"category": "tech", "input": "I got an error 500.", "output": "BUG"}
]

def get_k_examples(target_category: str, k: int = 2) -> List[Dict[str, str]]:
    """Filters the master database to return exactly K relevant examples."""
    try:
        # Use list comprehension to filter strictly by the requested category tag
        filtered = [ex for ex in MASTER_EXAMPLES if ex.get("category") == target_category]

        # Slice the list to enforce the K boundary constraint mathematically
        selected_examples = filtered[:k]

        if not selected_examples:
            print(f"[WARNING] No examples found for category: {target_category}. Defaulting to Zero-Shot.")

        return selected_examples
    except Exception as e:
        print(f"Database Filtering Error: {e}")
        return []
    finally:
        pass

if __name__ == "__main__":
    try:
        # Scenario: Pytest is executing a "tech" related test
        test_category = "tech"
        print(f"-> Extracting K=2 examples for category: {test_category}")

        injected_data = get_k_examples(target_category=test_category, k=2)

        print("\n--- INJECTED CONTEXT DATA ---")
        for item in injected_data:
            print(f"INPUT: {item['input']} -> OUTPUT: {item['output']}")

        # Proving the safety net mechanism
        print("\n-> Extracting K=2 for missing category: 'billing'")
        missing_data = get_k_examples("billing", k=2)

    except Exception as e:
        print(f"Execution Error: {e}")