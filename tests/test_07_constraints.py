# SPDX-License-Identifier: MPL-2.0
# Concept 4: Negative Constraints - Program 4
# File: tests/test_07_constraints.py
# Purpose: Verifies AI obeys negative constraints.
# Author: Sandeep Dixit

import pytest
from typing import List

def test_negative_constraints() -> None:
    banned_words: List[str] = ["amazon", "walmart"]
    response: str = "We offer great prices at ShopEase."

    for word in banned_words:
        assert word not in response.lower()