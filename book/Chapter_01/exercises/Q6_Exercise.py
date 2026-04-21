import os
def get_db_url() -> str:
    return os.getenv("DATABASE_URL", "sqlite:///:memory:")