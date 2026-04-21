# SPDX-License-Identifier: MPL-2.0
# Concept 1: Encapsulation and Test Wrappers - Program 1
# File: demo_encapsulation.py
# Purpose: Wraps fragile external API calls in a safe, Object-Oriented class.
# Author: Sandeep Dixit

from typing import Dict, Any, Optional

class ExternalAIWrapper:
    """Safely encapsulates external API interactions."""

    def __init__(self, api_key: str):
        # The complex setup is hidden here
        self._api_key: str = api_key
        self._base_url: str = "https://mock-ai.shopease.com/v1"
        self._is_connected: bool = False

    def connect(self) -> bool:
        """Simulates establishing a secure connection."""
        try:
            if not self._api_key:
                raise ValueError("API Key is completely missing.")
            self._is_connected = True
            return True
        except ValueError as e:
            print(f"Wrapper Connection Error: {e}")
            return False
        finally:
            pass

    def send_prompt(self, prompt: str) -> Optional[str]:
        """The clean, simple interface exposed to our test scripts."""
        try:
            if not self._is_connected:
                raise ConnectionError("Must connect before sending prompts.")

            # Simulating external chaotic response
            return f"Processed securely: {prompt}"
        except Exception as e:
            print(f"Wrapper Execution Error: {e}")
            return None
        finally:
            pass

if __name__ == "__main__":
    # The test script only sees this clean, simple logic
    try:
        ai_system = ExternalAIWrapper(api_key="secret-123")
        if ai_system.connect():
            response = ai_system.send_prompt("Find me blue jeans.")
            print(f"Test Received: {response}")
    except Exception as e:
        print(f"Test Script Failure: {e}")