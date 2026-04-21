# SPDX-License-Identifier: MPL-2.0
# Concept 1 & 5: E2E Capstone - Lab Integration
# File: tests/test_14_capstone.py
# Purpose: Final integration test for Phase 2.
# Author: Sandeep Dixit

import pytest
from pydantic import BaseModel


class FinalSchema(BaseModel):
    status: str


def test_final_integration_pipeline() -> None:
    raw_ai = '```json\n{"status": "Foundation Secured"}\n```'

    # Simulate Stripper using clean string replacement
    clean = raw_ai.replace("```json\n", "").replace("```", "").strip()

    # Simulate Pydantic
    obj = FinalSchema.model_validate_json(clean)

    assert obj.status == "Foundation Secured"
    print("VOLUME 1 CAPSTONE INTEGRATION COMPLETE.")