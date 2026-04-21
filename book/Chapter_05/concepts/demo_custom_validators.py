# SPDX-License-Identifier: MPL-2.0
# Concept 3: Custom Field Validators - Program 3
# File: demo_custom_validators.py
# Purpose: Enforces deep business logic rules beyond standard type checking.
# Author: Sandeep Dixit

from pydantic import BaseModel, ValidationError, field_validator
from typing import Optional

class SecureAIPrompt(BaseModel):
    """Schema ensuring prompts are logically sound for execution."""
    prompt_text: str
    max_tokens: int

    @field_validator("prompt_text")
    @classmethod
    def prevent_empty_or_malicious_prompts(cls, value: str) -> str:
        """Validates the business rules of the prompt string."""
        cleaned_val = value.strip()
        if len(cleaned_val) < 5:
            raise ValueError("Prompt must be at least 5 characters long.")
        if "DROP TABLE" in cleaned_val.upper():
            raise ValueError("CRITICAL: SQL Injection pattern detected!")
        return cleaned_val

    @field_validator("max_tokens")
    @classmethod
    def enforce_token_limits(cls, value: int) -> int:
        """Validates AI token boundary constraints."""
        if not (50 <= value <= 2000):
            raise ValueError("Tokens must be strictly between 50 and 2000.")
        return value

def execute_business_validation() -> None:
    try:
        print("-> Testing valid constraints...")
        safe_model = SecureAIPrompt(prompt_text="Find laptops", max_tokens=100)
        print(f"Passed: {safe_model.prompt_text}")

        print("\n-> Testing malicious prompt constraint...")
        SecureAIPrompt(prompt_text="DROP TABLE users;", max_tokens=100)
    except ValidationError as e:
        print(f"[REJECTED] {e.errors()[0]['msg']}")
    except Exception as e:
        print(f"System fault: {e}")
    finally:
        pass

if __name__ == "__main__":
    execute_business_validation()