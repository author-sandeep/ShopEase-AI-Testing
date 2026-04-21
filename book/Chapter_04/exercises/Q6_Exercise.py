import pytest
@pytest.mark.parametrize(
    "price, expected_discount",
    [(100, 10), (200, 20), (50, 5)]
)
def test_discounts(price, expected_discount):
    assert calculate_discount(price) == expected_discount