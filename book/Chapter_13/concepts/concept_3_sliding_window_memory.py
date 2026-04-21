# SPDX-License-Identifier: MPL-2.0
# Concept 3: Sliding Window Memory Strategy
# Author: Sandeep Dixit

import pytest
from typing import List, Dict

def apply_sliding_window(
    system_prompt: Dict[str, str],
    history: List[Dict[str, str]],
    window_size: int = 4
) -> List[Dict[str, str]]:
    trimmed_history = history[-window_size:] if history else []
    return [system_prompt] + trimmed_history

def test_sliding_window_preservation() -> None:
    sys_prompt = {"role": "system", "content": "I am ShopEase."}
    
    chat_log = [
        {"role": "user", "content": "Msg 1: Too old"},
        {"role": "assistant", "content": "Msg 2: Too old"},
        {"role": "user", "content": "Msg 3: Keep"},
        {"role": "assistant", "content": "Msg 4: Keep"},
        {"role": "user", "content": "Msg 5: Keep"},
        {"role": "assistant", "content": "Msg 6: Keep"},
    ]
    
    final_payload = apply_sliding_window(sys_prompt, chat_log, window_size=4)
    
    assert final_payload[0]["role"] == "system", "System prompt lost!"
    assert len(final_payload) == 5, f"Expected 5, got {len(final_payload)}"
    assert "Too old" not in final_payload[1]["content"], "FIFO logic failed!"
    
    print("PASS: Sliding window maintained perfect structural integrity.")

if __name__ == "__main__":
    test_sliding_window_preservation()
