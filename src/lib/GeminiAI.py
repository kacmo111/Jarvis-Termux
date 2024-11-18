import aiohttp
import json
import asyncio

class GeminiAI:
    """
    A class to interact with Gemini AI API using direct asynchronous HTTP requests (using aiohttp).
    """

    def __init__(self, api_key: str, model_id: str):
        """
        Initializes the GeminiAI instance with an API key and model ID.

        Args:
            api_key (str): The API key for Gemini AI.
            model_id (str): The model ID (e.g., gemini-1.5-flash).
        """
        self.api_key = api_key
        self.model_id = model_id
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"

    async def generate_content(self, prompt: str) -> str:
        """
        Sends a request to the Gemini AI API to generate content based on the given prompt.

        Args:
            prompt (str): The input text to send to the model.

        Returns:
            str: The AI-generated response (just the text).
        """
        url = f"{self.base_url}/{self.model_id}:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        data = {"contents": [{"parts": [{"text": prompt}]}]}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status != 200:
                    raise Exception(
                        f"Error: {response.status}, {await response.text()}"
                    )

                response_json = await response.json()
                return self._parse_response(response_json)

    def _parse_response(self, response_json: dict) -> str:
        """
        Parses the response from Gemini AI to extract just the text.

        Args:
            response_json (dict): The JSON response from Gemini AI.

        Returns:
            str: The text from the AI response.
        """
        try:
            text = response_json["candidates"][0]["content"]["parts"][0]["text"]
            return text.strip()
        except (KeyError, IndexError) as e:
            raise ValueError(f"Error parsing the response: {e}")
