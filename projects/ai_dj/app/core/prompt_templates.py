from typing import List
from app.schemas.ai_response_schema import PartySetResponse

def dj_songs_customer_prompt(theme_of_party:str, 
                             emotional_flow_of_the_songs:List[str],
                               duration:int) -> str:
    
    schema_json = PartySetResponse.model_json_schema()


    return f"""
    You will analyze the theme of the party and emotional flow of the songs with the duration of the party, and return the playlist that fits to the party.


    Theme of the Party:
    {theme_of_party}

    Emotional Flow of the Songs:
    {emotional_flow_of_the_songs}

    Duration of the party:
    {duration}

    Return JSON that matches this JSON Schema exactly:
    {schema_json}


    Remember:
        - Soft language
        - Don't hallucinate
        - Give reasons in 3-5 short sentences (max 1200 characters total)
    """
