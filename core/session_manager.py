# SPDX-License-Identifier: MPL-2.0
# Concept 5: The Sliding Window Strategy - Program 5
# File: core/session_manager.py
# Purpose: Maintains chat history within strict token boundaries.
# Author: Sandeep Dixit

import logging
from typing import List, Dict
from core.token_manager import TokenManager

logger = logging.getLogger(__name__)

class SessionManager:
    """Manages chat history and implements sliding window truncation."""

    def __init__(self, max_tokens: int = 3000):
        self.history: List[Dict[str, str]] = []
        self.max_tokens = max_tokens
        self.token_manager = TokenManager()

    def add_message(self, role: str, content: str) -> None:
        """Adds a message and strictly enforces the sliding window."""
        self.history.append({"role": role, "content": content})
        self._enforce_window()

    def _get_total_tokens(self) -> int:
        """Calculates token weight of the entire history."""
        full_text = " ".join([msg["content"] for msg in self.history])
        return self.token_manager.count_tokens(full_text)

    def _enforce_window(self) -> None:
        """
        Removes oldest messages (index 1) until within limits.
        Index 0 is protected assuming it is the System Prompt.
        """
        while self._get_total_tokens() > self.max_tokens and len(self.history) > 1:
            dropped_msg = self.history.pop(1)
            logger.info(f"Sliding Window: Dropped oldest message to save space.")

if __name__ == "__main__":
    session = SessionManager(max_tokens=20)
    session.add_message("system", "You are ShopEase AI.")
    session.add_message("user", "Hello, I want to buy shoes.")
    session.add_message("assistant", "Sure, what kind of shoes?")
    session.add_message("user", "Red running shoes size 10 please.")

    print(f"Final History Size: {len(session.history)} messages.")