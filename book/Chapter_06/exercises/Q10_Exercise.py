import pytest
import requests

def test_e2e_ai_health():
    try:
        response = requests.get("https://api.openai.com/v1/models", timeout=5.0)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        pytest.fail("E2E FATAL: Internet connection is completely severed.")
    except Exception as e:
        pytest.fail(f"E2E Unknown failure: {e}")