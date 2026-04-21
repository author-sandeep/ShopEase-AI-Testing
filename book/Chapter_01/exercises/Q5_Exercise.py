def check_for_error(ai_response: str) -> bool:
    try:
        return "error" in ai_response.lower()
    except AttributeError:
        return False