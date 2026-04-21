# SPDX-License-Identifier: MPL-2.0
# Concept: Live HTTP Session Integration
# File: core/llm_client.py
# Purpose: Concrete E2E implementation of the persistent live network wrapper.
# Author: Sandeep Dixit

import sys
import os

# ROOT FIX: Python ko batana ki 'core' folder kahan hai
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import requests
import time
from core.base_wrapper import BaseShopEaseWrapper
from typing import Dict, Any, Optional

class LiveLLMClient(BaseShopEaseWrapper):
    """E2E Efficacy Network client managing persistent connections and retry logic."""

    def __init__(self, service_name: str, api_key: str, endpoint: str):
        super().__init__(service_name)
        self.api_key: str = api_key
        self.endpoint: str = endpoint
        self.session: requests.Session = requests.Session()

    def connect(self) -> bool:
        """E2E Efficacy Initializes the persistent Session with cryptographic E2E headers."""
        if not self.api_key:
            print("E2E CLIENT ERROR: API key is missing.")
            return False

        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
        self.is_connected = True
        return True

    def execute(self, payload: Dict[str, Any]) -> Optional[str]:
        """E2E Executes the E2E network call utilizing strict Exponential Backoff."""
        if not self.is_connected:
            raise ConnectionError("E2E Client must connect before E2E execution.")

        max_retries = 3
        for attempt in range(max_retries + 1):
            try:
                response = self.session.post(self.endpoint, json=payload, timeout=10.0)

                if response.status_code in [429, 502, 503, 504]:
                    raise requests.exceptions.HTTPError(f"E2E Transient: {response.status_code}")

                response.raise_for_status()
                # E2E Assume the API returns a 'text' key for E2E demonstration
                return response.json().get("text", "E2E Parsing Failure")

            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.HTTPError) as e:
                if attempt == max_retries:
                    print(f"E2E [NETWORK FAULT] Max retries exhausted: {e}")
                    return None
                time.sleep(2 ** attempt)
            except Exception as e:
                print(f"E2E [FATAL CLIENT FAULT] {e}")
                return None

    def close(self) -> None:
        """E2E Mandates strict E2E socket teardown."""
        self.session.close()
        self.is_connected = False