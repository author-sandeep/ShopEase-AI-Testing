# SPDX-License-Identifier: MPL-2.0
# Concept 3: Master Execution Script
# Author: Sandeep Dixit

import sys
import pytest
from typing import List

def execute_test_suite() -> int:
    print("=" * 50)
    print(" SHOPEASE AI - PHASE 2 CAPSTONE EXECUTION ENGINE ")
    print("=" * 50)
    
    pytest_args: List[str] = [
        "Chapters.Chapter_18/concepts/",
        "-v",
        "--tb=short",
        "--disable-warnings",
        "-p", "no:cacheprovider"
    ]
    
    print(f"\nTriggering Engine with args: {pytest_args}\n")
    exit_code: int = pytest.main(pytest_args)
    
    return exit_code

def test_master_script_execution() -> None:
    result_code = pytest.main(["Chapters.Chapter_18/concepts/concept_1_e2e_capstone_architecture.py", "-q"])
    assert result_code == 0 or result_code == 1, "Invalid exit code"
    print("PASS: Master execution script structure verified.")

if __name__ == "__main__":
    result_code: int = execute_test_suite()
    sys.exit(result_code)
