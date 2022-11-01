import  datetime

import pydantic as _pydantic
from pydantic import EmailStr

class UserModel(_pydantic.BaseModel):
    email: EmailStr

class UserCreate(_pydantic.BaseModel):
    hashed_password: str

    class Config:
        orm_mode = True