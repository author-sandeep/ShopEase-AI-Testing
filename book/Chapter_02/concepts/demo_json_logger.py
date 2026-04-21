# SPDX-License-Identifier: MPL-2.0
# Concept 3: Structuring Non-Deterministic Payloads - Program 3
# File: demo_json_logger.py
# Purpose: Formats AI test outputs securely into queryable JSON.
# Author: Sandeep Dixit

import json
import logging
import sys
from typing import Dict, Any

class JSONFormatter(logging.Formatter):
    """Custom Formatter to enforce JSON structures."""
    def format(self, record: logging.LogRecord) -> str:
        """Overrides the standard format to yield JSON."""
        try:
            log_data: Dict[str, Any] = {
                "timestamp": self.formatTime(record, self.datefmt),
                "level": record.levelname,
                "logger": record.name,
                "message": record.getMessage()
            }
            # Safely serialize into a single line string
            return json.dumps(log_data)
        except TypeError as e:
            return f'{{"level": "ERROR", "message": "JSON Serialization Failed: {e}"}}'
        finally:
            pass

def run_json_audit() -> None:
    try:
        logger = logging.getLogger("JSON_Audit")
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler(sys.stdout)
        # Attach our custom structured formatter
        handler.setFormatter(JSONFormatter())
        logger.addHandler(handler)

        ai_payload: str = "The user wants a laptop. \n Recommend: Model X."
        logger.info(f"AI Output: {ai_payload}")
    except Exception as e:
        print(f"Audit setup failed: {e}")

if __name__ == "__main__":
    run_json_audit()