# SPDX-License-Identifier: MPL-2.0
# Concept 2: Local Token Estimation (Tiktoken)
# Author: Sandeep Dixit

import pytest
import tiktoken

def estimate_tokens(text: str, model_name: str = "gpt-3.5-turbo") -> int:
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    
    token_array: list[int] = encoding.encode(text)
    return len(token_array)

def test_tiktoken_estimation_accuracy() -> None:
    sample_text: str = "Welcome to ShopEase! We love automated testing."
    
    token_count: int = estimate_tokens(sample_text)
    
    assert token_count >= 7, "Token count impossibly low!"
    assert token_count <= 15, "Token count impossibly high!"
    
    print(f"PASS: String '{sample_text}' consumes exactly {token_count} tokens.")

if __name__ == "__main__":
    test_tiktoken_estimation_accuracy()
