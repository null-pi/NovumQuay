import logging

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from cass_manager.service import CASSManagerService

from .manager import ConnectionManager


logger = logging.getLogger(__name__)
router = APIRouter()

connection_manager = ConnectionManager()
agent_manager = CASSManagerService()


@router.websocket("/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    try:
        connection_id = await connection_manager.connect(websocket)

        while True:
            logger.info(f"Client {client_id} connected with ID: {connection_id}")
            # Wait for a message from the client
            unstructured_data = await websocket.receive_text()

            logger.info(f"Received message from client {client_id}: {unstructured_data}")

            data = agent_manager.parse_conversations(unstructured_data)

            agent = agent_manager.create_agent(model="openrouter/horizon-alpha")

            response = agent.act(data)

            # Process the message or send a response
            await connection_manager.send_message(connection_id, response)
    except WebSocketDisconnect:
        await connection_manager.disconnect(connection_id)
    except Exception as e:
        logger.error(f"WebSocket error for client {client_id}: {e}")
        raise e
