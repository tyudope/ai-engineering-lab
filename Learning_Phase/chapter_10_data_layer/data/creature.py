from typing import Optional
from .init import curs
from model.creature import Creature

# Create table once
curs.execute("""
CREATE TABLE IF NOT EXISTS creature (
    name TEXT PRIMARY KEY,
    country TEXT,
    area TEXT,
    description TEXT,
    aka TEXT
)
""")

def row_to_model(row: tuple) -> Creature:
    # row is (name, country, area, description, aka)
    name, country, area, description, aka = row
    return Creature(
        name=name,
        country=country,
        area=area,
        description=description,
        aka=aka,
    )

def model_to_dict(creature: Creature) -> dict:
    # Pydantic v2 best practice
    return creature.model_dump() if creature else None

def get_one(name: str) -> Optional[Creature]:
    qry = "SELECT * FROM creature WHERE name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row) if row else None

def get_all() -> list[Creature]:
    qry = "SELECT * FROM creature"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(creature: Creature) -> Creature:
    qry = """
    INSERT INTO creature (name, country, area, description, aka)
    VALUES (:name, :country, :area, :description, :aka)
    """
    params = model_to_dict(creature)
    curs.execute(qry, params)
    
    return get_one(creature.name)

def modify(name: str, creature: Creature) -> Optional[Creature]:
    qry = """
    UPDATE creature
    SET country = :country,
        area = :area,
        description = :description,
        aka = :aka
    WHERE name = :name_orig
    """
    params = model_to_dict(creature)
    params["name_orig"] = name
    curs.execute(qry, params)
    return get_one(name)

def replace(name: str, creature: Creature) -> Optional[Creature]:
    # "PUT replace" pattern (simple approach):
    # delete then insert, or update all fields. We'll update all fields here.
    qry = """
    UPDATE creature
    SET country = :country,
        area = :area,
        description = :description,
        aka = :aka
    WHERE name = :name_orig
    """
    params = model_to_dict(creature)
    params["name_orig"] = name
    curs.execute(qry, params)
    return get_one(name)

def delete(name: str) -> bool:
    qry = "DELETE FROM creature WHERE name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    return curs.rowcount > 0