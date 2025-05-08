from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    email: str
    username: str

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
