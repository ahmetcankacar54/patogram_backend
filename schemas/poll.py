from pydantic import BaseModel, Field


class PollBase(BaseModel):
    id: int = Field(default=None)
    user_id: int = Field(default=None)
    post_id: int = Field(default=None)
    item: str = Field(default=None)
    isChosen: bool = Field(default=None)

    class Config:
        orm_mode = True


class PollCreate(BaseModel):
    item: str = Field(default=None)
    isChosen: bool = Field(default=None)

    class Config:
        orm_mode = True


class GetPollResponseModel(PollBase):
    percentage: float = Field(default=None)

    class Config:
        orm_mode = True
