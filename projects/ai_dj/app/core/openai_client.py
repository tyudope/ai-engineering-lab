from openai import OpenAI
from app.core.config import settings
import json
from app.schemas.party_schema import PartySetRequest
from app.core.prompts import DJ_PARTY_SYSTEM
from app.core.prompt_templates import dj_songs_customer_prompt
from app.schemas.ai_response_schema import PartySetResponse

client = OpenAI(api_key = settings.openai_api_key)




class ModelOutputError(Exception):
    pass


def _extract_json(text : str) -> dict:
    """
    Best-effor JSON extraction:
    - If model returns pure JSON -> json.loads works.
    - If model adds text accidentally -> try to silce the first {...} block.
    
    """

    text = text.strip()


    # Fast path: perfect JSON
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass


    # Recovery path : extract the first JSON object
    start = text.find("{")
    end = text.rfind("}") # .rfind() -> return the highest index of given parameter.

    if start == -1 or end == -1 or end <= start:
        raise ModelOutputError("No JSON object found in model output.")
    
    candidate = text[start:end + 1]
    try:
        return json.loads(candidate)
    except json.JSONDecodeError as e:
        raise ModelOutputError(f"Invalid JSON after extraction {e}") from e
    


def create_playlist(request: PartySetRequest) -> PartySetResponse:
    user_prompt = dj_songs_customer_prompt(
        theme_of_party=request.theme_of_party,
        emotional_flow_of_the_songs=request.emotional_flow_of_the_songs,
        duration=request.duration
        )
    

    response = client.responses.create(
        model = settings.openai_model,
        input = [
            {"role":"system","content": DJ_PARTY_SYSTEM},
            {"role":"user","content":user_prompt},
        ]
    )

    # Use the SDK-provided shortcut which already concatenates message text.
    # This avoids indexing ResponseOutputItem objects like dicts.
    raw_text = response.output_text or ""

    data = _extract_json(raw_text)

    # Hard guarantee: validate against your model
    try:
        return PartySetResponse.model_validate(data)
    except Exception as e:
        raise ModelOutputError(f"Model output failed schema validation: {e}") from e






def openai_test() -> str:
    """
    Test of the API Connection.
    """
    response = client.responses.create(
        model = settings.openai_model,
        input="Hey, I am developing a program this is the first test call to you.",
        max_output_tokens = 16,
    )

    # responses API may return structured output:
    # output_text is the safest shortcut.
    return response.output_text.strip()
 
