
# CODING EXERCISES
#
# Q5. Write a Python expression that generates a random float between 0.1 and 0.5 to use as jitter.
#
# Q6. Complete the function to cap the maximum backoff delay:
#
# def cap_delay(calculated_delay: int) -> int:
#     max_cap = 60
#     # return the lesser of calculated_delay or max_cap
#
# Q7. Debug this code:
#
# try:
#     make_api_call()
# except Exception:
#     trigger_backoff()
#
# Why is catching Exception here a dangerous testing and architectural practice?
#
# Q8. Write a test assertion that verifies a CircuitOpenError is raised when calling breaker.check_state() on an OPEN breaker.
#
# Q9. Write a list comprehension that converts all keys in my_dict to uppercase strings.
#
# Q10. Extend the ShopEase project by creating test_09_circuit_breaker.py that instantiates SimpleCircuitBreaker and tests the exact failure threshold boundary.
# SOLUTIONS FOR CHAPTER 12



# Q5:
import random

from Chapter_12.concepts.concept_4_circuit_breaker import CircuitOpenError

jitter = random.uniform(0.1, 0.5)

# Q6:
def cap_delay(calculated_delay: int) -> int:
    return min(calculated_delay, 60)

# Q7: Catches EVERYTHING (SyntaxError, KeyError, MemoryError) and falsely triggers backoff. Fix: except RateLimitError:

# Q8:
import pytest
with pytest.raises(CircuitOpenError):
    breaker.check()

# Q9:
upper_dict = {k.upper(): v for k, v in my_dict.items()}

# Q10: (Conceptual)
# Create test that loops record_failure up to threshold-1 (assert CLOSED), then one more (assert OPEN).