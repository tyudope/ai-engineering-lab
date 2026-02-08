from pydantic import ConfigDict, BaseModel, Field
from typing import List


class StrictModel(BaseModel):
    model_config = ConfigDict(extra = "forbid")


class PartySetResponse(StrictModel):

    analyze:str = Field(
        ...,
        min_length=20,
        max_length= 1200,
        description = "Analyzing the song choices gives a reasons.")


    songs:List[str] = Field(
        default_factory=list,
        min_length=3,
        max_length=100,
        description = "Songs that are fit the flow of the party. with their duration besides (The weekend: Party Monster : 3.45)"
    )

    
     
    
