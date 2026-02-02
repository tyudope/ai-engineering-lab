from fastapi import APIRouter, HTTPException
from app.schemas.dreams import DreamAnalyzeRequest, DreamAnalyzeResponse
from app.core.openai_client import analyze_dream, ModelOutputError


router = APIRouter(prefix="/dreams", tags=["dreams"])



@router.post("/analyze", response_model= DreamAnalyzeResponse)
def analyze(req: DreamAnalyzeRequest):
    try:
        return analyze_dream(req)
    except ModelOutputError as e:
        # model returned invalid or unsafe output
        raise HTTPException(status_code= 502, detail=str(e))
    except Exception as e:
        # Unexpected error.
        raise HTTPException(status_code=500, detail = "Internal Server Error.")