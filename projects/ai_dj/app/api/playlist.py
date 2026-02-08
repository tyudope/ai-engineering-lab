from fastapi import APIRouter, HTTPException
from app.schemas.ai_response_schema import PartySetResponse
from app.schemas.party_schema import PartySetRequest
from app.core.openai_client import create_playlist, ModelOutputError


router = APIRouter(prefix = "/dj", tags = ["dj"])


@router.post("/create_playlist", response_model = PartySetResponse)
def create(request : PartySetRequest):
    try:
        return create_playlist(request)
    except ModelOutputError as e:
        # model returned invalid or unsafe output
        raise HTTPException(status_code= 502, detail=str(e))
    except Exception as e:
        # Temporary debug detail: surface the exception to identify the root cause.
        raise HTTPException(status_code=500, detail=f"Unhandled error: {type(e).__name__}: {e}")
