from sqlalchemy import CheckConstraint, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class Philosopher(Base):
    __tablename__ = "philosopher"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    country: Mapped[str]
    school: Mapped[str]
    birth_year: Mapped[int]
    death_year: Mapped[int]
    catch_phrase: Mapped[str | None]

    __table_args__ = (
        CheckConstraint("birth_year <= death_year", name="valid_life"),
    )


if __name__ == "__main__":
    engine = create_engine("sqlite:///try.db", echo=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add_all([
            Philosopher(name="René Descartes", country="France", birth_year=1596, death_year=1650, school="Rationalism", catch_phrase="I think therefore I am"),
            Philosopher(name="David Hume", country="Scotland", birth_year=1711, death_year=1776, school="Empiricism", catch_phrase="Reason is, and ought only to be the slave of the passions."),
        ])
        session.commit()

        philosophers = session.scalars(select(Philosopher)).all()
        for philosopher in philosophers:
            print(philosopher.name)
