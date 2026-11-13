from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine
from models import RELATION_PHRASES, Argument, ArgumentsConnection, Base, Philosopher, Writing


def get_or_create_philosopher(session: Session, name: str, country: str, birth_year: int, death_year: int, school: str, catch_phrase: str | None) -> Philosopher:
    find_philosopher = session.scalar(select(Philosopher).where(Philosopher.name == name))
    if find_philosopher is None:
        philosopher = Philosopher(name=name, country=country, birth_year=birth_year, death_year=death_year, school=school, catch_phrase=catch_phrase)
        session.add(philosopher)
        return philosopher
    else:
        print(f"{name} already exists")
        return find_philosopher


def get_or_create_writing(session: Session, title: str, kind: str, publish_year: int, philosopher: Philosopher) -> Writing:
    find_writing = session.scalar(select(Writing).where(Writing.title == title, Writing.philosopher == philosopher))
    if find_writing is None:
        writing = Writing(title=title, kind=kind, publish_year=publish_year, philosopher=philosopher)
        session.add(writing)
        return writing
    else:
        print(f"{title} already exists")
        return find_writing


def get_or_create_argument(session: Session, name: str, description: str, philosopher: Philosopher, writing: Writing | None = None) -> Argument:
    find_argument = session.scalar(select(Argument).where(Argument.name == name, Argument.philosopher == philosopher))
    if find_argument is None:
        argument = Argument(name=name, description=description, philosopher=philosopher, writing=writing)
        session.add(argument)
        return argument
    else:
        print(f"{name} already exists")
        return find_argument

def get_or_create_connection(session: Session, source_arg: Argument, relation_type: str, target_arg: Argument) -> ArgumentsConnection:
    find_connection = session.scalar(select(ArgumentsConnection).where(ArgumentsConnection.source_arg == source_arg, ArgumentsConnection.relation_type == relation_type, ArgumentsConnection.target_arg == target_arg))
    if find_connection is None:
        arg_connection = ArgumentsConnection(source_arg=source_arg, relation_type=relation_type, target_arg=target_arg)
        session.add(arg_connection)
        return arg_connection
    else:
        print(f"The {source_arg.name} {RELATION_PHRASES[relation_type]} {target_arg.name} connection already exists")
        return find_connection


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        descartes = get_or_create_philosopher(session, name="René Descartes", country="France", birth_year=1596, death_year=1650, school="Rationalism", catch_phrase="I think therefore I am")
        meditation = get_or_create_writing(session, title="Meditation", kind="book", publish_year=1641, philosopher=descartes)
        senses_argument = get_or_create_argument(session, name="Senses argument", writing=meditation, philosopher=descartes, description="Descartes' first argument for doubt rests on the unreliability of the senses. Everything he had accepted as most true came to him through the senses, yet the senses have sometimes deceived him. Since it is unwise to fully trust anything that has deceived us even once, he concludes that beliefs based on the senses cannot be accepted as certain.")
        dream_argument = get_or_create_argument(session, name="Dream argument", writing=meditation, philosopher=descartes, description="The dream argument pushes the doubt further. Even if the senses sometimes deceive us about distant or small things, it seems certain that I am sitting here by the fire, holding this paper. Yet he recalls that in dreams he has been just as convinced of such things while actually lying in bed. Since there are no certain signs by which waking can be distinguished from dreaming, he cannot be sure he is not dreaming right now, and so even his most immediate sensory experiences cannot be accepted as certain.")
        dream_sense_connection = get_or_create_connection(session, source_arg=dream_argument, relation_type="based_on", target_arg=senses_argument)
        session.commit()
