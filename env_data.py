import os

from dotenv import load_dotenv

load_dotenv()


class EnvData:
    def __init__(self):
        self.api_url: str = os.getenv("API_URL")
        self.db: str = os.getenv("DB")
        self.client: str = os.getenv("CLIENT")
