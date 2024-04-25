from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True, index=True)
    email = Column(String)
    password = Column(String)
    email_confirmed = Column(Boolean, default=True)
    created_at = Column(DateTime)

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String)
    created_at = Column(DateTime)

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)

class UserFriend(Base):
    __tablename__ = 'user_friend'
    user_id = Column(Integer, primary_key=True, index=True)
    friend_id = Column(String)

class UserConversation(Base):
    __tablename__ = 'user_conversation'
    user_id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id'))


