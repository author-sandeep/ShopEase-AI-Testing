# SPDX-License-Identifier: MPL-2.0
# Concept 2: The Singleton Pattern in Testing - Program 2
# File: demo_singleton.py
# Purpose: Ensures heavy test resources are only initialized once.
# Author: Sandeep Dixit

from typing import Optional

class DatabaseConnectionSingleton:
    """Restricts database connection object to a single instance."""

    _instance: Optional['DatabaseConnectionSingleton'] = None

    def __new__(cls, *args, **kwargs):
        """Intercepts object creation to enforce the Singleton rule."""
        if cls._instance is None:
            # Create it exactly once
            cls._instance = super(DatabaseConnectionSingleton, cls).__new__(cls)
            cls._instance._initialize_heavy_resource()
        return cls._instance

    def _initialize_heavy_resource(self) -> None:
        """Simulates an expensive operation like network binding."""
        try:
            self.connection_id: str = "DB_CONN_999"
            print("-> EXECUTED: Heavy Database Connection Established.")
        except Exception as e:
            print(f"Singleton initialization failed: {e}")
        finally:
            pass

    def get_connection_id(self) -> str:
        return self.connection_id

if __name__ == "__main__":
    try:
        print("Test 1: Requesting DB Connection...")
        db1 = DatabaseConnectionSingleton()

        print("Test 2: Requesting DB Connection...")
        db2 = DatabaseConnectionSingleton()

        print(f"DB1 ID: {db1.get_connection_id()}")
        print(f"DB2 ID: {db2.get_connection_id()}")

        # Demonstrating memory identity check
        if db1 is db2:
            print("SUCCESS: Both tests are sharing the exact same Singleton object.")
    except Exception as e:
        print(f"Execution Error: {e}")