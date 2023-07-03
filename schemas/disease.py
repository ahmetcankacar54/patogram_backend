from pydantic import BaseModel, Field, conint
from database.configuration import Base


class Disease(BaseModel):
    disease_en: str = Field(default=None)
    disease_tr: str = Field(default=None)

    class Config:
        orm_mode = True


class MainpageDiseaseOut(Disease):
    id: int = Field(default=None)

    class Config:
        orm_mode = True
