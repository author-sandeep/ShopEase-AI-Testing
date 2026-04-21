
# CODING EXERCISES
#
# Q5. Write a Python expression using time.perf_counter() to calculate the execution time of a function named do_work().
#
# Q6. Complete the async function syntax:
#
# _____ get_ai_data():
# data = _____ make_network_request()
# return data
#
# Q7. Debug this code:
#
# async def my_test():
#     result = slow_api_call()
#     assert result == "Success"
#
# Why does this fail instantly, and how do you fix it?
#
# Q8. Write an assertion that verifies a duration variable is strictly less than a max_sla variable.
#
# Q9. Create a list comprehension that generates 5 identical coroutines of the function mock_api().
#
# Q10. Extend the ShopEase project by writing an async test function that uses asyncio.gather to execute mock_api() 5 times, and asserts the length of the returned results list is exactly 5.
# SOLUTIONS FOR CHAPTER 15


# Q5:
start = time.perf_counter()
do_work()
duration = time.perf_counter() - start

# Q6:
async def get_ai_data():
    data = await make_network_request()
    return data

# Q7: slow_api_call() is async coroutine; calling without await returns coroutine object, not result. Fix: result = await slow_api_call()

# Q8:
assert duration < max_sla, f"Latency {duration} exceeded SLA {max_sla}"

# Q9:
tasks = [mock_api() for _ in range(5)]

# Q10:
import pytest
import asyncio
@pytest.mark.asyncio
async def test_gather_length():
    async def mock_api():
        return "done"
    tasks = [mock_api() for _ in range(5)]
    results = await asyncio.gather(*tasks)
    assert len(results) == 5