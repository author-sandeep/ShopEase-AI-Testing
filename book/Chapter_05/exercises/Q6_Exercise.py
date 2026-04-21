from pydantic import field_validator
@classmethod
@field_validator("score")
def validate_score(cls, v):
    if v <= 0:
        raise ValueError("Score must be greater than zero.")
    return v