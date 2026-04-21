# SPDX-License-Identifier: MPL-2.0
# Concept 1: E2E Capstone Architecture
# Author: Sandeep Dixit

import pytest
from unittest.mock import MagicMock
from pydantic import BaseModel, ValidationError

class ShopEaseCart(BaseModel):
    item: str
    price: float

def simulated_e2e_pipeline(mock_client: MagicMock, query: str) -> ShopEaseCart:
    if len(query) > 1000:
        raise ValueError("Prompt too large!")
    
    raw_response: str = mock_client()
    clean_text: str = raw_response.replace("```json\n", "").replace("```", "").strip()
    validated_obj: ShopEaseCart = ShopEaseCart.model_validate_json(clean_text)
    
    return validated_obj

def test_phase_2_capstone_pipeline() -> None:
    mock_llm = MagicMock()
    mock_llm.return_value = '```json\n{"item": "Laptop", "price": 999.99}\n```'
    
    final_data: ShopEaseCart = simulated_e2e_pipeline(mock_llm, "Buy a laptop")
    
    assert final_data.item == "Laptop", "E2E Pipeline lost data!"
    assert isinstance(final_data.price, float), "E2E Pipeline typing failed!"
    
    print("PASS: The Phase 2 Capstone Pipeline executed flawlessly.")

if __name__ == "__main__":
    test_phase_2_capstone_pipeline()
