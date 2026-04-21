# SPDX-License-Identifier: MPL-2.0
# Concept 5: Parallel Execution Validation
# Author: Sandeep Dixit

import time
import asyncio
import pytest

async def slow_mock_api(task_id: int) -> str:
    await asyncio.sleep(1.0)
    return f"Task {task_id} done"

@pytest.mark.asyncio
async def test_parallel_efficiency() -> None:
    num_tasks: int = 3
    individual_delay: float = 1.0
    
    start_time: float = time.perf_counter()
    
    tasks = [slow_mock_api(i) for i in range(num_tasks)]
    results = await asyncio.gather(*tasks)
    
    end_time: float = time.perf_counter()
    duration: float = end_time - start_time
    
    assert len(results) == num_tasks, "Did not return all results!"
    
    synchronous_time: float = num_tasks * individual_delay
    assert duration < synchronous_time, "Code executed synchronously!"
    assert duration < 1.5, f"Parallel execution failed! Took {duration}s"
    
    print(f"PASS: {num_tasks} tasks ran in {duration:.2f}s instead of {synchronous_time}s.")

if __name__ == "__main__":
    asyncio.run(test_parallel_efficiency())
