import os

from dotenv import load_dotenv

load_dotenv()


class EnvData:
    def __init__(self, desired_env: str = 'DEV'):
        self.api_url: str = os.getenv(f"{desired_env}_API_URL")
        self.db: str = os.getenv(f"{desired_env}_DB")
        self.client: str = os.getenv(f"{desired_env}_CLIENT")
