import asyncio
import time
import pytest

def mock_network_call(delay: float) -> str:
    if delay > 3.0:
        raise TimeoutError("Connection Aborted")
    time.sleep(delay)
    return "success"

def test_sla_latency_boundary() -> None:
    start = time.perf_counter()
    response = mock_network_call(delay=1.0)
    duration = time.perf_counter() - start

    assert response == "success"
    assert duration < 2.0, "API is too slow!"

def test_timeout_fallback() -> None:
    with pytest.raises(TimeoutError):
        mock_network_call(delay=5.0)


async def async_api_mock(task_id: int) -> str:
    await asyncio.sleep(0.5) # Fast 0.5s network call
    return f"Done {task_id}"

@pytest.mark.asyncio
async def test_parallel_speed() -> None:
    start = time.perf_counter()

    # Launch 5 concurrent calls
    tasks = [async_api_mock(i) for i in range(5)]
    results = await asyncio.gather(*tasks)

    duration = time.perf_counter() - start

    # Validation: 5 calls of 0.5s synchronously = 2.5s
    # In parallel, they should take ~0.5s total.
    assert len(results) == 5
    assert duration < 1.0, f"Concurrency failed! Took {duration}s"