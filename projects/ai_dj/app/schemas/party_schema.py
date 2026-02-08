from pydantic import BaseModel, Field
from pydantic import ConfigDict
from typing import List
class StrictModel(BaseModel):
    """ Only declared fields are allowed. """
    model_config = ConfigDict(extra = "forbid")



# Request
    
class PartySetRequest(StrictModel):

    theme_of_party:str = Field(
        ...,
        min_length = 20,
        max_length = 4000,
        description = "Customer's theme of the party description in natural language."
    )

    emotional_flow_of_the_songs: List[str] = Field(
        default_factory = list,
        min_length = 2,
        max_length = 5,
        description = "Emotional flow of the party (ordered e.g. 1. Sad, 2. Jazz means first songs are mostly sad second are mostly Jazz "
    )

    duration:int = Field(
        default = 10,
        ge = 10,
        le = 600,
        description = "Customer's duration of the party in minutes. (Greater than 10, less than 600)"
    )




