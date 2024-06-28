import os

from dotenv import load_dotenv

load_dotenv()


class TestData:
    @staticmethod
    def return_example_api_url():
        return os.getenv("EXAMPLE_API_URL")

    @staticmethod
    def return_example_user_name():
        return os.getenv("EXAMPLE_USERNAME")

    @staticmethod
    def return_example_password():
        return os.getenv("EXAMPLE_PASSWORD")