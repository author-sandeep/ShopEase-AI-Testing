# SPDX-License-Identifier: MPL-2.0
# Concept 1: The Necessity of AI Audit Trails - Program 1
# File: demo_audit_trail.py
# Purpose: Replaces print statements with basic persistent logging.
# Author: Sandeep Dixit

import logging
import os
from typing import Optional

def setup_basic_audit() -> Optional[logging.Logger]:
    """Configures a basic file-based audit trail."""
    try:
        # Create a directory if it does not exist
        os.makedirs("logs", exist_ok=True)

        # Configure the root logger to write to a file
        logging.basicConfig(
            filename=os.path.join("logs", "shopease_basic.log"),
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logger: logging.Logger = logging.getLogger("AI_Audit")
        return logger
    except OSError as e:
        print(f"CRITICAL: Failed to create log directory: {e}")
        return None
    finally:
        pass

if __name__ == "__main__":
    audit_logger = setup_basic_audit()
    if audit_logger:
        try:
            audit_logger.info("TEST CASE START: TC_Login_01")
            audit_logger.info("AI PROMPT: 'Generate a welcome message.'")
            # Simulating AI execution...
            audit_logger.info("AI RESPONSE: 'Welcome to ShopEase!'")
            print("Audit trail successfully written to logs/shopease_basic.log")
        except Exception as e:
            print(f"Logging execution failed: {e}")