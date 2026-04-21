# SPDX-License-Identifier: MPL-2.0
# Concept 2: Synchronous Timeout Limits
# Author: Sandeep Dixit

import time
import pytest

class ForcedTimeoutError(Exception):
    pass

def mock_network_client(delay: float, timeout_limit: float) -> str:
    if delay > timeout_limit:
        raise ForcedTimeoutError(f"Request aborted after {timeout_limit}s")
    
    time.sleep(delay)
    return '{"status": "success"}'

def test_hard_timeout_enforcement() -> None:
    system_timeout: float = 3.0
    slow_server_delay: float = 10.0
    
    with pytest.raises(ForcedTimeoutError) as exc_info:
        mock_network_client(delay=slow_server_delay, timeout_limit=system_timeout)
    
    assert "aborted" in str(exc_info.value)
    print(f"PASS: System successfully cut the connection at {system_timeout}s.")

if __name__ == "__main__":
    test_hard_timeout_enforcement()
