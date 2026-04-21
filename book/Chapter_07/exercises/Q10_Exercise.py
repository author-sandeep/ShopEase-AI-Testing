import pytest
from pydantic import BaseModel, Field

class ValidationSchema(BaseModel):
    product: str = Field(min_length=3)

class MockGateway:
    def evaluate(self, payload: ValidationSchema) -> str:
        if "laptop" in payload.product.lower(): return "Electronics"
        return "Apparel"

@pytest.fixture(scope="module")
def api_gateway(): yield MockGateway()

@pytest.mark.parametrize("item, category", [("Laptops", "electronics"), ("Shoes", "apparel")])
def test_zero_shot_category(api_gateway, item: str, category: str):
    secure_payload = ValidationSchema(product=item)
    response = api_gateway.evaluate(secure_payload)
    assert category in response.lower(), "Zero-Shot Mapping Failed."