from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database_logic.database import get_db
from friend_logic.crud import create_friendship, delete_friendship
from friend_logic.add_friend import Friend
from database_logic.model import User

router = APIRouter()

@router.post('/create_friendship')
def create_friendship_route(user_id: int, friend_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    friend = db.query(User).filter(User.id == friend_id).first()
    if not friend:
        raise HTTPException(status_code=404, detail="Friend not found")
    
    return create_friendship(db, user_id, friend_id)

@router.delete("/delete_friendship")
def delete_friendship_route(user_id: int, friend_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    friend = db.query(User).filter(User.id == friend_id).first()
    if not friend:
        raise HTTPException(status_code=404, detail="Friend not found")

    return delete_friendship(db, user_id, friend_id)
