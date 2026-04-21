import uuid
from typing import List

def generate_traces() -> List[str]:
    try:
        return [str(uuid.uuid4())[:12] for _ in range(5)]
    except Exception:
        return []