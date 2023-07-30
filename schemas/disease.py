from pydantic import BaseModel, Field


class Disease(BaseModel):
    disease_en: str = Field(default=None)
    disease_tr: str = Field(default=None)

    class Config:
        orm_mode = True


class DiseaseOut(BaseModel):
    id: int = Field(default=None)
    disease_en: str = Field(default=None)
    disease_tr: str = Field(default=None)

    class Config:
        orm_mode = True
