# SPDX-License-Identifier: MPL-2.0
# Concept 4: Graceful Error Handling Layer - Program 4
# File: demo_error_handling.py
# Purpose: Catches specific AI instability errors to prevent framework death.
# Author: Sandeep Dixit

import time
from typing import Optional

def simulate_unstable_ai_call(prompt: str, simulate_crash: bool = False) -> str:
    """Simulates a volatile external AI endpoint."""
    if simulate_crash:
        raise TimeoutError("The ShopEase AI servers are currently unresponsive.")
    return f"AI Processed: {prompt}"

def safe_ai_execution(prompt: str) -> Optional[str]:
    """The graceful error handling layer wrapping the unstable call."""
    print(f"--- Attempting Payload: {prompt} ---")
    try:
        # This is the dangerous code block
        result: str = simulate_unstable_ai_call(prompt, simulate_crash=True)
        return result

    except TimeoutError as te:
        # Highly specific exception caught
        print(f"[HANDLED ERROR] Network Timeout: {te}")
        return None

    except Exception as e:
        # Generic fallback for unknown, bizarre errors
        print(f"[FATAL CATCH] Unknown systemic failure: {e}")
        return None

    finally:
        # This ALWAYS runs, critical for freeing memory or closing files
        print("-> SAFETY NET: Execution cycle cleanly finalized.")

if __name__ == "__main__":
    try:
        # The test runner executes this securely
        final_output = safe_ai_execution("Explain quantum mechanics.")

        if final_output is None:
            print("Test gracefully failed. Proceeding to next test case without crashing.")
    except Exception as e:
        print(f"The safety net itself failed: {e}")