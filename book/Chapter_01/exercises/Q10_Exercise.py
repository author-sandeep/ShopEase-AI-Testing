import pytest
from typing import Generator

class VectorDBMock:
    def open(self): print("Vector DB Open")
    def close(self): print("Vector DB Closed")

@pytest.fixture
def vector_db() -> Generator[VectorDBMock, None, None]:
    db = VectorDBMock()
    try:
        db.open()
        yield db
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()