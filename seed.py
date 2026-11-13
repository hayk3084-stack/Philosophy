from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine
from models import Argument, ArgumentsConnection, Base, Philosopher, Writing


def get_or_create_philosopher(session: Session, philosopher: Philosopher):
    find_philosopher = session.scalar(select(Philosopher).where(Philosopher.name == philosopher.name))
    if find_philosopher is None:
        session.add(philosopher)
        return philosopher
    else:
        print(f"{philosopher.name} already exists")
        return find_philosopher


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        descartes = Philosopher(name="René Descartes", country="France", birth_year=1596, death_year=1650, school="Rationalism", catch_phrase="I think therefore I am")
        descartes = get_or_create_philosopher(session, descartes)
        session.commit()
