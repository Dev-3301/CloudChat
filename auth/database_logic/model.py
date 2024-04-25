from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database_logic.database import Base
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

    def set_password(self, password: str):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verify_password(self, password: str):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
