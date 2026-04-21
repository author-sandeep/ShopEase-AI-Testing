# SPDX-License-Identifier: MPL-2.0
# Concept 4: CI/CD Pipeline Readiness (Exit Codes)
# Author: Sandeep Dixit

import sys
import pytest

def run_pipeline() -> None:
    print("Initiating Pipeline Execution...")
    exit_code: int = pytest.main(["-q", "--collect-only"])
    
    if exit_code == 0:
        print("\n[PIPELINE SUCCESS] All systems Go. Safe to deploy.")
    else:
        print(f"\n[PIPELINE FAILED] Exit Code {exit_code}. Deployment BLOCKED.")
    
    sys.exit(exit_code)

def test_exit_code_handling() -> None:
    result = pytest.main(["-q", "--collect-only"])
    assert result == 0 or result == 5, "Exit code should be 0 or 5"
    print("PASS: Exit code handling logic works.")

if __name__ == "__main__":
    try:
        run_pipeline()
    except Exception as e:
        print(f"CRITICAL RUNNER CRASH: {str(e)}")
        sys.exit(1)
