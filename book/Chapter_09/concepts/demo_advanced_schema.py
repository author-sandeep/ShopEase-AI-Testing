# SPDX-License-Identifier: MPL-2.0
# Concept 5: Dynamically Configuring the Pydantic Payload - Program 5
# File: demo_advanced_schema.py
# Purpose: Enforces strict mathematical boundary layers for generation parameters.
# Author: Sandeep Dixit

from pydantic import BaseModel, Field, ValidationError
from typing import Optional

class AdvancedAIPayload(BaseModel):
    """The upgraded execution schema encompassing all generation parameters."""

    test_id: str = Field(min_length=3)
    prompt: str = Field(min_length=1)

    # Mathematical boundaries mirroring standard LLM API specifications
    temperature: float = Field(default=0.0, ge=0.0, le=2.0, description="Creativity dial.")

    # Optional parameters fallback to standard API defaults if omitted
    top_p: Optional[float] = Field(default=1.0, ge=0.0, le=1.0, description="Nucleus mass.")
    frequency_penalty: Optional[float] = Field(default=0.0, ge=-2.0, le=2.0)
    presence_penalty: Optional[float] = Field(default=0.0, ge=-2.0, le=2.0)

def test_schema_boundaries() -> None:
    """Validates the schema's ability to reject out-of-bound float parameters."""

    print("--- Test 1: Flawless Boundary Configuration ---")
    try:
        valid = AdvancedAIPayload(
            test_id="TC_01",
            prompt="Hello",
            temperature=1.5,
            top_p=0.9,
            frequency_penalty=2.0
        )
        print(f"Success. Temp: {valid.temperature} | Freq: {valid.frequency_penalty}")
    except ValidationError as e:
        print(f"Fault: {e}")

    print("\n--- Test 2: Fatal Boundary Violation ---")
    try:
        # We explicitly violate the Less-Than-or-Equal (le) constraint
        invalid = AdvancedAIPayload(
            test_id="TC_02",
            prompt="Hello",
            presence_penalty=5.0 # Max allowed is 2.0
        )
    except ValidationError as ve:
        error_dict = ve.errors()[0]
        print(f"-> PYDANTIC FIREWALL BLOCKED MALICIOUS DATA: ")
        print(f"   Field: {error_dict['loc'][0]}")
        print(f"   Reason: {error_dict['msg']}")
    finally:
        pass

if __name__ == "__main__":
    test_schema_boundaries()