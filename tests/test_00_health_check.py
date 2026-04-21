# SPDX-License-Identifier: MPL-2.0
# Concept 5: The Connectivity Health-Check Assertion - Program 5
# File: tests/test_00_health_check.py
# Purpose: The ultimate E2E Pytest gateway verifying live API stability.
# Author: Sandeep Dixit

import pytest
import requests
from typing import Dict, Any

# Simulating the extraction of our critical parameters
API_URL = "https://jsonplaceholder.typicode.com/posts"
API_KEY = "mock-secure-token"

@pytest.mark.smoke
def test_live_ai_connectivity():
    """E2E script verifying the framework can securely reach the AI API."""

    # 1. Construct the tiny, cheap E2E payload
    health_payload: Dict[str, Any] = {
        "title": "ShopEase Health Check",
        "body": "System Ping",
        "userId": 1
    }

    secure_headers: Dict[str, str] = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # 2. Execute the E2E Efficacy Network Call
        response = requests.post(
            url=API_URL,
            headers=secure_headers,
            json=health_payload,
            timeout=5.0
        )

        # 3. Core E2E Assertions: Network Level
        assert response.status_code == 201, f"Health-check failed with status: {response.status_code}"

        # 4. Core E2E Assertions: Structural Level
        data: Dict[str, Any] = response.json()
        assert isinstance(data, dict), "E2E Response is not structurally JSON."
        assert "id" in data, "E2E Response lacks critical architectural ID key."

        print(f"\n[SYSTEM HEALTHY] AI API is reachable. E2E Assigned ID: {data.get('id')}")

    except requests.exceptions.RequestException as e:
        pytest.fail(f"CRITICAL: Live E2E connectivity completely severed. {e}")