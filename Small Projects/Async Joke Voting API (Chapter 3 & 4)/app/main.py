from pyexpat.errors import messages

from fastapi import FastAPI
from fastapi import HTTPException
from typing import Optional
import asyncio

jokes = [
    {
        "id": 1,
        "text": "Why do programmers prefer dark mode? Because light attracts bugs.",
        "category": "programming",
        "votes": 3,
    },
    {
        "id": 2,
        "text": "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'",
        "category": "dad",
        "votes": 0,
    },
]


app = FastAPI()


@app.get("/health")
def health():

    return {"status" : "GOOD"}


## GET/Jokes (with optional category filter)
# Goal: If no category -> return all jokes
# If category is provided -> filter by category.
# optional, query parameter.
#http://127.0.0.1:8000/jokes?category=programming
#http://127.0.0.1:8000/jokes

@app.get("/jokes")
async def list_jokes(category : Optional[str] = None, min_votes : Optional[int] = 0):
    await asyncio.sleep(0.2)

    filtered_jokes = []

    for joke in jokes:
        if joke["votes"] >= min_votes:
            if not category:
                filtered_jokes.append(joke)
            else:
                if joke["category"] == category:
                    filtered_jokes.append(joke)

    if not filtered_jokes:
        raise HTTPException(status_code = 404, detail = "No Jokes Found.")
    return filtered_jokes

@app.get("/jokes/slow")
async def list_jokes_slow():
    await asyncio.sleep(3)
    return jokes

#Path parameter
#Goal: return a single joke or 404
# http://127.0.0.1:8000/jokes/1
@app.get("/jokes/{joke_id}")
async def get_joke(joke_id : int):
    await asyncio.sleep(0.1)
    for joke in jokes:
        if joke["id"] == joke_id:
            return joke


    raise HTTPException(status_code = 404, detail ="Joke not Found.")



# Add POST /jokes to create a new joke
# Create a method POST, Path /jokes
# Request Body (JSON)
# request body should contain
# text:str
# category : str

@app.post("/jokes")
async def create_joke(given_joke : dict):
    await asyncio.sleep(0.1)

    #1. Generate a new id
    new_id = max([joke["id"] for joke in jokes] , default = 0) + 1
    # If the list is not empty find the max id, and then increment by one and this gives us the last id.
    # If the list is empty, create a new id equal to  = 1

    # Build the joke object.
    new_joke = {
        "id":new_id,
        "text":given_joke["text"],
        "category":given_joke["category"],
        "votes":0
    }

    # Save
    jokes.append(new_joke)

    return new_joke


# Delete joke by id
@app.delete("/jokes/{id}")
async def delete_jokes(id : int):
    for index, joke in enumerate(jokes):
        if joke["id"] == id:
            return jokes.pop(index)


    raise HTTPException(status_code = 404 , detail = f"There is no joke with id {id} ")

