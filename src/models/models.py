from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    staff_status: bool

