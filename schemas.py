from pydantic import BaseModel, ConfigDict

from models import RelationType


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class PhilosopherSummarySchema(BaseSchema):
    id: int
    name: str


class PhilosopherSchema(BaseSchema):
    id: int
    name: str
    country: str
    school: str
    birth_year: int
    death_year: int
    catch_phrase: str | None


class ArgumentSchema(BaseSchema):
    id: int
    name: str
    description: str


class ArgumentSummarySchema(BaseSchema):
    id: int
    name: str
    philosopher: PhilosopherSummarySchema


class IncomingConnectionSchema(BaseSchema):
    relation_type: RelationType
    source_arg: ArgumentSummarySchema


class OutgoingConnectionSchema(BaseSchema):
    relation_type: RelationType
    target_arg: ArgumentSummarySchema


class PhilosopherWithArgumentsSchema(PhilosopherSchema):
    arguments: list[ArgumentSchema]


class ArgumentWithConnectionsSchema(ArgumentSchema):
    incoming: list[IncomingConnectionSchema]
    outgoing: list[OutgoingConnectionSchema]
