def safe_cast(user_input: str) -> int:
    try:
        return int(user_input)
    except ValueError:
        print("Input is not a valid integer.")
        return 0
    finally:
        print("Casting attempt completed.")