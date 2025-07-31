import abc

from cass_clients.abstract_client import AbstractClient


class AbstractAgent(abc.ABC):
    def __init__(self, name: str, client: AbstractClient):
        self.name = name
        self.client = client


    @abc.abstractmethod
    def act(self, prompt: str) -> str:
        """
        Perform an action based on the given prompt.
        
        :param prompt: The input text to generate an action for.
        :return: The result of the action performed by the agent.
        """
        pass

    
    @abc.abstractmethod
    def get_name(self) -> str:
        """
        Get the name of the agent.
        
        :return: The name of the agent.
        """
        pass