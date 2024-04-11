from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base 


# Association table for the many-to-many relationship between users and conversations
user_conversation_table = Table('user_conversation', Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('conversation_id', ForeignKey('conversations.id'), primary_key=True)
)

class Conversation(Base):
    __tablename__ = 'conversations'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    users = relationship("User", secondary=user_conversation_table, back_populates="conversations")
    messages = relationship("Message", back_populates="conversation") 

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False) 
    content = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    conversation = relationship("Conversation", back_populates="messages")
    sender = relationship("User", back_populates="messages")