from pydantic import BaseModel
from pydantic import Field

class Book(BaseModel):
    id: int
    name: str = Field(... , max_length=50)
    category:str = Field(..., max_length=10)
    pages:int = Field(..., gt=10, lt=10000)


