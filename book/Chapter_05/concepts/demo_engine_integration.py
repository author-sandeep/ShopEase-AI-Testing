# SPDX-License-Identifier: MPL-2.0
# Concept 5: Integrating Schemas - Program 5
# File: demo_engine_integration.py
# Purpose: Fuses strict data validation directly into the central execution pipeline.
# Author: Sandeep Dixit

from pydantic import BaseModel, ValidationError, Field
from typing import Optional

# 1. The Impenetrable Schema
class EnginePayload(BaseModel):
    """The strict data envelope required by the central Engine."""
    operation_name: str = Field(min_length=3)
    target_endpoint: str
    is_secure: bool = True

# 2. Mocking the API Wrapper
class MockSecureWrapper:
    def execute_api_call(self, endpoint: str) -> str:
        return f"200 OK: Secured connection to {endpoint}"

# 3. The Central Execution Engine
class EnterpriseExecutionEngine:
    """The central orchestrator strictly enforcing schema payloads."""

    def run_validated_cycle(self, payload: EnginePayload, wrapper: MockSecureWrapper) -> Optional[str]:
        """Accepts ONLY Pydantic objects, completely banning loose dictionaries."""
        try:
            # The Engine completely trusts the payload because Pydantic already validated it.
            print(f">> ENGINE: Payload Validated for '{payload.operation_name}'")
            print(">> ENGINE: Handing trusted data to API Wrapper...")

            result: str = wrapper.execute_api_call(payload.target_endpoint)
            return result

        except Exception as e:
            print(f">> ENGINE FATAL ERROR: {e}")
            return None
        finally:
            print(">> ENGINE: Execution flow terminated safely.\n")

if __name__ == "__main__":
    engine = EnterpriseExecutionEngine()
    api_wrapper = MockSecureWrapper()

    try:
        # Step 1: The Test Script securely instantiates the payload
        clean_payload = EnginePayload(
            operation_name="Auth_Test",
            target_endpoint="/v1/auth"
        )
        # Step 2: The Test Script hands the trusted object to the Engine
        response = engine.run_validated_cycle(clean_payload, api_wrapper)
        print(f"Test Assertion receives: {response}")

    except ValidationError as ve:
        print(f"Test aborted instantly due to bad schema data: {ve}")