from pydantic import BaseModel

class NumbersRequest(BaseModel):
    numbers: list[int]