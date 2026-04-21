def build_template(user_text: str) -> str:
    return f"""
    SYSTEM: Classify.
    INPUT: "Is this open?"
    OUTPUT: HOURS
    
    INPUT: "{user_text}"
    OUTPUT:
    """.strip()