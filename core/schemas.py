# SPDX-License-Identifier: MPL-2.0
# Concept: Dynamically Configuring the Pydantic Payload
# File: core/schemas.py
# Purpose: Foundational data validation schemas for the ShopEase framework.
# Author: Sandeep Dixit

from pydantic import BaseModel, Field, field_validator
from typing import Optional

class ShopEaseAIPayload(BaseModel):
    """Strict execution schema encompassing advanced AI generation parameters."""

    test_id: str = Field(min_length=3, description="Unique execution tracker.")
    prompt: str = Field(min_length=2, description="The raw natural language prompt.")

    # Mathematical Generation Boundaries
    temperature: float = Field(default=0.0, ge=0.0, le=2.0)
    top_p: Optional[float] = Field(default=1.0, ge=0.0, le=1.0)
    frequency_penalty: Optional[float] = Field(default=0.0, ge=-2.0, le=2.0)
    presence_penalty: Optional[float] = Field(default=0.0, ge=-2.0, le=2.0)

    @field_validator("prompt")
    @classmethod
    def sanitize_prompt(cls, v: str) -> str:
        """Enforces business logic boundaries on the text prompt."""
        clean_text = v.strip()
        if not clean_text:
            raise ValueError("Prompt cannot be completely blank.")
        if "SYSTEM:" in clean_text.upper():
            raise ValueError("Unauthorized attempt to hijack AI system instructions.")
        return clean_text