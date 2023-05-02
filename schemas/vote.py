from pydantic import BaseModel, Field, conint


class Vote(BaseModel):
    user_id: int = Field(default=None)
    poll_id: int = Field(default=None)
    vote_status: conint(le=1) = Field(default=None)
    isVote: bool = True

    class Config:
        orm_mode = True


class AddVote(BaseModel):
    poll_id: int = Field(default=None)
    post_id: int = Field(default=None)
    vote_status: conint(le=1) = Field(default=None)

    class Config:
        orm_mode = True
