# SPDX-License-Identifier: MPL-2.0
# Concept 4: Handling Pydantic Validation Errors - Program 4
# File: demo_graceful_validation.py
# Purpose: Extracts and safely logs Pydantic crashes without halting execution.
# Author: Sandeep Dixit

from pydantic import BaseModel, ValidationError, Field
from typing import Optional

class RobustPayload(BaseModel):
    # Using Field for inline constraints as an alternative to custom validators
    target_url: str = Field(min_length=10, description="Must be a valid URL length.")
    retry_count: int = Field(ge=0, le=5, description="Retries capped at 5.")

def safe_schema_instantiation(url_input: str, retries: int) -> Optional[RobustPayload]:
    """Wraps schema creation in a highly defensive error layer."""
    try:
        payload = RobustPayload(target_url=url_input, retry_count=retries)
        return payload

    except ValidationError as ve:
        print("\n-> FRAMEWORK SHIELD ACTIVATED: Caught Bad Test Data.")
        # ve.errors() returns a list of dictionaries with exact failure metadata
        for error in ve.errors():
            field_name = error.get("loc", ["Unknown"])[0]
            error_msg = error.get("msg", "No message provided.")
            print(f"[SCHEMA FAULT] Field '{field_name}': {error_msg}")
        return None

    except Exception as e:
        print(f"Critical Unknown Failure: {e}")
        return None
    finally:
        pass

if __name__ == "__main__":
    print("Test Cycle 1: Executing flawless data...")
    success_obj = safe_schema_instantiation("https://mock-shopease.com", 3)
    if success_obj: print("Cycle 1 Passed.")

    print("\nTest Cycle 2: Executing fatally flawed data...")
    # Passing an empty string (fails length) and an oversized integer (fails limit)
    failure_obj = safe_schema_instantiation("http", 99)
    if failure_obj is None: print("Cycle 2 Safely Handled and Quarantined.")