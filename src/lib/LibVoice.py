import os
import asyncio
from typing import Optional

class LibVoice:
    @staticmethod
    async def say(msg: str) -> None:
        """
        Uses Termux Text-to-Speech (TTS) asynchronously to speak the provided message.
        
        Args:
            msg (str): The message to be spoken by the TTS engine.
        
        This function checks if Termux's Text-to-Speech (TTS) utility is available, and if so, 
        it asynchronously executes the TTS command to speak the provided message. If TTS is 
        unavailable, an error message is printed.
        """
        try:
            # Check if termux-tts-speak is available
            tts_available = await asyncio.create_subprocess_shell(
                "command -v termux-tts-speak > /dev/null 2>&1"
            )
            await tts_available.wait()

            if tts_available.returncode == 0:
                # Run the TTS command asynchronously
                process = await asyncio.create_subprocess_shell(
                    f"termux-tts-speak {msg.lower()}",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                )
                await process.communicate()
            else:
                print("Error: Termux TTS is not available on this system.")
        except Exception as e:
            print(f"Error while using TTS: {e}")

    @staticmethod
    async def listen() -> Optional[str]:
        """
        Uses Termux speech-to-text asynchronously to capture voice input.
        
        Returns:
            Optional[str]: The transcribed text from speech input. Returns None if an error occurs
            or no speech is captured.
        
        This function checks if Termux's speech-to-text utility is available. If it is, it 
        asynchronously captures voice input and returns the transcribed text. If the utility 
        is unavailable or an error occurs, an appropriate error message is printed, and None is returned.
        """
        try:
            # Check if termux-speech-to-text is available
            stt_available = await asyncio.create_subprocess_shell(
                "command -v termux-speech-to-text > /dev/null 2>&1"
            )
            await stt_available.wait()

            if stt_available.returncode == 0:
                # Run the speech-to-text command asynchronously
                process = await asyncio.create_subprocess_shell(
                    "termux-speech-to-text",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                )
                stdout, stderr = await process.communicate()
                if process.returncode == 0 and stdout:
                    return stdout.decode().strip()
                elif stderr:
                    print(f"Error from Termux STT: {stderr.decode().strip()}")
            else:
                print("Error: Termux Speech-to-Text is not available.")
        except Exception as e:
            print(f"Error during voice input: {e}")
        return None
