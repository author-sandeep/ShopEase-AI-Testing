def test_ai_structural_schema():
    response = get_ai_data()
    assert isinstance(response, dict), "Response must be a dict."
    assert "confidence_score" in response, "Missing critical key."