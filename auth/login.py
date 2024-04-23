from fastapi import FastAPI, HTTPException, Depends, status, APIRouter
from sqlalchemy.orm import Session
from database_logic import schema
from database_logic import crud
from database_logic import database

router = APIRouter()


@router.post("/login/", response_model=schema.Token)
def login(user_login: schema.UserLogin, db: Session = Depends(database.get_db)):
    user = crud.authenticate_user(db, user_login.username, user_login.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    # Generate a JWT token
    access_token = crud.create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}