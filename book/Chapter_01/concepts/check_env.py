# SPDX-License-Identifier: MPL-2.0
# Concept 2: Environment Isolation - Program 2
# File: check_env.py
# Purpose: Validates if code is running in an isolated venv.
# Author: Sandeep Dixit

import sys
import os

def check_virtual_environment() -> bool:
    """Detects if Python is running inside a virtual environment."""
    try:
        # sys.prefix points to the environment Python is running from
        # sys.base_prefix points to the global system Python installation
        is_isolated: bool = sys.prefix != sys.base_prefix
        return is_isolated
    except AttributeError as e:
        print(f"Attribute error detected: {e}")
        return False
    finally:
        pass

if __name__ == "__main__":
    try:
        if check_virtual_environment():
            print("SUCCESS: Running securely inside an isolated environment.")
        else:
            print("WARNING: Running on global system. Please activate venv.")
    except Exception as e:
        print(f"Framework execution failed: {e}")