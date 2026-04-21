import os


def check_temperature() -> float:
    try:
        temp = os.getenv("AI_TEMP", "0.0")
        return float(temp)
    except (TypeError, ValueError):
        return 0.0