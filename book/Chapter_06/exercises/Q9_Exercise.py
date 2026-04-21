def calculate_e2e_backoff(attempt_number: int) -> int:
    return 2 ** attempt_number