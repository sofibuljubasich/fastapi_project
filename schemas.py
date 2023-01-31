from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class UserLogin(BaseModel):
    email: EmailStr
    password = str

class UserCreate(BaseModel):
    email: EmailStr
    password : str
    name: str
class ExpenseBase(BaseModel):
    name:str
    amount:int
    category:str

class UserOut(BaseModel):
    email:EmailStr

    class Config:
        orm_mode = True

class Expense(ExpenseBase):
    owner_id = int
    owner = UserOut
   

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type:str

class TokenData(BaseModel):
    id: Optional[str] 