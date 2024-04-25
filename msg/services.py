from typing import List, Dict
from fastapi import WebSocket
from collections import defaultdict

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[int, List[WebSocket]] = defaultdict(list)

    async def connect(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id].append(websocket)

    def disconnect(self, user_id: int, websocket: WebSocket):
        self.active_connections[user_id].remove(websocket)

    async def broadcast(self, message: str):
        for connections in self.active_connections.values():
            for connection in connections:
                await connection.send_text(message)

    async def broadcast_to_user(self, user_id: int, message: str):
        connections = self.active_connections.get(user_id)
        if connections:
            for connection in connections:
                await connection.send_text(message)

    def get_connections_by_user_id(self, user_id: int) -> List[WebSocket]:
        return self.active_connections.get(user_id, [])

    def remove_user_connections(self, user_id: int):
        del self.active_connections[user_id]
