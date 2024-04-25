from fastapi import FastAPI
from fastapi.testclient import TestClient
from msg
app = FastAPI()
app.include_router(messages.router)
client = TestClient(app)
