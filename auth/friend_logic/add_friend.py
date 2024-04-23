from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from friend_logic.association_tables import friend_association_table
from database_logic.model import User
from database_logic.database import Base 

class Friend(Base):
    __tablename__ = 'friend'

    id = Column(Integer, primary_key=True)
    added_at = Column(DateTime(timezone=True), server_default=func.now())

User.friends = relationship(
    'User',
    secondary=friend_association_table,
    primaryjoin=User.id == friend_association_table.c.user_id,
    secondaryjoin=User.id == friend_association_table.c.friend_id,
    back_populates='friends'
)