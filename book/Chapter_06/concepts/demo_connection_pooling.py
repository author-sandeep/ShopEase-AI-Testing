# SPDX-License-Identifier: MPL-2.0
# Concept 3: HTTP Connection Pooling - Program 3
# File: demo_connection_pooling.py
# Purpose: Drastically accelerates API E2E Efficacy testing via persistent sockets.
# Author: Sandeep Dixit

import requests
import time
from typing import List

class PersistentAIClient:
    """A highly optimized network client utilizing Session pooling."""

    def __init__(self, api_key: str):
        # 1. Instantiate the persistent Session object
        self.session: requests.Session = requests.Session()

        # 2. Attach headers globally to the session.
        # They will automatically inject into EVERY request.
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "ShopEase-Test-Framework/1.0"
        })
        self.target_url = "https://httpbin.org/post"

    def execute_batch(self, prompts: List[str]) -> None:
        """Executes multiple tests over a single TCP connection."""
        print("-> Initiating persistent high-speed execution batch...")
        try:
            for index, prompt in enumerate(prompts):
                start_time = time.perf_counter()

                # Using the session object, not the raw requests module
                response = self.session.post(
                    url=self.target_url,
                    json={"data": prompt},
                    timeout=5.0
                )
                response.raise_for_status()

                duration = (time.perf_counter() - start_time) * 1000
                print(f"Prompt {index+1} processed in {duration:.2f} ms")

        except requests.exceptions.RequestException as e:
            print(f"Batch Execution Interrupted: {e}")
        finally:
            pass

    def close(self) -> None:
        """Mandatory architectural teardown of the persistent sockets."""
        self.session.close()
        print("-> Connection pool destroyed safely.")

if __name__ == "__main__":
    test_prompts = ["Test 1", "Test 2", "Test 3"]
    client = PersistentAIClient(api_key="mock-key-123")

    try:
        # Notice the speed difference locally if testing against real servers
        client.execute_batch(test_prompts)
    finally:
        client.close()