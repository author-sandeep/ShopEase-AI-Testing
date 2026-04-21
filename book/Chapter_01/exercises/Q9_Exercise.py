import json
def parse_mock_json(data: str):
    try:
        parsed = json.loads(data)
        print("Success")
        return parsed
    except json.JSONDecodeError as e:
        print(f"Failed to parse: {e}")
        return None
    finally:
        print("Execution completed.")