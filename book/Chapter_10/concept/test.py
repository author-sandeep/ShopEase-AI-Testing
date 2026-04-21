# Q5. Write a Python expression that generates a random float between 0.1 and 0.5 to use as
# jitter.
# Q6. Complete the function to cap the maximum backoff delay:
# Python
# def cap_delay(calculated_delay: int) -> int:
#     max_cap = 60
# # return the lesser of calculated_delay or max_cap
# Q7. Debug this code:
# Python
# try:
#     make_api_call()
# except Exception:
# trigger_backoff()
# Why is catching Exception here a dangerous testing and architectural practice?
# Q8. Write a test assertion that verifies a CircuitOpenError is raised when calling
# breaker.check_state() on an OPEN breaker.
# Q9. Write a list comprehension that converts all keys in my_dict to uppercase strings.
# Q10. Extend the ShopEase project by creating test_09_circuit_breaker.py that instantiates
# SimpleCircuitBreaker and tests the exact failure threshold boundary.
# EXERCISE SOLUTIONS
# SOLUTION Q1. Because repeatedly hammering a live, paid API to intentionally trigger a rate
# limit will drain your account balance and potentially get your company's IP address
# permanently banned.
# SOLUTION Q2. A static 5-second loop can overwhelm a recovering server. Exponential
# backoff progressively reduces the load, giving the struggling server breathing room to
# recover.
# SOLUTION Q3. Thundering Herd problem. Without jitter, thousands of clients might backoff
# and retry at the exact same millisecond, crushing the API again.
# SOLUTION Q4. It allows the system to cautiously send a single test request to check if the
# downstream server has recovered, without fully opening the floodgates and letting all traffic
# through.
# SOLUTION Q5.
# Python
# import random
# jitter = random.uniform(0.1, 0.5)
# SOLUTION Q6.
# Python
# def cap_delay(calculated_delay: int) -> int:
#     max_cap = 60
# return min(calculated_delay, max_cap)
# SOLUTION Q7. It catches EVERYTHING. If there is a SyntaxError, KeyError, or
# MemoryError, the system will falsely trigger a rate-limit backoff instead of reporting the actual
# bug. Always catch specific exceptions like RateLimitError.
# SOLUTION Q8.
# Python
# import pytest
# with pytest.raises(CircuitOpenError):
#     breaker.check_state()
# SOLUTION Q9.
# Python
# upper_dict = {k.upper(): v for k, v in my_dict.items()}
# SOLUTION Q10. (See Lab Implementation logic). Create a file that loops record_failure
# exactly up to the threshold minus one (assert CLOSED), then hits the threshold (assert
# OPEN).