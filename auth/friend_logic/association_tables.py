from sqlalchemy import Table, Column, Integer, ForeignKey
from database_logic.database import Base

friend_association_table = Table(
    'user_friend', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('friend_id', Integer, ForeignKey('users.id'), primary_key=True)
)