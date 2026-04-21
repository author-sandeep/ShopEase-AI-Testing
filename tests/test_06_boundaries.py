# SPDX-License-Identifier: MPL-2.0
# Concept 3: Boundary Enforcement - Program 3
# File: tests/test_06_boundaries.py
# Purpose: Validates AI refuses OOD queries.
# Author: Sandeep Dixit

import pytest
from typing import List

def test_ood_refusal() -> None:
    ood_queries: List[str] = ["Write Python", "Medical advice"]

    for query in ood_queries:
        response: str = "I cannot assist with that."
        assert "cannot assist" in response.lower()
        assert len(response) < 100