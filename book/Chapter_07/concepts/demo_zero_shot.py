# SPDX-License-Identifier: MPL-2.0
# Concept 1: The Zero-Shot Paradigm - Program 1
# File: demo_zero_shot.py
# Purpose: Demonstrates drafting rigid instructions for unguided AI execution.
# Author: Sandeep Dixit

import requests
import os
from typing import Optional

def execute_zero_shot(user_text: str) -> Optional[str]:
    """Sends a Zero-Shot prompt asking for strict classification."""

    # Notice the aggressive, highly explicit formatting instruction
    prompt = f"""
    You are an intent classification system for ShopEase.
    Analyze the following user text.
    Classify it into EXACTLY ONE of these categories: [PURCHASE, SUPPORT, COMPLAINT]
    Return ONLY the category name. Do not include any other text, punctuation, or apologies.
    
    User Text: '{user_text}'
    """

    # Simulating connection via our Chapter 6 architecture principles
    api_key = os.getenv("SHOPEASE_API_KEY", "mock-key")
    url = "https://httpbin.org/post" # Using httpbin to simulate a live endpoint
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"data": prompt}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=5.0)
        response.raise_for_status()

        # Simulating extracting the AI text. In a real endpoint, this would be
        # response.json()['choices'][0]['message']['content']
        return "SUPPORT" # Simulating the AI's perfect compliance

    except requests.exceptions.RequestException as e:
        print(f"Network Failure: {e}")
        return None

if __name__ == "__main__":
    test_input = "My laptop arrived with a cracked screen."
    print(f"User Input: {test_input}")

    ai_response = execute_zero_shot(test_input)
    print(f"AI Zero-Shot Classification: {ai_response}")