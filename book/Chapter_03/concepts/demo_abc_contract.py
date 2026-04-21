# SPDX-License-Identifier: MPL-2.0
# Concept 3: Abstract Base Classes for Contracts - Program 3
# File: demo_abc_contract.py
# Purpose: Forces strict architectural compliance across all test wrappers.
# Author: Sandeep Dixit

from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAIAssertionContract(ABC):
    """The strict blueprint for any AI test evaluation logic."""

    @abstractmethod
    def evaluate(self, ai_response: str) -> bool:
        """Mandatory: Must execute the core evaluation logic."""
        pass

    @abstractmethod
    def get_failure_reason(self) -> str:
        """Mandatory: Must provide a detailed string if evaluate() fails."""
        pass

class JSONFormatAssertion(BaseAIAssertionContract):
    """A concrete implementation honoring the ABC contract."""

    def __init__(self):
        self._reason: str = "No execution yet."

    def evaluate(self, ai_response: str) -> bool:
        """Concrete implementation of the required method."""
        try:
            if "{" in ai_response and "}" in ai_response:
                return True
            self._reason = "Response lacks JSON brackets."
            return False
        except Exception as e:
            self._reason = f"Fatal Error: {e}"
            return False
        finally:
            pass

    def get_failure_reason(self) -> str:
        """Concrete implementation of the required tracking method."""
        return self._reason

if __name__ == "__main__":
    try:
        # We instantiate the CONCRETE class, not the ABSTRACT one
        validator = JSONFormatAssertion()

        test_payload: str = "Here is your item: [Red Shirt]"
        is_valid: bool = validator.evaluate(test_payload)

        if not is_valid:
            print(f"Assertion Failed! Reason: {validator.get_failure_reason()}")
    except Exception as e:
        print(f"System Error: {e}")