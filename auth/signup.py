from fastapi import FastAPI, HTTPException, Depends, status, APIRouter
from sqlalchemy.orm import Session
from database_logic.database import get_db
from database_logic import crud
from database_logic import schema

router = APIRouter()

@router.post("/signup/", response_model=schema.UserOut)
def signup(user_create: schema.UserCreate, db: Session = Depends(get_db)):
    # Check if the email or username already exists
    if crud.get_user_by_email(db, user_create.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # Create a new user
    new_user = crud.create_user(db, user_create)
    return new_user