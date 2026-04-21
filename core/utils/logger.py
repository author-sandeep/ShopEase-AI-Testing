# SPDX-License-Identifier: MPL-2.0
# Concept: Advanced Logging Architecture
# File: core/logger.py
# Purpose: Centralized enterprise logging generator with rotation and context.
# Author: Sandeep Dixit

import logging
from logging.handlers import RotatingFileHandler
import os
import sys
from typing import Optional

def get_enterprise_logger(module_name: str) -> Optional[logging.Logger]:
    """Generates a highly robust logger for the ShopEase framework."""
    try:
        logger: logging.Logger = logging.getLogger(module_name)
        logger.setLevel(logging.DEBUG)

        # Prevent handler duplication across Pytest runs
        if logger.hasHandlers():
            logger.handlers.clear()

        # Terminal Handler (Clean, concise)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            '[%(name)s] %(levelname)s: %(message)s'
        )
        console_handler.setFormatter(console_formatter)

        # File Handler (Deep debug, rotated)
        os.makedirs("logs", exist_ok=True)
        file_path: str = os.path.join("logs", "shopease_core.log")

        # 5 MB limit, 3 backups strictly enforced
        file_handler = RotatingFileHandler(
            filename=file_path,
            maxBytes=5 * 1024 * 1024,
            backupCount=3
        )
        file_handler.setLevel(logging.DEBUG)

        # Note: %(correlation_id)s requires the 'extra' dict on execution
        file_formatter = logging.Formatter(
            '%(asctime)s | [%(name)s] | Trace: %(correlation_id)s | %(levelname)s | %(message)s'
        )
        file_handler.setFormatter(file_formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger
    except OSError as e:
        print(f"CRITICAL: Failed to initialize log directory: {e}")
        return None
    finally:
        pass