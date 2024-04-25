import pytest
from fastapi import FastAPI, WebSocket
from fastapi.testclient import TestClient
from ..messages import router

@pytest.fixture(scope="messages")
def app():
    app = FastAPI()
    app.include_router(router)
    yield app

@pytest.fixture(scope="messages")
def test_messages(app):
    return TestClient(app)





def test_websocket_connection(test_client, mock_db, mock_connection_manager):
    with test_client.websocket_connect("/ws/1/2") as websocket:
        assert websocket.accept()  # Ensure connection is accepted

def test_message_sending(test_client, mock_db, mock_connection_manager):
    with test_client.websocket_connect("/ws/1/2") as websocket:
        websocket.send_text("Test message")
        assert websocket.receive_text() == "Test message"  # Ensure message is echoed back

def test_disconnection(test_client, mock_db, mock_connection_manager):
    with test_client.websocket_connect("/ws/1/2") as websocket:
        websocket.close()
        # Ensure WebSocketDisconnect is handled properly (no assertion, just making sure no errors occur)
