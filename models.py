from sqlalchemy import CheckConstraint, ForeignKey, UniqueConstraint, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship


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
    arguments: Mapped[list["Argument"]] = relationship(back_populates="philosopher")

    __table_args__ = (
        CheckConstraint("birth_year <= death_year", name="valid_life"),
    )


class Argument(Base):
    __tablename__ = "argument"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    philosopher_id: Mapped[int] = mapped_column(ForeignKey("philosopher.id"))
    philosopher: Mapped["Philosopher"] = relationship(back_populates="arguments")

    __table_args__ = (
        UniqueConstraint("philosopher_id", "name", name="unique_argument_per_philosopher"),
    )


if __name__ == "__main__":
    engine = create_engine("sqlite:///try.db", echo=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        descartes = Philosopher(name="René Descartes", country="France", birth_year=1596, death_year=1650, school="Rationalism", catch_phrase="I think therefore I am")
        senses_argument = Argument(name="Senses argument", philosopher=descartes, description="Descartes' first argument for doubt rests on the unreliability of the senses. Everything he had accepted as most true came to him through the senses, yet the senses have sometimes deceived him. Since it is unwise to fully trust anything that has deceived us even once, he concludes that beliefs based on the senses cannot be accepted as certain.")
        dream_argument = Argument(name="Dream argument", philosopher=descartes, description="The dream argument pushes the doubt further. Even if the senses sometimes deceive us about distant or small things, it seems certain that I am sitting here by the fire, holding this paper. Yet he recalls that in dreams he has been just as convinced of such things while actually lying in bed. Since there are no certain signs by which waking can be distinguished from dreaming, he cannot be sure he is not dreaming right now, and so even his most immediate sensory experiences cannot be accepted as certain.")
        session.add_all([descartes, senses_argument, dream_argument])

        session.commit()

        found_philosopher = session.scalars(select(Philosopher).where(Philosopher.id == 1)).first()
        for argument in found_philosopher.arguments:
            print(argument.name)

        found_argument = session.scalar(select(Argument).where(Argument.name == "Senses argument"))
        print(found_argument.philosopher.name)
