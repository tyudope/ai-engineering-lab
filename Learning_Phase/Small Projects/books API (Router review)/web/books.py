from model.book import Book 
from fake_data import data as service
from fastapi import APIRouter
from typing import Optional
from fastapi import HTTPException


router = APIRouter(prefix = "/books")

@router.get("/")
def get_all() -> list[Book]:
    books = service.get_all()
    if books is None:
        raise HTTPException(status_code=404, detail="No books found")
    return books


@router.get("/{name}")
def get_one(name:str) -> Optional[Book]:
    book = service.get_one(name)
    if book is None:
        raise HTTPException(status_code=404, detail=f"No books found with that name {name}")
    return book


@router.get("/category/{category}")
def get_by_category(category:str) -> list[Book]:
    books =  service.get_by_category(category)
    print(books)
    if books is None:
        raise HTTPException(status_code=404, detail=f"No books found in that category {category}")

    return books