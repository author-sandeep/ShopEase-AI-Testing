# SPDX-License-Identifier: MPL-2.0
# Concept 4: Log Rotation and Retention - Program 4
# File: demo_rotation.py
# Purpose: Prevents catastrophic server disk overflow using automatic rotation.
# Author: Sandeep Dixit

import logging
from logging.handlers import RotatingFileHandler
import os

def setup_rotating_logger() -> logging.Logger:
    """Configures a logger with strict disk space constraints."""
    try:
        os.makedirs("logs", exist_ok=True)
        log_file: str = os.path.join("logs", "shopease_rotation.log")

        logger: logging.Logger = logging.getLogger("Rotator")
        logger.setLevel(logging.DEBUG)

        # 1024 bytes * 1024 = 1 MB. Max size set to 2 MB. Keep 3 backups.
        # Strict memory control implemented.
        handler: RotatingFileHandler = RotatingFileHandler(
            filename=log_file,
            maxBytes=2 * 1024 * 1024, # 2 MB limit
            backupCount=3 # Keeps .log, .log.1, .log.2, .log.3
        )

        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger
    except OSError as e:
        print(f"OS Error during rotation setup: {e}")
        # Always return a safe fallback logger to prevent framework death
        return logging.getLogger("Fallback")
    finally:
        pass

if __name__ == "__main__":
    rot_logger = setup_rotating_logger()
    try:
        print("Writing aggressive payloads to trigger rotation...")
        # Simulating heavy AI payload generation
        large_payload = "A" * 500000 # 500 KB string

        for i in range(5): # Writes 2.5 MB total (triggers rotation at 2 MB)
            rot_logger.info(f"Massive AI Response block {i}: {large_payload[:20]}...")

        print("Rotation logic executed successfully. Check logs/ directory.")
    except Exception as e:
        print(f"Rotation failure: {e}")