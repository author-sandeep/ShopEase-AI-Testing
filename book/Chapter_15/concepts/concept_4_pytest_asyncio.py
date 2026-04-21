# SPDX-License-Identifier: MPL-2.0
# Concept 4: Asynchronous API Testing (pytest-asyncio)
# Author: Sandeep Dixit

import asyncio
import pytest
from typing import Dict, Any

async def async_llm_call(prompt: str) -> Dict[str, str]:
    await asyncio.sleep(0.5)
    return {"status": "success", "echo": prompt}

@pytest.mark.asyncio
async def test_async_coroutine_execution() -> None:
    test_prompt: str = "Hello Async"
    
    response: Dict[str, str] = await async_llm_call(test_prompt)
    
    assert response["status"] == "success", "Async dict corrupted!"
    assert response["echo"] == test_prompt, "Data mapping failed!"
    
    print(f"PASS: Async coroutine resolved correctly -> {response}")

if __name__ == "__main__":
    asyncio.run(test_async_coroutine_execution())
