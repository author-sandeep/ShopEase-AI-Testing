# SPDX-License-Identifier: MPL-2.0
# Concept: Abstract Base Classes for Test Contracts
# File: core/base_wrapper.py
# Purpose: Defines the strict architectural contract for all ShopEase wrappers.
# Author: Sandeep Dixit

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class BaseShopEaseWrapper(ABC):
    """The foundational contract forcing uniform API execution mechanics."""

    def __init__(self, service_name: str):
        self.service_name: str = service_name
        self.is_connected: bool = False

    @abstractmethod
    def connect(self) -> bool:
        """Mandatory: Establish and verify a secure connection."""
        pass

    @abstractmethod
    def execute(self, payload: Dict[str, Any]) -> Optional[str]:
        """Mandatory: Send the payload and return the string response."""
        pass

    @abstractmethod
    def close(self) -> None:
        """Mandatory: Safely teardown connection and free memory."""
        pass

    def check_status(self) -> str:
        """Shared utility function inherited by all children automatically."""
        try:
            status: str = "ONLINE" if self.is_connected else "OFFLINE"
            return f"Service [{self.service_name}] Status: {status}"
        except Exception as e:
            return f"Status Check Failed: {e}"
        finally:
            pass