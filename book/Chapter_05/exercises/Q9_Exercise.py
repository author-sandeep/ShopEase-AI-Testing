from pydantic import BaseModel, Field
class SecureAPI(BaseModel):
    api_key: str = Field(min_length=16)