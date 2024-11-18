from .ConfigManager import ConfigManager
import google.generativeai as genai
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
        """
        Singleton pattern: Ensure only one instance of ChatManager exists.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        """
        Initialize the ChatManager instance with API keys and settings.
        """
        self.api_key = ConfigManager.get_geminiAi_key()
        print(f"Using API Key: {self.api_key}")
        self.model_id = ConfigManager.get_gemini_model_id()
        if not self.api_key:
            raise ValueError("Gemini AI API key not found in configuration.")
        genai.configure(api_key=self.api_key)

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
            await self._ensure_chat_session()
            await self._apply_finetuning()

            response = await self._send_message_async(prompt)
            return response.text
        except Exception as e:
            return f"Error while communicating with Gemini AI: {e}"

    async def _ensure_chat_session(self):
        """
        Ensures that a chat session is initialized.
        If not, creates a new session asynchronously.
        """
        if not self.chat_session:
            model = await self._create_model_async()
            self.chat_session = model.start_chat(history=[])

    async def _apply_finetuning(self):
        """
        Applies fine-tuning by sending pre-configured prompts asynchronously.
        """
        if not self.fine_tuned:
            fine_tune_prompts = ConfigManager.get_finetune_prompt()
            if fine_tune_prompts:
                for prompt in fine_tune_prompts:
                    await self._send_message_async(prompt)
                self.fine_tuned = True
                # print("Fine-tuning completed successfully.")

    async def _send_message_async(self, prompt: str) -> Any:
        """
        Simulates asynchronous behavior for sending messages.
        """
        return await asyncio.to_thread(self.chat_session.send_message, prompt)

    async def _create_model_async(self) -> Any:
        """
        Creates and returns a Generative AI model asynchronously.
        """
        try:
            return await asyncio.to_thread(
                genai.GenerativeModel,
                model_name=self.model_id,
                safety_settings=self.settings.get("safety_settings"),
                generation_config=self.settings.get("generation_config"),
            )
        except Exception as e:
            raise ValueError(f"Error initializing Generative AI model: {e}")