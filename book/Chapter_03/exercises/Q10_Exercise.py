import json

class ValidationEngine:
    def run_validation(self, payload: str) -> bool:
        try:
            json.loads(payload)
            return True
        except json.JSONDecodeError as e:
            print(f"Validation failed: Invalid JSON structure - {e}")
            return False
        finally:
            print("Validation Engine cycle finalized.")