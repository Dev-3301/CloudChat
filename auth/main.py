# main.py
from fastapi import FastAPI
from signup import router as signup_router
from login import router as login_router
from friend import router as friend_router


app = FastAPI()

# Include the signup router
app.include_router(signup_router)
app.include_router(login_router)
app.include_router(friend_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)