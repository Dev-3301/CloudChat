from fastapi import APIRouter, WebSocket, Depends, WebSocketDisconnect
from sqlalchemy.orm import Session
from database import get_db
from crud import create_message
from services import ConnectionManager

router = APIRouter()

manager = ConnectionManager()

@router.websocket("/ws/{sender_id}/{receiver_id}")
async def websocket_endpoint(websocket: WebSocket, sender_id: int, receiver_id: int, db: Session = Depends(get_db)):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

            await create_message(db, sender_id, receiver_id, data)
            await manager.broadcast_to_user(receiver_id, data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)


    return {"message": "WebSocket connection closed"}


async def broadcast_to_user(self, user_id: int, message: str):
    connections = self.get_connections_by_user_id(user_id)
    if connections:
        for connection in connections:
            await connection.send_text(message)

ConnectionManager.broadcast_to_user = broadcast_to_user
