import os
import yaml
from typing import Union, Optional, Dict, Any

class ConfigManager:
    """
    Manages configuration settings, including loading from YAML files.
    """

    CONFIG_FILE_PATH = "config.yml"
    DEFAULT_GEMINI_MODEL_ID = "gemini-1.5-flash-latest"

    @staticmethod
    def load_config() -> Optional[Dict[str, Any]]:
        """
        Load configuration settings from a YAML config file.
        """
        config_file_path = os.path.abspath(ConfigManager.CONFIG_FILE_PATH)
        try:
            with open(config_file_path, "r") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Config file not found at {config_file_path}")
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return None

    @staticmethod
    def get_config_value(key: str) -> Optional[Union[str, int, Dict[str, Any]]]:
        """
        Retrieve a specific value from the configuration settings.
        """
        config = ConfigManager.load_config()
        return config.get(key) if config else None

    @staticmethod
    def get_gemini_settings() -> Dict[str, Any]:
        """
        Retrieve Gemini AI generation and safety settings.
        """
        return {
            "generation_config": ConfigManager.get_config_value("generation_config") or {},
            "safety_settings": ConfigManager.get_config_value("safety_settings") or {},
        }

    @staticmethod
    def get_finetune_prompt() -> list[str]:
        """
        Retrieve fine-tuning prompts from the configuration.
        """
        fine_tune = ConfigManager.get_config_value("fine_tune")
        return fine_tune.get('prompt', []) if fine_tune else []

    @staticmethod
    def get_geminiAi_key() -> Optional[str]:
        """
        Retrieve Gemini AI API access key from environment variables.
        """
        return os.getenv("GEMINIAI_KEY")

    @staticmethod
    def get_gemini_model_id() -> str:
        """
        Retrieve Gemini AI model ID from configuration or return default.
        """
        return ConfigManager.get_config_value("gemini_model_id") or ConfigManager.DEFAULT_GEMINI_MODEL_ID
