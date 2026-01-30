from fastapi import FastAPI
from web import explorer
from web import creature
app = FastAPI()


# Connect the main application to the subrouter
app.include_router(explorer.router)
app.include_router(creature.router)

@app.get("/")
def top():
    return "top here"
