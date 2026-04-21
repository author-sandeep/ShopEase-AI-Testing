from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    product_name: str
    discount_code: Optional[str] = None