import os
import logging

from openai import OpenAI
from openai.types.chat import ChatCompletion

from .abstract_client import AbstractClient

logger = logging.getLogger(__name__)

class OpenRouterClient(AbstractClient):
    def __init__(self, model: str, secondary_models: list[str] = []):
        """
        Initialize the OpenRouterClient with the specified model and optional secondary models.
        """
        self.api_key = os.getenv('OPEN_ROUTER_KEY')
        if not self.api_key:
            raise ValueError("API key for OpenRouter is not set. Please set the OPEN_ROUTER_KEY environment variable.")

        self.base_url = "https://openrouter.ai/api/v1"
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
        self.model = model
        self.secondary_models = secondary_models


    def completion(self, prompt: str) -> ChatCompletion:
        try:
            logger.info(f"Generating completion for prompt: {prompt} with model: {self.model}")

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response
        except Exception as e:
            logger.error(f"Error generating completion: {e}")
            raise e
    
