# SPDX-License-Identifier: MPL-2.0
# Concept 1: Memory & State - Lab Integration
# File: tests/test_09_memory.py
# Purpose: Core testing suite for context amnesia and sliding windows.
# Author: Sandeep Dixit

import pytest
import json

def test_payload_structure() -> None:
    history = [
        {"role": "system", "content": "You are ShopEase."},
        {"role": "user", "content": "Hi"},
        {"role": "assistant", "content": "Hello"},
        {"role": "user", "content": "Help"}
    ]

    assert history[0]["role"] == "system"
    assert history[-1]["role"] == "user"
    assert len(history) == 4

def apply_window(sys_prompt: dict, logs: list, size: int) -> list:
    trimmed = logs[-size:] if logs else []
    return [sys_prompt] + trimmed

def test_sliding_window_execution() -> None:
    sys_msg = {"role": "system", "content": "Rules"}
    chat = [
        {"role": "user", "content": "1"},
        {"role": "assistant", "content": "2"},
        {"role": "user", "content": "3"},
        {"role": "assistant", "content": "4"}
    ]

    # Apply a window size of 2
    result = apply_window(sys_msg, chat, size=2)

    assert len(result) == 3 # 1 System + 2 Chat
    assert result[0] == sys_msg
    assert result[1]["content"] == "3"
    assert result[2]["content"] == "4"
def merge_state(system: str, json_state: str) -> str:
    try:
        data = json.loads(json_state)
        state_str = ", ".join([f"{k}:{v}" for k,v in data.items()])
        return f"{system} | STATE: {state_str}"
    except Exception:
        return system

def test_state_merge() -> None:
    base = "I am an AI."
    state = '{"vip": true}'
    merged = merge_state(base, state)

    assert "vip:True" in merged or "vip:true" in merged.lower()
    assert merged.startswith("I am an AI.")