#import asyncio
import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient
from websockets import connect
from ..messages import router


@pytest.fixture(scope="module")
def app():
    app = FastAPI()
    app.include_router(router)
    return app


@pytest.fixture
def client(app):
    return TestClient(app)

# testing if there is a connection
@pytest.mark.asyncio
async def test_websocket_connection(client):
    async with connect("ws://localhost/ws/1/2") as websocket:
        assert await websocket.recv() == '{"message":"WebSocket connection closed"}'


