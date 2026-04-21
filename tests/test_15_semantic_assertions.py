# SPDX-License-Identifier: MPL-2.0
# Concept 4 & 5: Semantic Testing - Lab Integration
# File: tests/test_15_semantic_assertions.py
# Purpose: Validates the new meaning-based evaluation logic.
# Author: Sandeep Dixit

import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.semantic_assert import assert_semantically_close

class TestSemanticEvaluation:
    """Suite validating that the framework grades meaning, not syntax."""

    def test_synonym_tolerance(self):
        """Verifies that synonyms pass the semantic check."""
        try:
            ai_reply = "I am absolutely furious about this delay."
            target = "I am very angry."
            # This should pass because underlying meaning is identical
            assert_semantically_close(ai_reply, target, threshold=0.65)
        finally:
            pass

    def test_hallucination_detection(self):
        """Verifies that unrelated topics fail the semantic check."""
        try:
            ai_reply = "Your order will arrive on Tuesday."
            target = "I love ice cream."
            with pytest.raises(AssertionError, match="Mismatch"):
                assert_semantically_close(ai_reply, target, threshold=0.65)
        finally:
            pass

    def test_boundary_validation(self):
        """Ensures empty strings are handled gracefully."""
        try:
            with pytest.raises(ValueError, match="cannot be empty"):
                assert_semantically_close("", "Target", threshold=0.5)
        finally:
            pass

if __name__ == "__main__":
    pytest.main(["-v", __file__])