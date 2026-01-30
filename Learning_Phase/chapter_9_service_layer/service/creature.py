from model.creature import Creature
import fake.creature as data
from typing import Optional

def get_all() -> list[Creature]:
    """Get all creatures."""
    return data.get_all()

def get_one(name: str) -> Optional[Creature]:
    """Get one creature by name."""
    return data.get_one(name)


def create(creature : Creature) -> Creature:
    """Create a new creature."""
    return data.create(creature)

def replace(id, creature: Creature) -> Creature:
    """Replace a creature by id."""
    return data.replace(id, creature)


def modify(id, creature: Creature) -> Creature:
    """Modify a creature by id."""
    return data.modify(id, creature)

def delete(id, creature:Creature) -> bool:
    """Delete a creature by id."""
    return data.delete(id, creature)


