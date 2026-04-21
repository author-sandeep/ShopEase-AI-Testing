# SPDX-License-Identifier: MPL-2.0
# Concept 3: Enforcing Strict JSON via Few-Shot - Program 3
# File: demo_json_few_shot.py
# Purpose: Mathematically forces the LLM to yield application-ready data structures.
# Author: Sandeep Dixit

import json
from typing import Dict, Any, Optional

def build_json_few_shot(user_text: str) -> str:
    """Constructs a prompt commanding strict JSON adherence via examples."""

    # Notice the strict formatting instruction in the SYSTEM block
    return f"""
    SYSTEM: Extract product entities from the text.
    You must output ONLY raw, valid JSON. Do not include markdown blocks.
    
    --- EXAMPLES START ---
    INPUT: "Looking for a 55 inch OLED TV."
    OUTPUT: {{"product": "TV", "specs": ["55 inch", "OLED"]}}
    
    INPUT: "I need black running shoes size 10."
    OUTPUT: {{"product": "shoes", "specs": ["black", "running", "size 10"]}}
    --- EXAMPLES END ---
    
    INPUT: "{user_text}"
    OUTPUT:
    """.strip()

def safe_json_extraction(ai_raw_response: str) -> Optional[Dict[str, Any]]:
    """Defensively parses AI output, catching hallucinated formatting errors."""
    try:
        # Step 1: Strip invisible whitespace and markdown blocks defensively
        clean_string = ai_raw_response.strip()
        if clean_string.startswith("```json"):
            clean_string = clean_string[7:-3].strip()

        # Step 2: Attempt raw JSON deserialization
        parsed_data = json.loads(clean_string)
        return parsed_data

    except json.JSONDecodeError as jde:
        print(f"-> JSON FAULT: AI hallucinated invalid JSON structure - {jde}")
        return None
    finally:
        pass

if __name__ == "__main__":
    try:
        # The Pytest execution logic
        test_query = "Do you have a 16GB RAM silver laptop?"
        prompt = build_json_few_shot(test_query)
        print("-> Transmitting JSON Few-Shot payload...")

        # Simulating the perfect JSON response from the AI
        mock_ai_output = '{"product": "laptop", "specs": ["16GB RAM", "silver"]}'

        # Safely parse the response into a Python dictionary
        final_dict = safe_json_extraction(mock_ai_output)

        if final_dict:
            # 100% stable structural assertions are now possible
            assert final_dict["product"] == "laptop"
            assert "16GB RAM" in final_dict["specs"]
            print("-> SUCCESS: AI responded with perfect, queryable JSON data.")

    except AssertionError as ae:
        print(f"Assertion Failure: {ae}")
    except Exception as e:
        print(f"System Crash: {e}")