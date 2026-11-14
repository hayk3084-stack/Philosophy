from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine
from models import RELATION_PHRASES, Argument, ArgumentsConnection, Base, Philosopher, Writing

PHILOSOPHERS = [
    {
        "name": "René Descartes",
        "country": "France",
        "birth_year": 1596,
        "death_year": 1650,
        "school": "Rationalism",
        "catch_phrase": "I think therefore I am",
    },
    {
        "name": "David Hume",
        "country": "Scotland",
        "birth_year": 1711,
        "death_year": 1776,
        "school": "Empiricism",
        "catch_phrase": "Reason is, and ought only to be, the slave of the passions",
    },
]

WRITINGS = [
    {
        "title": "Meditations",
        "kind": "book",
        "publish_year": 1641,
        "philosopher": "René Descartes",
    },
]

ARGUMENTS = [
    {
        "name": "Senses argument",
        "writing": "Meditations",
        "philosopher": "René Descartes",
        "description": "Descartes' first argument for doubt rests on the unreliability of the senses. Everything he had accepted as most true came to him through the senses, yet the senses have sometimes deceived him. Since it is unwise to fully trust anything that has deceived us even once, he concludes that beliefs based on the senses cannot be accepted as certain.",
    },
    {
        "name": "Dream argument",
        "writing": "Meditations",
        "philosopher": "René Descartes",
        "description": "The dream argument pushes the doubt further. Even if the senses sometimes deceive us about distant or small things, it seems certain that I am sitting here by the fire, holding this paper. Yet he recalls that in dreams he has been just as convinced of such things while actually lying in bed. Since there are no certain signs by which waking can be distinguished from dreaming, he cannot be sure he is not dreaming right now, and so even his most immediate sensory experiences cannot be accepted as certain.",
    },
]

CONNECTIONS = [
    {
        "source_arg": "Dream argument",
        "relation_type": "based_on",
        "target_arg": "Senses argument",
    },
]


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
        philosophers_by_name = {}
        writings_by_title = {}
        arguments_by_name = {}

        for philosopher_data in PHILOSOPHERS:
            philosopher = get_or_create_philosopher(session, **philosopher_data)
            philosophers_by_name[philosopher.name] = philosopher
        for writing_data in WRITINGS:
            writing = get_or_create_writing(session, title=writing_data["title"], kind=writing_data["kind"], publish_year=writing_data["publish_year"], philosopher=philosophers_by_name[writing_data["philosopher"]])
            writings_by_title[writing.title] = writing
        for argument_data in ARGUMENTS:
            writing_title = argument_data.get("writing")
            argument = get_or_create_argument(session, name=argument_data["name"], writing=writings_by_title.get(writing_title), philosopher=philosophers_by_name[argument_data["philosopher"]], description=argument_data["description"])
            arguments_by_name[argument.name] = argument
        for connection_data in CONNECTIONS:
            connection = get_or_create_connection(session, source_arg=arguments_by_name[connection_data["source_arg"]], relation_type=connection_data["relation_type"], target_arg=arguments_by_name[connection_data["target_arg"]])
        session.commit()
