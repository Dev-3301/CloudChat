from fastapi import APIRouter,Depends,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models import UserFriend, UserConversation
from schemas import ConversationCreate,User


router = APIRouter()


@router.post("/conversations/", response_model=ConversationCreate)
def create_conversation(user_id: int, friend_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    friend = db.query(User).filter(User.id == friend_id).first()
    if not friend:
        raise HTTPException(status_code=404, detail="Friend not found")

    # Create the conversation
    conversation = ConversationCreate(user_id=user_id)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    db.add(UserConversation(user_id=user_id, conversation_id=conversation.id))
    db.add(UserConversation(user_id=friend_id, conversation_id=conversation.id))
    db.commit()

    # Store the user-friend relationship
    user_friend_entry = UserFriend(user_id=user_id, friend_id=friend_id)
    db.add(user_friend_entry)
    db.commit()

    return conversation
