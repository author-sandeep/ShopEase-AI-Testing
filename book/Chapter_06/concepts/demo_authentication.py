# SPDX-License-Identifier: MPL-2.0
# Concept 2: Bearer Token Authentication - Program 2
# File: demo_authentication.py
# Purpose: Secures external API calls by correctly injecting cryptographic headers.
# Author: Sandeep Dixit

import requests
import os
from typing import Dict, Any

def execute_authenticated_request(prompt: str) -> bool:
    """Injects secure headers and transmits a payload to a mocked secured endpoint."""

    # Simulating the extraction from our Chapter 1 Config Singleton
    api_key: str = os.getenv("SHOPEASE_API_KEY", "mock-secret-key").strip()

    if not api_key:
        print("CRITICAL: Cannot execute API. Authentication token is missing.")
        return False

    # The exact architectural standard for API authentication headers
    secure_headers: Dict[str, str] = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    test_payload: Dict[str, str] = {
        "model": "shopease-v1",
        "messages": prompt
    }

    print("-> Headers constructed securely. Executing request...")
    try:
        # Passing the secure_headers dictionary into the request
        response = requests.post(
            url="https://httpbin.org/bearer", # A safe testing endpoint
            headers=secure_headers,
            json=test_payload,
            timeout=5.0
        )

        # 401 = Unauthorized (Bad Token), 403 = Forbidden (Bad Scope)
        if response.status_code == 401:
            print("Authentication Failed: The provided Bearer token is invalid.")
            return False

        response.raise_for_status()
        print("-> SUCCESS: Server validated the Bearer token and accepted the payload.")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Network Transaction Failed: {e}")
        return False
    finally:
        pass

if __name__ == "__main__":
    # Simulating environment setup
    os.environ["SHOPEASE_API_KEY"] = "sk-778899aabbcc"

    is_successful = execute_authenticated_request("Hello, Secure AI.")
    print(f"Test Pass Status: {is_successful}")