from fastapi import Depends, HTTPException, APIRouter
from schemas import User
from database import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/users/{username}", response_model=User)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user