import uvicorn
from fastapi import  FastAPI
from conversation import router as conversation_router
from messages import router as messages_router
from users import router as users_router

app = FastAPI()

app.include_router(users_router)
app.include_router(conversation_router)
app.include_router(messages_router)

"""
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000, reload=True)"""
