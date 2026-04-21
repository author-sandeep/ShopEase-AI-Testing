# SPDX-License-Identifier: MPL-2.0
# Concept 2: Network Interception via @patch
# Author: Sandeep Dixit

import pytest
import requests
from unittest.mock import patch, MagicMock
from typing import Dict, Any

def execute_external_api() -> Dict[str, Any]:
    response = requests.post("https://fake-shopease-api.com/v1/chat")
    return response.json()

@patch(f"{__name__}.requests.post")
def test_network_interception(mock_post: MagicMock) -> None:
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"reply": "Mocked Success"}
    
    mock_post.return_value = mock_response
    
    result: Dict[str, Any] = execute_external_api()
    
    assert result["reply"] == "Mocked Success", "Intercept failed!"
    mock_post.assert_called_once_with("https://fake-shopease-api.com/v1/chat")
    
    print("PASS: Network call successfully intercepted and mocked.")

if __name__ == "__main__":
    test_network_interception()
