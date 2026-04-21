# SPDX-License-Identifier: MPL-2.0
# Concept 5: Async Mocking (AsyncMock)
# Author: Sandeep Dixit

import asyncio
import pytest
from unittest.mock import AsyncMock
from typing import Dict, Any, List

async def parallel_backend_processor(async_client: AsyncMock, num_tasks: int) -> List[Dict[str, Any]]:
    tasks = [async_client() for _ in range(num_tasks)]
    results: List[Dict[str, Any]] = await asyncio.gather(*tasks)
    return results

@pytest.mark.asyncio
async def test_async_mock_execution() -> None:
    fake_async_api = AsyncMock()
    fake_async_api.return_value = {"status": "async_success"}
    
    results: List[Dict[str, Any]] = await parallel_backend_processor(fake_async_api, num_tasks=3)
    
    assert len(results) == 3, "Parallel execution dropped tasks!"
    assert results[0]["status"] == "async_success", "Async data corrupted!"
    assert fake_async_api.await_count == 3, "Mock was not awaited correctly!"
    
    print(f"PASS: AsyncMock processed {fake_async_api.await_count} concurrent requests.")

if __name__ == "__main__":
    asyncio.run(test_async_mock_execution())
