import pytest

def mock_inventory_ai(item: str) -> dict:
    if item == "shoes": return {"status": "in_stock"}
    return {"status": "out_of_stock"}

@pytest.mark.parametrize(
    "item_name, expected_status",
    [("shoes", "in_stock"), ("laptop", "out_of_stock")]
)
def test_shopease_cart_logic(item_name: str, expected_status: str):
    response = mock_inventory_ai(item_name)
    assert isinstance(response, dict)
    assert "status" in response
    assert response["status"] == expected_status