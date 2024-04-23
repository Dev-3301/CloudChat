from sqlalchemy.orm import Session
from database_logic import model
from database_logic import schema
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "YourSecretKeyHere"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  
def create_user(db: Session, user_create: schema.UserCreate):
    new_user = model.User(
        first_name=user_create.first_name,
        last_name=user_create.last_name,
        username=user_create.username,
        email=user_create.email,
        created_at=datetime.utcnow() 
    )
    new_user.set_password(user_create.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    new_user_dict = new_user.__dict__
    new_user_dict['created_at'] = str(new_user_dict['created_at'])

    return new_user_dict

def get_user_by_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.email == email).first()

def authenticate_user(db: Session, username: str, password: str) -> bool:
    user = db.query(model.User).filter_by(username = username).first()
    print(user)
    if user and user.verify_password(password):
        print("EEEEEEEEEEEEEEEEEEEEEEEEEEE")
        return user
    return False

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
