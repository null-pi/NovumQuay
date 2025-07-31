import json
import logging

from cass_agents.generic_agent import GenericAgent
from cass_clients.open_router_client import OpenRouterClient
from .dto import ChatMessage

logger = logging.getLogger(__name__)


class CASSManagerService:
    def create_agent(self, model: str, secondary_models: list[str] = []):
        try:
            return GenericAgent(
                name="GenericAgent",
                client=OpenRouterClient(model=model, secondary_models=secondary_models),
            )
        except Exception as e:
            logger.error(f"Error creating agent: {e}")
            raise e
        

    def parse_conversations(self, unstructured_convos: str) -> str:
        """
        Parse the response from the agent and return the content.
        
        :param response: The response object from the agent.
        :return: The content of the response.
        """
        try:
            json_convo = json.loads(unstructured_convos)
            conversations = [ChatMessage(**item) for item in json_convo]

            response = [str(message) for message in conversations]
            return "\n".join(response)
        except Exception as e:
            logger.error(f"Error parsing response: {e}")
            raise e
