import json
import logging

from cass_manager.dto import ChatMessage, MessageType, ProvidedBy

from .abstract_agent import AbstractAgent

logger = logging.getLogger(__name__)


class GenericAgent(AbstractAgent):
    def act(self, prompt: str) -> str:
        """
        Generate a completion for the given prompt using the client's completion method.
        
        :param prompt: The input text to generate a completion for.
        :return: The generated completion response.
        """
        try:
            completion_response = self.client.completion(prompt)

            content = completion_response.choices[0].message.content

            response = ChatMessage(
                providedBy=ProvidedBy.SYSTEM,
                messageType=MessageType.TEXT,
                content=content
            )
            return json.dumps(response.model_dump())
        except Exception as e:
            # Handle exceptions that may occur during completion generation
            logger.error(f"Error generating completion for prompt '{prompt}': {e}")
            return "Error generating completion"
        

    def get_name(self) -> str:
        """
        Get the name of the agent.
        
        :return: The name of the agent.
        """
        return self.name