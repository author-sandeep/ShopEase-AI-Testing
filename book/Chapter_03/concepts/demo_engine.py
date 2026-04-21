# SPDX-License-Identifier: MPL-2.0
# Concept 5: The Execution Engine - Program 5
# File: demo_engine.py
# Purpose: Orchestrates the complex lifecycle of AI test execution centrally.
# Author: Sandeep Dixit

from typing import Optional

# Mocking the Wrapper from Concept 1 for integration
class MockWrapper:
    def send(self, data: str) -> str:
        if not data:
            raise ValueError("Empty data rejected.")
        return f"[MOCK_API] Processed: {data}"

class FrameworkExecutionEngine:
    """The central conductor orchestrating test logic safely."""

    def run_cycle(self, wrapper_object: MockWrapper, prompt: str) -> Optional[str]:
        """Manages the full lifecycle of a single AI interaction."""
        print(">> ENGINE: Starting execution cycle...")

        try:
            # Step 1: Pre-execution validation
            if not isinstance(wrapper_object, MockWrapper):
                raise TypeError("Engine provided with invalid wrapper type.")

            # Step 2: Safe execution via the wrapper interface
            print(f">> ENGINE: Handing payload to Wrapper: '{prompt}'")
            raw_response: str = wrapper_object.send(prompt)

            # Step 3: Post-execution formatting/logging
            print(">> ENGINE: Payload processed successfully.")
            return raw_response.strip()

        except ValueError as ve:
            print(f">> ENGINE FAULT: Invalid Data provided - {ve}")
            return None
        except Exception as e:
            print(f">> ENGINE FAULT: Critical framework crash - {e}")
            return None
        finally:
            print(">> ENGINE: Cycle Complete. Releasing resources.\n")

if __name__ == "__main__":
    try:
        engine = FrameworkExecutionEngine()
        valid_wrapper = MockWrapper()

        # Scenario 1: Clean Execution
        result1 = engine.run_cycle(valid_wrapper, "Search for shoes.")
        print(f"Test Assertion receives: {result1}\n")

        # Scenario 2: Framework fault (Empty data)
        result2 = engine.run_cycle(valid_wrapper, "")
        if result2 is None:
            print("Test Assertion safely halted due to Engine fault protection.")

    except Exception as e:
        print(f"System completely failed: {e}")