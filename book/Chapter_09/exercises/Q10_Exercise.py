import pytest
from pydantic import BaseModel, Field, ValidationError
from typing import Optional

class PenaltySchema(BaseModel):
    freq: Optional[float] = Field(default=0.0, ge=-2.0, le=2.0)

@pytest.mark.parametrize("bad_val", [3.0, -5.0])
def test_penalty_boundaries_fail(bad_val):
    with pytest.raises(ValidationError):
        PenaltySchema(freq=bad_val)

def test_penalty_boundaries_pass():
    valid = PenaltySchema(freq=None)
    assert valid.freq is None, "Optional 'None' evaluation failed."