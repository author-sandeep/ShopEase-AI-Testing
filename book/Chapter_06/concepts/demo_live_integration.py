# SPDX-License-Identifier: MPL-2.0
# Concept 1: Live API Integration - Program 1
# File: demo_live_integration.py
# Purpose: Establishes a basic, raw HTTP POST connection to a live endpoint.
# Author: Sandeep Dixit

import requests
from typing import Dict, Any, Optional

# FIX: Naam change kar diya gaya hai (test_ hata diya) taaki PyCharm confuse na ho.
def execute_live_connection(endpoint_url: str, test_payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Transmits data to a live server and extracts the JSON response."""
    print(f"-> Transmitting payload to {endpoint_url}...")
    try:
        # The timeout parameter is mathematically mandatory for test stability
        response: requests.Response = requests.post(
            url=endpoint_url,
            json=test_payload,
            timeout=10.0
        )

        # Raise an HTTPError if the status code is 4xx or 5xx
        response.raise_for_status()

        # Attempt to parse the raw network bytes into a Python dictionary
        data: Dict[str, Any] = response.json()
        print("-> SUCCESS: Live connection verified. Data received.")
        return data

    except requests.exceptions.ConnectionError as ce:
        print(f"Network Failure (No Internet / DNS Issue): {ce}")
        return None
    except requests.exceptions.HTTPError as he:
        print(f"Server Rejected Request (Bad Auth / Formatting): {he}")
        return None
    except requests.exceptions.Timeout as te:
        print(f"Latency Failure (Server took > 10s): {te}")
        return None
    except Exception as e:
        print(f"Unknown Fatal Exception: {e}")
        return None
    finally:
        pass

if __name__ == "__main__":
    # We use a public mock API for safe demonstration purposes
    target_url: str = "https://jsonplaceholder.typicode.com/posts"
    safe_payload: Dict[str, Any] = {"title": "ShopEase Test", "body": "Ping", "userId": 1}

    # FIX: Yahan par bhi naya naam update kar diya hai
    result = execute_live_connection(target_url, safe_payload)
    if result:
        print(f"Extracted API Response ID: {result.get('id')}")