import abc

from openai.types.chat import ChatCompletion


class AbstractClient(abc.ABC):
    @abc.abstractmethod
    def completion(self, prompt: str) -> ChatCompletion:
        """
        Generate a completion for the given prompt using the specified model.
        
        :param prompt: The input text to generate a completion for.
        :param max_tokens: The maximum number of tokens to generate in the completion.
        :return: The generated completion response.
        """
        pass