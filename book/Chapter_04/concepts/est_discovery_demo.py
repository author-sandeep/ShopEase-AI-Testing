# SPDX-License-Identifier: MPL-2.0
# Concept 1: The Pytest Discovery Mechanics - Program 1
# File: test_discovery_demo.py
# Purpose: Demonstrates strict Pytest naming conventions for automated execution.
# Author: Sandeep Dixit

def setup_database_mock():
    """This function does NOT start with 'test_'. Pytest will ignore it."""
    print("Database mock initialized silently.")
    return True

def test_valid_ai_response():
    """This function STARTS with 'test_'. Pytest will execute it."""
    print("Executing core test logic...")
    ai_status = "ONLINE"
    assert ai_status == "ONLINE", "AI should be strictly online."

def test_fallback_mechanism():
    """Another valid test Pytest will discover automatically."""
    print("Testing safe fallback...")
    fallback_active = True
    assert fallback_active is True, "Fallback must be active on failure."

# Note: We do NOT need an 'if __name__ == "__main__":' block.
# Pytest runs this file entirely from the outside.