from pydantic import BaseModel


class JobSchema(BaseModel):
    title: str
    company: str
    is_active: bool

    class Config:
        orm_mode = True
