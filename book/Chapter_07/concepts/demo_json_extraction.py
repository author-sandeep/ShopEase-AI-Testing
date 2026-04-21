# SPDX-License-Identifier: MPL-2.0
# Concept 4: Handling JSON Payload Extraction - Program 4
# File: demo_json_extraction.py
# Purpose: Defensively navigates deeply nested LLM API network responses.
# Author: Sandeep Dixit

from typing import Dict, Any, Optional

def simulate_openai_response() -> Dict[str, Any]:
    """Generates a mock payload mimicking standard LLM API structures."""
    return {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "model": "shopease-gpt",
        "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "Category identified as: REFUND"
                },
                "finish_reason": "stop"
            }
        ]
    }

def safe_extract_ai_content(api_payload: Dict[str, Any]) -> Optional[str]:
    """The defensive extraction architecture."""
    try:
        # Step 1: Ensure choices array exists and is not empty
        choices = api_payload.get("choices", [])
        if not choices or not isinstance(choices, list):
            print("EXTRACTION FAULT: 'choices' key missing or invalid.")
            return None

        # Step 2: Extract the first choice block
        first_choice = choices[0]

        # Step 3: Ensure the message object exists
        message = first_choice.get("message", {})

        # Step 4: Extract the ultimate content safely
        # We use .get() so if 'content' is mysteriously missing, it returns ""
        content: str = message.get("content", "")

        if not content:
            print("EXTRACTION FAULT: 'content' field was completely empty.")
            return None

        return content.strip()

    except (IndexError, KeyError, TypeError) as e:
        print(f"FATAL EXTRACTION CRASH: Unexpected JSON mutation - {e}")
        return None
    finally:
        pass

if __name__ == "__main__":
    print("-> Attempting to extract payload from raw network format...")
    mock_network_data = simulate_openai_response()

    clean_text = safe_extract_ai_content(mock_network_data)
    if clean_text:
        print(f"-> SUCCESS. Extracted raw intelligence: '{clean_text}'")