# SPDX-License-Identifier: MPL-2.0
# Concept: Stress-Testing Determinism (The Entropy Loop)
# File: tests/test_03_temperature.py
# Purpose: Scientifically discovers the failure threshold of an AI system prompt.
# Author: Sandeep Dixit

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import json
from core.llm_client import LiveLLMClient
from core.schemas import ShopEaseAIPayload

@pytest.fixture(scope="module")
def shopease_client():
    api_key = os.getenv("SHOPEASE_API_KEY", "mock-fail-key")
    url = "https://jsonplaceholder.typicode.com/posts" # Mocking Live Endpoint
    client = LiveLLMClient(service_name="ShopEase-Entropy", api_key=api_key, endpoint=url)
    if not client.connect(): pytest.fail("CRITICAL: Client Connection Failed.")
    yield client
    client.close()

@pytest.mark.smoke
def test_prompt_entropy_boundary(shopease_client):
    """Gradually cranks the mathematical temperature until the JSON structure shatters."""

    tracker_id = "TEMP_01"
    base_prompt = "ROLE: Analyze input. Output valid JSON.\nINPUT: Help me.\nOUTPUT:"

    current_temp = 0.0
    step_size = 0.5
    max_temp = 2.0

    print(f"\n[EXECUTING {tracker_id}] Commencing Destructive Entropy Test...")

    while current_temp <= max_temp:
        safe_temp = round(current_temp, 1)
        print(f"   [STRESSING] Heat Level: {safe_temp}...")

        # 1. Pydantic securely validates the float limit locally
        secure_payload = ShopEaseAIPayload(
            test_id=tracker_id,
            prompt=base_prompt,
            temperature=safe_temp,
            # We strictly pass exclude_none=True to prevent transmitting null keys
        ).model_dump(exclude_none=True)

        # 2. Network Execution
        raw_response = shopease_client.execute(secure_payload)

        if raw_response is None:
            pytest.fail(f"[{tracker_id}] Network aborted at Temp {safe_temp}.")

        # Simulating AI Breakdown: At Temp >= 1.5, the AI hallucinates broken JSON
        simulated_response = '{"intent": "HELP"}' if safe_temp < 1.5 else '{"intent": "HELP", }'

        try:
            # 3. Structural Validation Trap
            parsed = json.loads(simulated_response)
            assert "intent" in parsed

        except (json.JSONDecodeError, AssertionError) as e:
            final_score = round(safe_temp - step_size, 1)
            print(f"\n[{tracker_id}] -> PROMPT SHATTERED at Temperature {safe_temp}")
            print(f"[{tracker_id}] -> Official Entropy Score: {final_score}")
            return # Test officially passes by successfully finding the boundary

        current_temp += step_size

    print(f"\n[{tracker_id}] -> INDESTRUCTIBLE. Prompt survived Temp {max_temp}")

if __name__ == "__main__":
    pytest.main(["-s", "-v", __file__])