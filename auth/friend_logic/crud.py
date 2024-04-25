from sqlalchemy.orm import Session
from database_logic.model import User
from sqlalchemy.exc import SQLAlchemyError



def create_friendship(db: Session, user_id: int, friend_id: int) -> None:
    try:
        user = db.query(User).filter(User.id == user_id).first()
        friend = db.query(User).filter(User.id == friend_id).first()

        if user and friend:
            # Check if the friendship already exists in both directions
            if friend not in user.friends and user not in friend.friends:
                # Add the friend to the user's list of friends
                user.friends.append(friend)
                db.commit()
        else:
            raise ValueError("User or friend not found.")
    except Exception as e:
        db.rollback()
        raise e
    
def read_friends(db: Session, user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            return [friend.id for friend in user.friends]
        else:
            raise ValueError("User not found.")
    except Exception as e:
        raise e
    
def delete_friendship(db: Session, user_id: int, friend_id: int) -> None:
    try:
        user = db.query(User).filter(User.id == user_id).first()
        friend = db.query(User).filter(User.id == friend_id).first()

        if user and friend:
            # Remove the friend from the user's list of friends
            user.friends.remove(friend)
            db.commit()
        else:
            raise ValueError("User or friend not found.")
    except Exception as e:
        db.rollback()
        raise e
    