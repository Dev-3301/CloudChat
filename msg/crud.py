from sqlalchemy.orm import Session
from models import Message
from datetime import datetime

def create_message(db: Session,sender_id: int, recipient_id: int, content:str):
    db_message = Message(sender_id=sender_id, receiver_id=recipient_id, content=content, created_at=datetime.now())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
