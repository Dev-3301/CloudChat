from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema for user sign-up
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str  # Plain text for input; will be hashed before storage

# Schema for user login
class UserLogin(BaseModel):
    username: str
    password: str

# Schema for returning user information (exclude sensitive data like hashed passwords)
class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    email_verified: bool
    created_at: Optional[str]

    class Config:
        orm_mode = True

# Schema for JWT token response
class Token(BaseModel):
    access_token: str
    token_type: str
