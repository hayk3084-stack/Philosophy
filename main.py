from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Argument, Philosopher
from schemas import ArgumentWithConnectionsSchema, PhilosopherSchema, PhilosopherWithArgumentsSchema

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionDep = Annotated[Session, Depends(get_db)]


@app.get("/philosophers", response_model=list[PhilosopherSchema])
def get_all_philosophers(db: SessionDep):
    stmt = select(Philosopher)
    return db.scalars(stmt).all()


@app.get("/philosophers/{philosopher_id}", response_model=PhilosopherWithArgumentsSchema)
def get_philosopher_by_id(philosopher_id: int, db: SessionDep):
    philosopher = db.get(Philosopher, philosopher_id)
    if philosopher is None:
        raise HTTPException(status_code=404, detail="Philosopher not found")
    return philosopher


@app.get("/arguments/{argument_id}", response_model=ArgumentWithConnectionsSchema)
def get_argument_relations(argument_id: int, db: SessionDep):
    argument = db.get(Argument, argument_id)
    if argument is None:
        raise HTTPException(status_code=404, detail="Argument not found")
    return argument
