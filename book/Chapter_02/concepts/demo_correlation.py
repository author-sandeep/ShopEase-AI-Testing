# SPDX-License-Identifier: MPL-2.0
# Concept 5: Contextual Tracing via Correlation IDs - Program 5
# File: demo_correlation.py
# Purpose: Injects unique tracking UUIDs into concurrent logs.
# Author: Sandeep Dixit

import logging
import sys
import uuid
from typing import Dict

def setup_tracing_logger() -> logging.Logger:
    """Configures a logger capable of handling extra context fields."""
    try:
        logger: logging.Logger = logging.getLogger("Tracing")
        logger.setLevel(logging.INFO)

        # Notice the %(correlation_id)s custom variable in the format
        formatter = logging.Formatter(
            '%(asctime)s | [%(correlation_id)s] | %(levelname)s: %(message)s'
        )

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger
    except Exception as e:
        print(f"Tracing logger setup failed: {e}")
        return logging.getLogger("Fallback")
    finally:
        pass

def simulate_test_execution(logger: logging.Logger, test_name: str) -> None:
    """Simulates a test execution needing a unique trace ID."""
    try:
        # Generate a perfectly unique tracking number for this run
        trace_id: str = str(uuid.uuid4())[:8] # Using 8 chars for clean display

        # Inject the trace_id using the 'extra' parameter
        context: Dict[str, str] = {'correlation_id': trace_id}

        logger.info(f"Starting {test_name}", extra=context)
        # Deep logic simulating an AI call
        logger.info("Connecting to AI Model...", extra=context)
        logger.info("Received AI Payload successfully.", extra=context)

    except Exception as e:
        print(f"Test simulation failed: {e}")
    finally:
        pass

if __name__ == "__main__":
    trace_logger = setup_tracing_logger()
    print("Simulating concurrent test execution (Notice the IDs):\n")
    # Both tests run, but their logs can be easily separated by the UUID
    simulate_test_execution(trace_logger, "TC_Login_UI")
    simulate_test_execution(trace_logger, "TC_Cart_AI")