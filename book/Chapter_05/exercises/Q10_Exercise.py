from pydantic import BaseModel, field_validator

class CartPayload(BaseModel):
    item_id: int
    quantity: int

    @field_validator("quantity")
    @classmethod
    def enforce_inventory_limits(cls, v: int) -> int:
        if v > 50:
            raise ValueError("Cart quantity boundary exceeded (Max 50).")
        return v