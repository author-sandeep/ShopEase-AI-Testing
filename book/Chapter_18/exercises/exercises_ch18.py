import pytest


# CODING EXERCISES
#
# Q5. Write the exact fixture decorator required to make a setup function run automatically once for the entire test session.
#
# Q6. Complete the execution logic to trap the result:
#
# import pytest
# def run_tests():
#     args = ["tests/", "-v"]
#     # Execute engine with args and store the integer result
#     exit_code = pytest.main(args)
#     return exit_code
#
# Q7. Debug this CI/CD pipeline script:
#
# import pytest
# import sys
# result = pytest.main(["tests/"])
# print(f"Tests finished with code {result}")
# sys.exit(0)
#
# Why is this incredibly dangerous to your deployment pipeline?
#
# Q8. Write a Python string operation that cleanly chains two strip commands to remove both markdown wrappers from a string named raw_data.
#
# Q9. Write an assertion to mathematically prove that a variable named exit_code is exactly zero.
#
# Q10. Extend the ShopEase project by creating the logic inside run_all_tests.py to check if the environment variables file exists, raising a RuntimeError to prevent tests from running if it is missing.
# SOLUTIONS FOR CHAPTER 18



# Q5:
@pytest.fixture(scope="session", autouse=True)
def global_setup():
    # setup
    yield
    # teardown

# Q6:
def run_tests():
    exit_code = pytest.main(["tests/", "-v"])
    return exit_code

# Q7: Unconditionally exits with 0 even if tests fail. Fix: sys.exit(result)

# Q8:
clean = raw_data.replace("```json\n", "").replace("```", "").strip()

# Q9:
assert exit_code == 0, f"Expected 0, got {exit_code}"

# Q10:
import os
def run_all_tests():
    if not os.path.exists(".env"):
        raise RuntimeError("Missing .env file")
    # rest of execution