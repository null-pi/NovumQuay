import logging
import uuid

from fastapi import WebSocket

logger = logging.getLogger(__name__)

class ConnectionManager:
    def __init__(self):
        self.connections: dict[str, WebSocket] = {}

    async def connect(self, connection: WebSocket):
        try:
            connection_id = str(uuid.uuid4())
            await connection.accept()
            self.connections[connection_id] = connection
            logger.info(f"New connection established: {connection_id}")
            return connection_id
        except Exception as e:
            logger.error(f"Error during connection: {e}")
            raise e

    async def disconnect(self, connection_id: str):
        try:
            connection = self.get_connection(connection_id)

            if connection.client_state == 1:  # CONNECTED
                logger.info(f"Disconnecting connection: {connection_id}")
                await connection.close(code=1000, reason="Normal Closure")
                del self.connections[connection_id]
                logger.info(f"Connection {connection_id} disconnected successfully.")
        except Exception as e:
            logger.error(f"Error during disconnection: {e}")
            raise e

    def get_connection(self, connection_id: str) -> WebSocket | None:
        try:
            connection = self.connections.get(connection_id)

            if not connection:
                logger.error(f"Connection {connection_id} not found for disconnection.")
                raise KeyError(f"Connection {connection_id} not found.")

            return connection
        except Exception as e:
            logger.error(f"Error retrieving connection {connection_id}: {e}")
            raise e
        

    async def send_message(self, connection_id: str, message: str):
        try:
            connection = self.get_connection(connection_id)

            if connection.client_state == 1:  # CONNECTED
                await connection.send_text(message)
                logger.info(f"Message sent to {connection_id}: {message}")
            else:
                logger.warning(f"Connection {connection_id} is not connected.")
        except Exception as e:
            logger.error(f"Error sending message to {connection_id}: {e}")
            raise e