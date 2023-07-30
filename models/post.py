from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import BaseModel


class Post(BaseModel):
    __tablename__ = "posts"

    disease_type = Column(
        Integer, ForeignKey("diseases.id", ondelete="CASCADE"), nullable=False
    )
    patient_date_of_birth = Column(String, nullable=False)
    patient_gender = Column(String, nullable=False)
    patient_other_disease = Column(String, nullable=False)
    patient_clinical_story = Column(String, nullable=False)
    tissue_sample_collection_method = Column(String, nullable=False)
    tissue_sample_collection_organ = Column(String, nullable=False)
    pathologic_description = Column(String, nullable=False)
    macroscopic_findings = Column(String, nullable=False)
    immunohistochemical_findings = Column(String, nullable=False)
    histochemical_findings = Column(String, nullable=False)
    diagnosis = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    radiology_report = Column(String, nullable=True)
    published = Column(Boolean, server_default="True", nullable=False)
    owner_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    post_disease = relationship("models.disease.Disease")
    post_owner = relationship("models.user.User")
    images = relationship(
        "models.image.Image", overlaps="images", back_populates="post"
    )
    thumbnail = relationship(
        "models.image.Image", overlaps="images", back_populates="post_1"
    )
    comments = relationship("models.comment.Comment", back_populates="post")
    favorites = relationship("models.favorite.Favorite", back_populates="post")
    polls = relationship("models.poll.Poll", back_populates="post")
    votes = relationship("models.vote.Vote", back_populates="post")
    follows = relationship("models.case_follow.Follow", back_populates="post")
