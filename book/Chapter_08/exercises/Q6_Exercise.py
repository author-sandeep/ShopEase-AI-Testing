def filter_finance(db: list) -> list:
    return [item for item in db if item.get("domain") == "finance"]