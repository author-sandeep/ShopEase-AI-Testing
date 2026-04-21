def test_e2e_success_code(resp):
    assert resp.status_code in [200, 201], f"Unexpected E2E Status: {resp.status_code}"