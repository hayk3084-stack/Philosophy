from pydantic import BaseModel, ConfigDict


class PhilosopherSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    country: str
    school: str
    birth_year: int
    death_year: int
    catch_phrase: str | None
