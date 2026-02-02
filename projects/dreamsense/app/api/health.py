from fastapi import APIRouter, HTTPException
from openai import AuthenticationError, RateLimitError, APIConnectionError, BadRequestError
from app.core.openai_client import openai_ping

router = APIRouter(prefix="/health", tags=["health"])

@router.get("")
def health():
    return {"status": "ok"}

@router.get("/openai")
def health_openai():
    try:
        out = openai_ping()
        # even if model replies "ok." or something, we still know the key worked
        return {"status": "ok", "openai_reply": out}
    except AuthenticationError:
        # invalid key / wrong org / revoked
        raise HTTPException(status_code=401, detail="OpenAI authentication failed (check API key).")
    except RateLimitError:
        raise HTTPException(status_code=429, detail="OpenAI rate limit hit (billing/limits).")
    except BadRequestError as e:
        # e.g. invalid model name
        raise HTTPException(status_code=400, detail=f"OpenAI bad request: {str(e)}")
    except APIConnectionError:
        raise HTTPException(status_code=503, detail="OpenAI connection error (network/DNS).")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")