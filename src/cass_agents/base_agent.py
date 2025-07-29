from cass_clients.abstract_client import AbstractClient


class BaseAgent:
    def __init__(self, name: str, client: AbstractClient):
        self.name = name
        self.client = client

    
    def generate_completion(self, prompt: str):
        """
        Generate a completion for the given prompt using the client's completion method.
        
        :param prompt: The input text to generate a completion for.
        :return: The generated completion response.
        """
        completion_response = self.client.completion(prompt)

        return completion_response.choices[0].message.content