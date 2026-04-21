# SPDX-License-Identifier: MPL-2.0
# File: core/token_manager.py
import tiktoken
import logging

logger = logging.getLogger(__name__)

class TokenManager:
    def __init__(self, model_name: str = "gpt-3.5-turbo") -> None:
        self.model_name = model_name
        try:
            self.encoding = tiktoken.encoding_for_model(self.model_name)
        except KeyError:
            self.encoding = tiktoken.get_encoding("cl100k_base")

    def count_tokens(self, text: str) -> int:
        if not isinstance(text, str):
            raise TypeError("TokenManager requires string input.")
        if not text.strip():
            return 0
        return len(self.encoding.encode(text))