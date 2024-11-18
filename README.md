---

# Jarvis-Termux (Python)

Jarvis-Termux is a Python-based AI chat and voice assistant, now powered by Google's Gemini AI model. It provides a convenient way to interact with an AI assistant using both voice and text commands directly from your Termux terminal. The assistant can answer questions, provide responses, and engage in natural conversations.

## Features

- **Voice-based AI assistant**: Interact with Jarvis using voice commands and receive spoken responses via Termux TTS.
- **Text-based AI assistant**: Interact with Jarvis using text-based queries.
- **Natural language conversation**: Engage in free-flowing conversations with the AI assistant.
- **Google Gemini AI-powered**: Jarvis now uses the Google Gemini API for generating intelligent responses instead of OpenAI's GPT.
- **Improved performance and reliability**: The Python version enhances readability, performance, and fixes previous bugs.

## Libraries Used

- **Google Gemini API**: Used for AI-powered responses.
- **LibVoice (Termux)**: A library for handling voice input and output using Termux.
- **dotenv**: For loading secret keys from `.env` files.
- **Asyncio**: Ensures asynchronous execution for voice commands and AI responses.

## Configuration

### Configuration File (`config.yml`)

```yaml
gemini_model_id: "gemini-1.5-flash-002"
generation_config:
  temperature: 1                    # Temperature parameter for text generation
  top_p: 0.95                        # Top p parameter for text generation
  top_k: 40                          # Top k parameter for text generation
  max_output_tokens: 2048            # Maximum number of output tokens
  response_mime_type: "text/plain"   # Mime type of the response

safety_settings:
  - category: "HARM_CATEGORY_HARASSMENT"
    threshold: "BLOCK_NONE"
  - category: "HARM_CATEGORY_HATE_SPEECH"
    threshold: "BLOCK_NONE"
  - category: "HARM_CATEGORY_SEXUALLY_EXPLICIT"
    threshold: "BLOCK_NONE"
  - category: "HARM_CATEGORY_DANGEROUS_CONTENT"
    threshold: "BLOCK_NONE"

fine_tune:
  prompt:
    - "my name is amitxd"
```

### Secrets File (`.env`)

```env
GEMINIAI_KEY=your.api.key
```

## Getting Started

### Prerequisites

- **Python**: Ensure Python 3.7+ is installed on your system. You can check by running:
  ```bash
  python --version
  ```
- **pip**: Python's package installer (comes with Python).
- **Termux**: This project is designed to work in Termux, a terminal emulator for Android.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Amitminer/Jarvis-Termux.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Jarvis-Termux
   ```

3. **Install Required Python Libraries**:
   Create a virtual environment (optional but recommended) and install the dependencies using `pip`:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   pip install -r requirements.txt
   ```

4. **Set Up Configuration**:
   - Copy `config.yml.example` to `config.yml`.
   - Update the `gemini_model_id`, `generation_config`, and `safety_settings` as needed.
   - Ensure the `GEMINIAI_KEY` is set in the `.env` file for API authentication.

5. **Run the Application**:
   You can start the application in two ways:
   - Run the script directly:
     ```bash
     python ./src/Jarvis.py
     ```
   - Or execute the shell script (`start.sh`), which automatically sets up and runs the app:
     ```bash
     ./start.sh
     ```

### Usage

1. **Start Jarvis**:
   - After running the script, you will be prompted to choose a mode (Voice or Text).
   - If you select Voice Mode, Jarvis will listen to your voice input and respond both verbally and in text.
   - If you select Text Mode, you can type your queries, and Jarvis will respond accordingly.

2. **Voice Interaction**:
   - Jarvis will listen for commands, and if recognized, will respond with speech and text.
   - Say 'exit' or 'bye' to quit the session.

3. **Text Interaction**:
   - Type your queries and interact with Jarvis via text.
   - Jarvis will process the request and respond in text.

### Example:

```bash
Welcome to Jarvis AI!
Select your preferred mode:
[0] Voice
[1] Text
: 0

You have selected Voice mode. Say 'exit' or 'bye' to quit.
Listening...
You: What is the weather today?
Jarvis: The weather is sunny with a chance of clouds. Enjoy your day!
```

### To Do

- Add functionality to open apps using voice commands.
- Improve response personalization and context management.

## Contributions

Contributions to Jarvis-Termux are welcome! If you have any ideas, suggestions, or bug reports, feel free to create an issue or submit a pull request on the [Jarvis-Termux GitHub repository](https://github.com/Amitminer/Jarvis-Termux). Let's improve Jarvis-Termux together!

## License

Jarvis-Termux is released under the [MIT License](https://github.com/Amitminer/Jarvis-Termux/blob/main/LICENSE).

---
