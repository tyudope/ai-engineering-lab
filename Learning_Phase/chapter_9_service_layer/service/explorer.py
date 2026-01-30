from model.explorer import Explorer
from fake.explorer import data
from typing import Optional
def get_all() -> list[Explorer]:
    """Get all explorers."""
    return data.get_all()

def get_one(name: str) -> Optional[Explorer]:
    """Get one explorer by name."""
    return data.get_one(name)

def create(explorer : Explorer) -> Explorer:
    """Create a new explorer."""
    return data.create(explorer)

def replace(id, explorer: Explorer) -> Explorer:
    """Replace an explorer by id."""
    return data.replace(id, explorer)

def modify(id, explorer: Explorer) -> Explorer:
    """Modify an explorer by id."""
    return data.modify(id, explorer)

def delete(id, explorer:Explorer) -> bool:
    """Delete an explorer by id."""
    return data.delete(id, explorer)
