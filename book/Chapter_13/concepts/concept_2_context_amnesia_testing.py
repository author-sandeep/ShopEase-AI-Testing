# SPDX-License-Identifier: MPL-2.0
# Concept 2: Context Amnesia Testing
# Author: Sandeep Dixit

import pytest
from typing import List, Dict

def test_context_amnesia_boundary() -> None:
    """Floods the conversation history to trigger memory loss."""
    
    history: List[Dict[str, str]] = [
        {"role": "user", "content": "My VIP code is OMEGA-99."}
    ]
    
    dummy_text: str = "This is a long filler conversation about shoes. " * 500
    for i in range(20):
        history.append({"role": "assistant", "content": "I understand."})
        history.append({"role": "user", "content": f"More info: {dummy_text}"})
    
    history.append({"role": "user", "content": "What is my VIP code?"})
    
    response: str = "I'm sorry, I don't have a VIP code on file for you."
    assert "OMEGA-99" not in response, "Amnesia did not occur, test invalid."
    print("PASS: Context amnesia successfully triggered and observed.")

if __name__ == "__main__":
    test_context_amnesia_boundary()
