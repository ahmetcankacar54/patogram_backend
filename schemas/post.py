from pydantic import BaseModel, Field
from datetime import datetime
from schemas.user import UserSchema
from schemas.image import Images
from typing import List
from schemas.favorite import IsFavorite


class PostBase(BaseModel):
    disease_type: str = Field(default=None)
    tissue_sample_collection_method: str = Field(default=None)
    paint_type: str = Field(default=None)
    zoom_amount: str = Field(default=None)
    patient_age: int = Field(default=None)
    patient_gender: str = Field(default=None)
    patient_other_disease: str = Field(default=None)
    clinical_diagnosis: str = Field(default=None)
    pathological_diagnosis: str = Field(default=None)
    radiology_report: str = Field(default=None)
    pathologic_description: str = Field(default=None)
    published: bool = True


class CreatePost(PostBase):
    pass


class PostOut(PostBase):
    id: int = Field(default=None)
    created_at: datetime = Field(default=None)
    # comment: int
    post_owner: int = Field(default=None)
    images: List[Images]
    isFavorite: bool = Field(default=None)
    post_owner: UserSchema

    class Config:
        orm_mode = True
