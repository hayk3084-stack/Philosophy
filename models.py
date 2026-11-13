from typing import Optional

from sqlalchemy import CheckConstraint, ForeignKey, ForeignKeyConstraint, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship




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
    arguments: Mapped[list["Argument"]] = relationship(back_populates="philosopher", passive_deletes=True)
    writings: Mapped[list["Writing"]] = relationship(back_populates="philosopher", passive_deletes=True)

    __table_args__ = (
        CheckConstraint("birth_year <= death_year", name="valid_life"),
    )


class Argument(Base):
    __tablename__ = "argument"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    philosopher_id: Mapped[int] = mapped_column(ForeignKey("philosopher.id", ondelete="CASCADE"))
    philosopher: Mapped["Philosopher"] = relationship(back_populates="arguments", foreign_keys=[philosopher_id])
    writing_id: Mapped[Optional[int]] = mapped_column()
    writing: Mapped[Optional["Writing"]] = relationship(back_populates="arguments", foreign_keys=[writing_id])
    incoming: Mapped[list["ArgumentsConnection"]] = relationship(back_populates="target_arg", foreign_keys="ArgumentsConnection.target_arg_id", passive_deletes=True)
    outgoing: Mapped[list["ArgumentsConnection"]] = relationship(back_populates="source_arg", foreign_keys="ArgumentsConnection.source_arg_id", passive_deletes=True)

    __table_args__ = (
        UniqueConstraint("philosopher_id", "name", name="unique_argument_per_philosopher"),
        ForeignKeyConstraint(
            ["writing_id", "philosopher_id"],
            ["writing.id", "writing.philosopher_id"],
            name="fk_argument_writing_same_philosopher",
        ),
    )




class Writing(Base):
    __tablename__ = "writing"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    kind: Mapped[str]
    publish_year: Mapped[int]
    philosopher_id: Mapped[int] = mapped_column(ForeignKey("philosopher.id", ondelete="CASCADE"))
    philosopher: Mapped["Philosopher"] = relationship(back_populates="writings")
    arguments: Mapped[list["Argument"]] = relationship(back_populates="writing", foreign_keys="Argument.writing_id")

    __table_args__ = (
        CheckConstraint("kind IN ('article', 'book', 'letter')", name="check_kind_allowed"),
        UniqueConstraint("id", "philosopher_id", name="uq_writing_philosopher"),
    )


RELATION_PHRASES = {
    "based_on": "is based on",
    "challenges": "challenges",
    "refutes": "refutes",
}


class ArgumentsConnection(Base):
    __tablename__ = "arg_connection"

    id: Mapped[int] = mapped_column(primary_key=True)
    relation_type: Mapped[str]
    source_arg_id: Mapped[int] = mapped_column(ForeignKey("argument.id", ondelete="CASCADE"))
    target_arg_id: Mapped[int] = mapped_column(ForeignKey("argument.id", ondelete="CASCADE"))
    target_arg: Mapped["Argument"] = relationship(back_populates="incoming", foreign_keys=[target_arg_id])
    source_arg: Mapped["Argument"] = relationship(back_populates="outgoing", foreign_keys=[source_arg_id])

    __table_args__ = (
        CheckConstraint("relation_type IN ('based_on', 'challenges', 'refutes')", name="valid_relation"),
        CheckConstraint("source_arg_id != target_arg_id", name="no_self_connection"),
        UniqueConstraint("relation_type", "source_arg_id", "target_arg_id", name="unique_arg_relation"),
    )

    def __str__(self):
        return f"{self.source_arg.name} {RELATION_PHRASES[self.relation_type]} {self.target_arg.name}"


