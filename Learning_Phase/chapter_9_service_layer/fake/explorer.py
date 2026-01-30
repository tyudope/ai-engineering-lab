from model.explorer import Explorer
from typing import Optional

_explorers = [
Explorer(name="Claude Hande",
country="FR",
description="Scarce during full moons"),

Explorer(name="Noah Weiser",
country="DE",
description="Myopic machete man"),
]


def get_all() -> list[Explorer]:
    """Return all explorers."""
    return _explorers


def get_one(name: str) -> Optional[Explorer]:
    """Return explorer by given Name."""
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
        
    return None


# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _explorer list:
def create(explorer: Explorer) -> Explorer:
    '''Create an explorer'''
    return explorer

def modify(explorer : Explorer) -> Explorer:
    '''Partially modify an explorer'''
    return explorer

def replace(explorer : Explorer) -> Explorer:
    '''Completely replace an explorer'''
    return explorer

def delete(explorer : Explorer) -> bool:
    '''Delete an explorer; return None if it existed.'''
    return None


