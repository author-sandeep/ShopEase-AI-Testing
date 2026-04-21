# SPDX-License-Identifier: MPL-2.0
# Concept 2: Structuring Contextual Templates - Program 2
# File: core_prompt_builder.py
# Purpose: A centralized engine for generating flawless Few-Shot matrices.
# Author: Sandeep Dixit

from typing import List, Dict

class PromptTemplateBuilder:
    """Centralizes and mathematically enforces LLM prompt structures."""

    def __init__(self, system_rules: str):
        self.system_rules: str = system_rules.strip()

    def build_few_shot(self, user_query: str, examples: List[Dict[str, str]]) -> str:
        """Dynamically injects examples and queries into an immutable template."""
        try:
            # 1. Start with the immutable System rules
            final_prompt: str = f"SYSTEM: {self.system_rules}\n\n"

            # 2. Safely construct the Examples block
            if examples:
                final_prompt += "--- EXAMPLES START ---\n"
                for idx, ex in enumerate(examples):
                    # Defensive extraction using .get() to prevent KeyErrors
                    inp = ex.get("input", "MISSING_INPUT")
                    out = ex.get("output", "MISSING_OUTPUT")
                    final_prompt += f"INPUT: {inp}\nOUTPUT: {out}\n\n"
                final_prompt += "--- EXAMPLES END ---\n\n"

            # 3. Append the active test execution block
            final_prompt += f"INPUT: {user_query}\nOUTPUT:"

            return final_prompt

        except Exception as e:
            print(f"CRITICAL: Template construction failed - {e}")
            return ""
        finally:
            pass

if __name__ == "__main__":
    # Centralized rules
    rules = "Determine if the user is asking for shipping info. Return YES or NO."

    # Master example set managed centrally
    training_data = [
        {"input": "Where is my box?", "output": "YES"},
        {"input": "I hate this app.", "output": "NO"}
    ]

    try:
        builder = PromptTemplateBuilder(rules)
        test_query = "Can you track my order?"

        # Generation is now a clean, 1-line call in the Pytest script
        perfect_prompt = builder.build_few_shot(test_query, training_data)

        print("--- GENERATED CONTEXTUAL TEMPLATE ---")
        print(perfect_prompt)
    except Exception as e:
        print(f"Execution Error: {e}")