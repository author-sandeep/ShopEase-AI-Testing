from pydantic import BaseModel
class AIAnalysis(BaseModel):
    intent: str
    is_shopping_related: bool
    confidence: float