from typing import Any
def process_data(data: Any) -> None:
    if not isinstance(data, list):
        raise TypeError(f"Expected list, got {type(data).__name__}")
    print("Processing list safely.")