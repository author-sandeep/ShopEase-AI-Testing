# SPDX-License-Identifier: MPL-2.0
# Concept 2: The Python Logging Architecture - Program 2
# File: demo_architecture.py
# Purpose: Implements advanced Logger, Formatter, and Handler separation.
# Author: Sandeep Dixit

import logging
import sys
from typing import Optional

def configure_enterprise_logger(name: str) -> Optional[logging.Logger]:
    """Builds a multi-handler enterprise logger."""
    try:
        # 1. The Reporter (Logger)
        logger: logging.Logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG) # Catch everything at the root

        # Prevent duplicate logs if function is called multiple times
        if logger.hasHandlers():
            logger.handlers.clear()

        # 2. The Editor (Formatter)
        formatter: logging.Formatter = logging.Formatter(
            fmt="[%(name)s] %(levelname)s: %(message)s"
        )

        # 3. The Publisher for Terminal (StreamHandler)
        console_handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO) # Terminal only gets INFO and above
        console_handler.setFormatter(formatter)

        # 4. Attach Publishers to Reporter
        logger.addHandler(console_handler)

        return logger
    except Exception as e:
        print(f"Architecture configuration failed: {e}")
        return None
    finally:
        pass

if __name__ == "__main__":
    adv_logger = configure_enterprise_logger("ShopEase_Engine")
    if adv_logger:
        try:
            # DEBUG will be ignored by the console handler (set to INFO)
            adv_logger.debug("This is hidden tech noise.")
            # INFO will be successfully published
            adv_logger.info("Test framework successfully initialized.")
            adv_logger.error("AI API Key validation failed!")
        except Exception as e:
            print(f"Execution error: {e}")