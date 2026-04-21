from pydantic import Field
from typing import Optional
presence_penalty: Optional[float] = Field(default=0.0, ge=-2.0, le=2.0)