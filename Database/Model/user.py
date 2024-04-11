from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from .association_tables import friend_association_table
from .messages import user_conversation_table
import bcrypt


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128))
    email_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False) 
    
    conversations = relationship("Conversation", secondary=user_conversation_table, back_populates="users")
    messages = relationship("Message", back_populates="sender")
    profile = relationship("Profile", back_populates="user", uselist=False)
    friends = relationship(
        "User",
        secondary=friend_association_table,
        primaryjoin=id == friend_association_table.c.user_id,
        secondaryjoin=id == friend_association_table.c.friend_id,
        back_populates="friends"
    )

    def set_password(self, password: str):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verify_password(self, password: str):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))