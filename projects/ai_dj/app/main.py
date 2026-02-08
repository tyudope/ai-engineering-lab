from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.core.openai_client import openai_test
from app.api.playlist import router as AIRouter



app = FastAPI(title = "DJ For your party")

app.include_router(AIRouter)

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def health():
    return {"status" : "ok"}

@app.get("/ui", response_class=HTMLResponse)
def ui():
    index_path = STATIC_DIR / "index.html"
    return index_path.read_text(encoding="utf-8")


@app.get("/ai")
def ai_test():
    return {"status AI" : openai_test()}
