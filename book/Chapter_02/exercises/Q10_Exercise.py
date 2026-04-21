import logging
from typing import Dict

def log_ai_hallucination(logger: logging.Logger, trace_id: str, message: str) -> None:
    try:
        context: Dict[str, str] = {"correlation_id": trace_id}
        logger.error(f"Hallucination Detected: {message}", extra=context)
    except Exception as e:
        print(f"Logging trace failed: {e}")