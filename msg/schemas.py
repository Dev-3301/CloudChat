from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):

    username: str

class MessageCreate(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    content: str
    created_at: datetime

    class Config:
        orm_mode = True


class ConversationCreate(BaseModel):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

