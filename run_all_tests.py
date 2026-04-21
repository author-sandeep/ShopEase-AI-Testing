# SPDX-License-Identifier: MPL-2.0
# Concept 3 & 4: Master Execution - Lab Integration
# File: run_all_tests.py
# Purpose: Triggers the framework and returns strict OS exit codes.
# Author: Sandeep Dixit

import sys
import pytest
from typing import List
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main() -> None:
    print("--- STARTING SHOPEASE PHASE 2 CAPSTONE RUN ---")

    # Suppress warnings for clean output
    args: List[str] = ["tests/", "-v", "--disable-warnings"]
    exit_code: int = pytest.main(args)

    if exit_code == 0:
        print("--- RUN SUCCESS: DEPLOYMENT AUTHORIZED ---")
    else:
        print(f"--- RUN FAILED (Code {exit_code}): DEPLOYMENT BLOCKED ---")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()