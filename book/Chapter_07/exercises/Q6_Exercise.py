import pytest
@pytest.mark.parametrize(
    "user_query, expected_category",
    [("I need help", "support"), ("Buy now", "sales"), ("Broken app", "bug")]
)
def test_ai_classification(user_query, expected_category):
    pass