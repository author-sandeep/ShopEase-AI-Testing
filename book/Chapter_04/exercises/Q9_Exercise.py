def test_latency_boundaries():
    ai_latency_ms = get_api_latency()
    assert isinstance(ai_latency_ms, int), "Latency must be integer."
    assert 0 < ai_latency_ms < 2000, "Latency exceeded 2-second SLA constraint."