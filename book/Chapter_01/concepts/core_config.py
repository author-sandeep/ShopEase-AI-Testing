# SPDX-License-Identifier: MPL-2.0
# Concept 4: Centralized Configuration - Program 4
# File: core_config.py
# Purpose: Manages framework configuration and secure environment variables.
# Author: Sandeep Dixit

import os
from typing import Optional

class FrameworkConfig:
    """Centralized configuration manager for ShopEase."""

    def __init__(self):
        # Always use getenv with a fallback to prevent hard crashes
        self.test_env: str = os.getenv("TEST_ENV", "LOCAL").strip().upper()
        self.api_timeout: int = int(os.getenv("API_TIMEOUT", "30"))
        self._api_key: Optional[str] = os.getenv("SECRET_API_KEY")

    def get_secure_key(self) -> str:
        """Safely retrieves the API key, stripping dangerous whitespace."""
        try:
            if not self._api_key:
                raise ValueError("CRITICAL: SECRET_API_KEY is not set.")
            return self._api_key.strip()
        except ValueError as e:
            print(f"Configuration Error: {e}")
            return "MISSING_KEY"
        finally:
            pass

if __name__ == "__main__":
    # Simulating environment variables for demonstration
    os.environ["TEST_ENV"] = "STAGING"
    os.environ["SECRET_API_KEY"] = " your_key  "

    try:
        config = FrameworkConfig()
        print(f"Active Test Environment: {config.test_env}")
        print(f"Timeout defined as: {config.api_timeout} seconds")
        # Demonstrating whitespace stripping
        print(f"Sanitized Key: '{config.get_secure_key()}'")
    except Exception as e:
        print(f"Initialization failure: {e}")