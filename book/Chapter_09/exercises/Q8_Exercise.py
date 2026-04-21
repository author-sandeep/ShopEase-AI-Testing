def calculate_entropy_score(failure_temp: float, step_size: float) -> float:
    return round(failure_temp - step_size, 1)