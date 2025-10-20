from pydantic import BaseModel, Field


class ProfileBase(BaseModel):
    name: str
    age: int
    description: str | None = Field(default=None, max_length=1000)
    interests: str | None = Field(default=None, max_length=300)


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    id: int

    class Config:
        orm_mode = True
