from pydantic import BaseModel, Field

class Creature(BaseModel):
    name: str = Field(..., min_length=2 )
    country : str = Field(... , min_length = 1, max_length=3)
    area : str
    description: str = Field(..., min_length=4, max_length = 20)
    aka: str


thing = Creature(
    name = "Yeti",
    country = "CN",
    area = "Himalayas",
    description= "Hirsute Himalayan",
    aka = "Abominable Snowman"
)
print("Name is" , thing.name)
