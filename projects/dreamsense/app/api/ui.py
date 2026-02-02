from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.schemas.dreams import DreamAnalyzeRequest
from app.core.openai_client import analyze_dream, ModelOutputError

router = APIRouter(tags=["ui"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Default values for form fields
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "default_intensity": 3},
    )


@router.post("/ui/analyze", response_class=HTMLResponse)
def ui_analyze(
    request: Request,
    dream_text: str = Form(...),
    user_context: str = Form(""),
    intensity: int = Form(3),
):
    # Build request object (Pydantic validation still applies here)
    try:
        req = DreamAnalyzeRequest(
            dream_text=dream_text,
            user_context=(user_context.strip() or None),
            intensity=intensity,
        )
    except Exception as e:
        # Form data invalid (too short, etc.)
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "title": "Invalid input",
                "message": str(e),
            },
            status_code=400,
        )

    try:
        result = analyze_dream(req)
        return templates.TemplateResponse(
            "result.html",
            {"request": request, "result": result},
        )

    except ModelOutputError as e:
        # Model failed JSON/schema contract
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "title": "Model output error",
                "message": str(e),
            },
            status_code=502,
        )
    except Exception as e:
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "title": "Server error",
                "message": "Unexpected error occurred.",
            },
            status_code=500,
        )