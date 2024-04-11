from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

friend_association_table = Table(
    'user_friend', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('friend_id', Integer, ForeignKey('users.id'), primary_key=True)
)