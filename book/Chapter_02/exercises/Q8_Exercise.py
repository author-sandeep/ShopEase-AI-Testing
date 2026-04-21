import json
from typing import Dict, Any

def serialize_payload(payload: Dict[str, Any]) -> str:
    try:
        return json.dumps(payload, ensure_ascii=False)
    except (TypeError, ValueError):
        return "{}"