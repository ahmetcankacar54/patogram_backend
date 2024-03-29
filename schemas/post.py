from pydantic import BaseModel, Field
from datetime import datetime
from models.disease import Disease
from schemas.disease import DiseaseOut
from schemas.user import UserSchema
from schemas.image import ImageBase
from typing import List


class PostBase(BaseModel):
    patient_date_of_birth: str = Field(default=None)
    patient_gender: str = Field(default=None)
    patient_other_disease: str = Field(default=None)
    patient_clinical_story: str = Field(default=None)
    tissue_sample_collection_method: str = Field(default=None)
    tissue_sample_collection_organ: str = Field(default=None)
    pathologic_description: str = Field(default=None)
    macroscopic_findings: str = Field(default=None)
    immunohistochemical_findings: str = Field(default=None)
    histochemical_findings: str = Field(default=None)
    diagnosis: str = Field(default=None)
    comment: str = Field(default=None)
    radiology_report: str = Field(default=None)
    published: bool = True


class CreatePost(PostBase):
    disease_type: int = Field(default=None)
    pass


class PostOut(PostBase):
    id: int = Field(default=None)
    created_at: datetime = Field(default=None)
    images: List[ImageBase]
    isFavorite: bool
    post_owner: UserSchema
    isFollow: bool
    post_disease: DiseaseOut

    class Config:
        orm_mode = True


class DiscoverOut(BaseModel):
    id: int = Field(default=None)
    images: List[ImageBase]

    class Config:
        orm_mode = True
