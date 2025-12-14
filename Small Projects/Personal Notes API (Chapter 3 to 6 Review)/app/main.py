
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from fastapi import Header
from fastapi import Depends
import asyncio
from datetime import datetime
from typing import Optional





# STEP 1. Create the Note Class
class Note(BaseModel):

    id:int
    title: str = Field(..., min_length = 2, max_length=10)
    content: str= Field(..., min_length = 2, max_length=148)
    tags : list[str] = Field(..., min_length = 1, max_length=5)
    created_at : datetime
    updated_at : datetime = Field(default_factory=datetime.now)

# Add an input model: NoteIn
# we define a simple model for the request body:
class NoteIn(BaseModel):
    title : str = Field(..., min_length= 2, max_length=10)
    content: str = Field(..., min_length= 2, max_length=148)
    tags : list[str]  = Field(..., min_length=1, max_length=5)



note_1 = Note(id = 1, title="ML note", content = "To perform ridge/lasso regression you have to normalize the data first.", tags = ["ML","REG"], created_at=datetime.now())
note_2 = Note(id = 2 , title="Math" , content = "Study calculus for 2 hours ", tags = ["Math","Uni"], created_at=datetime.now())
note_3 = Note(id = 3, title= "AI" , content = "Study AI Engineering from Chip Huyen for 2 hours" , tags = ["ML","AI","BOOK"] , created_at=datetime.now())

notes = [
    note_1,
    note_2,
    note_3
]


# Create a fake dependency.
def get_current_user(x_user : str = Header(None)):
    if not x_user:
        raise HTTPException(status_code = 401, detail = "Unauthorized: X-User header missing")

    return {"username": x_user}


# STEP 2.
# Create the FastAPI application
app = FastAPI()



# STEP 3.
# CRUD (CREATE (POST) , Read (GET), UPDATE (PUT) , DELETE (DELETE))

# Read all notes, Optionally you can sort it or filter with the given tag .
@app.get("/notes")
async def read_all_notes(user = Depends(get_current_user),tag : Optional[str] = None, sort : Optional[str] = "asc"):
    await asyncio.sleep(0.5)
    results = notes
    # if tag is provided filter by tag
    if tag:
        # Filter by tag using list comprehensions
        results = [n for n in results if tag in n.tags]

    if sort:
        sort = sort.lower() # make it lowercase
        if sort == "asc":
            results = sorted(results, key = lambda n : n.created_at)
        elif sort == "desc":
            results = sorted(results, key = lambda n : n.created_at, reverse = True)
        else:
            raise HTTPException(status_code = 400, detail = "Invalid sort type.")


    return results


# Read notes by given id
# You CANNOT have two endpoints with the same path.
@app.get("/notes/{user_id}")
async def read_notes_tag(user_id :int):
    await asyncio.sleep(0.1)
    read_notes = []
    for note in notes:
        if note.id == user_id:
            read_notes.append(note)

    if not read_notes:
        raise HTTPException(status_code=404, detail = "No notes found.")


    return read_notes


# Create a new Note
@app.post("/notes", response_model = Note)
async def create_note(note_in : NoteIn) -> Note:

    # Generate new id, if id is not exist start from 1, if there are notes, find the last node (max id) and plus 1
    new_id = max([note.id for note in notes]) + 1

    # Create time stamps
    now = datetime.now()

    # Build note object from NoteIn
    new_note = Note(
        id = new_id,
        title = note_in.title,
        content = note_in.content,
        tags = note_in.tags,
        created_at=now
    )
    notes.append(new_note)
    await asyncio.sleep(0.1)
    return new_note


# Delete note
@app.delete("/delete/{note_id}")
async def delete_note(note_id : int):
    for index, note in enumerate(notes):
        if note.id == note_id:
            return notes.pop(index)

    raise HTTPException(status_code = 404,detail = "Provided note_id is not appear in the database")



# Update note by id
@app.put("/notes/{note_id}", response_model = Note)
async def update_note(note_id : int, note_in : NoteIn) -> Note:
    # Simulate DB Latency
    await asyncio.sleep(0.4)

    for index, note in enumerate(notes):
        if note_id == note.id:
            now = datetime.now()

            updated_note = Note(
                id = note.id,
                title = note_in.title,
                content = note_in.content,
                tags = note_in.tags,
                created_at=note.created_at,
                updated_at=now
            )
            notes[index] = updated_note
            return updated_note

    raise HTTPException(status_code=400, detail=f"No note found with id {note_id}")
    # 400 -> Bad Request.