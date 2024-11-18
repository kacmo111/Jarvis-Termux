from .ConfigManager import ConfigManager
from lib.GeminiAI import GeminiAI
from typing import Optional, Any
import asyncio

class ChatManager:
    """
    Manages chat sessions with Gemini AI.
    Handles fine-tuning prompts, sending messages, and managing session state.
    """

    _instance = None
    fine_tuned = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        """
        Initialize the ChatManager instance with API keys and settings.
        """
        self.api_key = ConfigManager.get_geminiAi_key()
        # print(f"Using API Key: {self.api_key}")
        self.model_id = ConfigManager.get_gemini_model_id()
        if not self.api_key:
            raise ValueError("Gemini AI API key not found in configuration.")

        self.genai = GeminiAI(api_key=self.api_key, model_id=self.model_id)

        self.settings = ConfigManager.get_gemini_settings()
        self.chat_session = None

    async def ask_gemini_ai(self, prompt: str) -> str:
        """
        Sends a prompt to Gemini AI and retrieves the response asynchronously.

        Args:
            prompt (str): The prompt text to send to the model.

        Returns:
            str: The response text from the model.
        """
        try:
            await self._apply_finetuning()

            response = await self.genai.generate_content(prompt)
            return response
        except Exception as e:
            return f"Error while communicating with Gemini AI: {e}"

    async def _apply_finetuning(self):
        """
        Applies fine-tuning by sending pre-configured prompts asynchronously.
        Runs multiple fine-tuning prompts in parallel to speed up the process.
        """
        if not self.fine_tuned:
            fine_tune_prompts = ConfigManager.get_finetune_prompt()
            if fine_tune_prompts:
                tasks = [self.genai.generate_content(prompt) for prompt in fine_tune_prompts]
                await asyncio.gather(*tasks)
                self.fine_tuned = True