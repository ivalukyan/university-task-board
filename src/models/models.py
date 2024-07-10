from pydantic import BaseModel
from fastapi import Form


class User(BaseModel):
    id: int
    username: str
    password: str
    staff_status: bool
<<<<<<< HEAD
=======
    subscription_status: bool


class Mailing(BaseModel):
    user_id: int
    message: str
>>>>>>> origin/main

