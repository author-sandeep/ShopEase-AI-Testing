def assert_consistency(response_set: set):
    assert len(response_set) == 1, f"Variance Detected. Got: {response_set}"