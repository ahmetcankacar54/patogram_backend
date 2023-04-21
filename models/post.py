from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import BaseModel


class Post(BaseModel):
    __tablename__ = "posts"

    disease_type = Column(String, nullable=False)
    tissue_sample_collection_method = Column(String, nullable=False)
    paint_type = Column(String, nullable=False)
    zoom_amount = Column(String, nullable=False)
    patient_age = Column(Integer, nullable=False)
    patient_gender = Column(String, nullable=False)
    patient_other_disease = Column(String, nullable=False)
    clinical_diagnosis = Column(String, nullable=False)
    pathological_diagnosis = Column(String, nullable=False)
    radiology_report = Column(String, nullable=False)
    pathologic_description = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    post_owner = relationship("models.user.User")
    images = relationship(
        "models.image.Image", overlaps="images", back_populates="post")
    thumbnail = relationship(
        "models.image.Image", overlaps="images", back_populates="post_1")
    comments = relationship("models.comment.Comment", back_populates="post")
    favorites = relationship("models.favorite.Favorite",
                             overlaps="favorites", back_populates="post")
    favorite = relationship("models.favorite.Favorite",
                            overlaps="favorites", back_populates="isFavorite")
