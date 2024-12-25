from dotenv import load_dotenv
import os

class ConfigManager:
    @staticmethod
    def load_config():
        """
        Load configuration from .env file.
        """
        load_dotenv()
        config = {
            "api_dev_key": os.getenv("API_DEV_KEY"),
            "api_user_name": os.getenv("API_USER_NAME"),
            "api_user_password": os.getenv("API_USER_PASSWORD"),
        }
        # Check for missing values
        for key, value in config.items():
            if not value:
                raise ValueError(f"Missing environment variable: {key}")
        return config
