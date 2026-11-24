from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Philosopher
from schemas import PhilosopherSchema

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


@app.get("/philosophers/{philosopher_id}", response_model=PhilosopherSchema)
def get_philosopher_by_id(philosopher_id: int, db: SessionDep):
    philosopher = db.get(Philosopher, philosopher_id)
    if philosopher is None:
        raise HTTPException(status_code=404, detail="Philosopher not found")
    return philosopher
