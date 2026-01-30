from fastapi import FastAPI
from web import books

app = FastAPI()

# Connect to main application to the subrouter.
app.include_router(books.router)


@app.get("/")
def top():
    return "Welcome to the Books API!"



