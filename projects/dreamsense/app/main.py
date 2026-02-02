from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.dreams import router as dreams_router
from app.api.health import router as health_router
from app.api.ui import router as ui_router


app = FastAPI(title = "DreamSense", version = "0.1.0")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(health_router)
app.include_router(dreams_router)
app.include_router(ui_router)