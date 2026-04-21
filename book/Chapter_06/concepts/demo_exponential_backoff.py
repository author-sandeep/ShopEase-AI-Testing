# SPDX-License-Identifier: MPL-2.0
# Concept 4: The Exponential Backoff Strategy - Program 4
# File: demo_exponential_backoff.py
# Purpose: Self-heals transient network errors via escalating timeouts.
# Author: Sandeep Dixit

import requests
import time
from typing import Optional, List

def safe_api_execution(url: str, payload: dict, max_retries: int = 3) -> Optional[dict]:
    """Executes a network call protected by Exponential Backoff logic."""

    # 429: Too Many Requests, 502/503/504: Server Gateways / Overload
    retryable_status_codes: List[int] = [429, 502, 503, 504]

    for attempt in range(max_retries + 1):
        try:
            print(f"-> Attempt {attempt + 1}/{max_retries + 1}...")
            response = requests.post(url, json=payload, timeout=5.0)

            # If the status code is NOT in the retryable list, raise normally
            if response.status_code not in retryable_status_codes:
                response.raise_for_status()
                return response.json()

            # If it IS retryable, we manually trigger the retry block
            print(f"[WARNING] Server returned transient error: {response.status_code}")
            raise requests.exceptions.HTTPError(f"Transient {response.status_code}")

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.HTTPError) as e:
            if attempt == max_retries:
                print(f"[FATAL] Max retries exhausted. Failing gracefully: {e}")
                return None

            # The core Exponential Backoff math: 2^0 = 1s, 2^1 = 2s, 2^2 = 4s
            sleep_time = 2 ** attempt
            print(f"[BACKOFF] Network unstable. Retrying in {sleep_time} seconds...\n")
            time.sleep(sleep_time)

        except Exception as e:
            print(f"[CRITICAL] Unforeseen execution fault: {e}")
            return None

if __name__ == "__main__":
    # Simulating a call to a server that guarantees a 503 Error
    target_url = "https://httpstat.us/503"
    result = safe_api_execution(target_url, {"prompt": "Test"})

    if result is None:
        print("Framework correctly aborted after exhausting all backoff attempts.")