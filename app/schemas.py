from pydantic import BaseModel, Field


class ProfileBase(BaseModel):
    name: str
    age: int
    description: str | None = Field(max_length=1000)
    interests: str | None = Field(max_length=300)


class ProfileCreate(BaseModel):
    pass


class Profile(ProfileBase):
    id: int

    class Config:
        orm_mode = True
