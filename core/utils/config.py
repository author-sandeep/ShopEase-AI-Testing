# SPDX-License-Identifier: MPL-2.0
# Concept: Centralized Configuration Management
# File: core/config.py
# Purpose: Singleton configuration manager for ShopEase Framework.
# Author: Sandeep Dixit

import os
from typing import Optional

class FrameworkConfig:
    """Manages all environment variables securely."""

    _instance: Optional['FrameworkConfig'] = None

    def __new__(cls):
        """Implements Singleton pattern to ensure only one config exists."""
        if cls._instance is None:
            cls._instance = super(FrameworkConfig, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Loads environment variables safely."""
        self.test_environment: str = os.getenv("SHOPEASE_ENV", "LOCAL").strip().upper()

        try:
            timeout_str = os.getenv("API_TIMEOUT", "30")
            self.timeout: int = int(timeout_str)
        except ValueError:
            print("WARNING: API_TIMEOUT must be an integer. Defaulting to 30.")
            self.timeout: int = 30

    def get_api_timeout(self) -> int:
        return self.timeout

# Global instance for easy importing
config = FrameworkConfig()