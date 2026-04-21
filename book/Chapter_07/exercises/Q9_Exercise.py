def test_complex_containment(output: str):
    clean_text = output.lower()
    assert "approved" in clean_text and "finance" in clean_text, "Keywords missing."