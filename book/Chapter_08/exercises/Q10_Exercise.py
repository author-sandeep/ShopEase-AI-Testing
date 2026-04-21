def get_ai_status(): return "ACTIVE " # Mock AI

def shopease_halo_loop(runs: int):
    results = []
    for _ in range(runs):
        raw = get_ai_status()
        results.append(raw.strip().upper())

    unique = set(results)
    assert len(unique) == 1, "Consistency failed."
    assert "ACTIVE" in unique, "Accurate output missing."
    print("Halo loop passed safely.")