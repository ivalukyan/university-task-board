from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    password: str
    staff_status: bool
    subscription_status: bool
