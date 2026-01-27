from fastapi import APIRouter, HTTPException
from model.explorer import Explorer
from typing import Optional
import data.explorer as service
from errors import Duplicate, Missing

router = APIRouter(prefix = "/explorer")
@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name:str) -> Optional[Explorer]:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail = exc.msg)



# all the remaining endpoints do nothing yet:
@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
    


@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
    try:
        service.modify(explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail = exc.msg)



    

@router.put("/")
def replace(explorer: Explorer) -> Explorer:
    return service.replace(explorer)

@router.delete("/{name}",status_code=204)
def delete(name: str):
   try:
       return service.delete(name)
   except Missing as exc:
       raise HTTPException(status_code=404, detail = exc.msg)