from typing import Optional, Tuple
from dotenv import load_dotenv
from lib.LibVoice import LibVoice
from Manager.ChatManager import ChatManager
import asyncio

class Jarvis:
    """
    Jarvis AI Assistant class that provides both voice and text-based interaction modes.
    """
    MODES = {0: "Voice", 1: "Text"}
    EXIT_COMMANDS = ["exit", "bye"]

    def __init__(self):
        """Initialize the Jarvis AI assistant."""
        load_dotenv()
        self.chat_manager = ChatManager()

    def _display_welcome_message(self) -> None:
        """Display the welcome message and available modes."""
        print("Welcome to Jarvis AI!")
        print("Select your preferred mode:")
        for key, value in self.MODES.items():
            print(f"[{key}] {value}")

    def _get_mode_selection(self) -> Optional[int]:
        """
        Get and validate the user's mode selection.
        
        Returns:
            Optional[int]: Selected mode number or None if invalid
        """
        try:
            mode = int(input(": "))
            if mode not in self.MODES:
                print("Invalid mode. Please enter 0 for Voice or 1 for Text.")
                return None
            return mode
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None

    async def _process_voice_input(self) -> Tuple[str, bool]:
        """
        Process voice input from the user.
        
        Returns:
            Tuple[str, bool]: (response/error message, should_continue flag)
        """
        print("\nListening...")
        question = await LibVoice.listen()
        
        if not question:
            return "Couldn't understand your voice input. Please try again.", True
            
        print(f"\nYou: {question}")
        if question.lower() in self.EXIT_COMMANDS:
            return "", False
            
        response = await self.chat_manager.ask_gemini_ai(question)
        print(f"\nJarvis: {response}\n")
        await LibVoice.say(response)
        return response, True

    async def _process_text_input(self) -> Tuple[str, bool]:
        """
        Process text input from the user.
        
        Returns:
            Tuple[str, bool]: (response/error message, should_continue flag)
        """
        question = input("You: ").strip()
        
        if not question:
            return "Please enter a valid query.", True
            
        if question.lower() in self.EXIT_COMMANDS:
            return "", False
            
        response = await self.chat_manager.ask_gemini_ai(question)
        print(f"\nJarvis: {response}\n")
        return response, True

    async def _run_interaction_loop(self, mode: int) -> None:
        """
        Run the main interaction loop for the selected mode.
        
        Args:
            mode: The selected interaction mode (0 for Voice, 1 for Text)
        """
        print(f"You have selected {self.MODES[mode]} mode. Say 'exit' or 'bye' to quit.")

        while True:
            try:
                if mode == 0:  # Voice Mode
                    response, should_continue = await self._process_voice_input()
                else:  # Text Mode
                    response, should_continue = await self._process_text_input()
                
                if not should_continue:
                    break
                    
            except Exception as e:
                print(f"An error occurred: {e}")
                break

    async def run_jarvis(self) -> None:
        """Main execution method for running the Jarvis AI system."""
        self._display_welcome_message()
        
        mode = self._get_mode_selection()
        if mode is None:
            return
            
        await self._run_interaction_loop(mode)
        print("Goodbye! Thank you for using Jarvis AI.")


if __name__ == "__main__":
    jarvis = Jarvis()
    asyncio.run(jarvis.run_jarvis())