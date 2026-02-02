import json
from openai import OpenAI
from app.core.config import settings
from app.core.prompts import DREAM_ANALYSIS_SYSTEM
from app.core.prompt_templates import dream_analysis_user_prompt
from app.schemas.dreams import DreamAnalyzeRequest, DreamAnalyzeResponse

client = OpenAI(api_key=settings.openai_api_key)

class ModelOutputError(Exception):
    pass

def _extract_json(text: str) -> dict:
    """
    Best-effort JSON extraction:
    - If model returns pure JSON -> json.loads works.
    - If model adds text accidentally -> try to slice the first {...} block.
    """
    text = text.strip()

    # Fast path: perfect JSON
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Recovery path: extract the first JSON object
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ModelOutputError("No JSON object found in model output.")

    candidate = text[start:end + 1]
    try:
        return json.loads(candidate)
    except json.JSONDecodeError as e:
        raise ModelOutputError(f"Invalid JSON after extraction: {e}") from e


def analyze_dream(req: DreamAnalyzeRequest) -> DreamAnalyzeResponse:
    user_prompt = dream_analysis_user_prompt(
        dream_text=req.dream_text,
        user_context=req.user_context,
        intensity=req.intensity
    )

    resp = client.responses.create(
        model=settings.openai_model,
        input=[
            {"role": "system", "content": DREAM_ANALYSIS_SYSTEM},
            {"role": "user", "content": user_prompt},
        ],
    )

    raw_text = resp.output_text
    data = _extract_json(raw_text)

    # Hard guarantee: validate against your contract
    try:
        return DreamAnalyzeResponse.model_validate(data)
    except Exception as e:
        raise ModelOutputError(f"Model output failed schema validation: {e}") from e
    


from openai import OpenAI
from app.core.config import settings

# Single shared client
client = OpenAI(api_key=settings.openai_api_key)


def openai_ping() -> str:
    response = client.responses.create(
        model=settings.openai_model,
        input="If you're alive wave your hand.",
        max_output_tokens=16,
    )

    # responses API may return structured output;
    # output_text is the safest shortcut for MVP
    return response.output_text.strip()