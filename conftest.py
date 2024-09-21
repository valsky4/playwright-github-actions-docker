import os
import subprocess
import time

import pytest
from playwright.sync_api import APIRequestContext, Playwright
from pymongo import MongoClient

# from helpers.db import get_user_data
from helpers.vpn import is_vpn_connected
from env_data import EnvData


def pytest_addoption(parser):
    """
    Adds a custom command-line option to specify the environment.
    """
    parser.addoption(
        "--environment",
        action="store",
        default="DEV",
        help="Environment to run tests against (e.g., DEV, STAGE, PROD). Defaults to DEV.",
    )


@pytest.fixture(scope='session')
def env_data(pytestconfig) -> EnvData:
    """
    Provides an instance of TestData loaded with environment variables
    based on the specified environment.
    """
    environment = pytestconfig.getoption("environment").upper()

    if environment not in ["DEV", "STAGE"]:
        raise ValueError(f"The environment variable {environment} is not valid.")
    else:
        print("\nStarting the tests on", environment)
    try:
        return EnvData(desired_env=environment)
    except ValueError as e:
        pytest.exit(str(e))


# commented for the sake of the githubactions
@pytest.fixture(scope='session')
def mongodb_client(env_data) -> MongoClient:
    """
    Provides a MongoClient instance that persists across all tests.
    """
    pass
    # print("\n[Setup] Connecting to MongoDB")
    # connection_string = env_data.db
    # client = MongoClient(connection_string)
    # yield client
    # print("\n[Teardown] Closing MongoDB connection")
    # client.close()


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright, env_data) -> APIRequestContext:
    """
    Creates an APIRequestContext for making HTTP requests using Playwright.
    """
    api_context = playwright.request.new_context(base_url=env_data.api_url)
    yield api_context
    api_context.dispose()


@pytest.fixture(scope='session')
def auth_token(api_request_context: APIRequestContext, mongodb_client: MongoClient) -> str:
    """
    Retrieves an authentication token and provides it to tests.
    """
    # commented due to githubactions test and not to build containers
    # credentials = get_user_data(mongodb_client)
    credentials = ('admin', 'password123')
    if credentials is None:
        pytest.exit("Failed to retrieve credentials from the database.")

    username, password = credentials

    endpoint = "/auth"
    payload = {
        "username": username,
        "password": password
    }

    response = api_request_context.post(endpoint, data=payload)
    if response.status != 200:
        pytest.exit(f"Failed to retrieve token. Status code: {response.status}")

    response_data = response.json()
    token = response_data.get("token")
    if not token:
        pytest.exit("Token not found in the response.")

    return token


# @pytest.fixture(scope='session', autouse=True)
@pytest.fixture(scope='session')
def vpn_connection(env_data):
    """
    Pytest fixture to manage VPN connection using OpenVPN.
    """
    # Path to your OpenVPN configuration file
    vpn_config_path = os.getenv("VPN_CONFIG_PATH")
    if not vpn_config_path:
        pytest.exit("VPN configuration path not set. Set the 'VPN_CONFIG_PATH' environment variable.")

    # Command to start the VPN connection
    vpn_command = [
        "sudo", "openvpn",
        "--config", vpn_config_path,
        "--daemon",
        "--log", "openvpn.log"
    ]

    print("\n[Setup] Starting VPN connection...")
    try:
        # Start the VPN connection
        subprocess.check_call(vpn_command)
    except subprocess.CalledProcessError as e:
        pytest.exit(f"Failed to start VPN connection: {e}")

    # Wait until VPN is connected
    max_attempts = 10
    for attempt in range(max_attempts):
        print(f"Checking VPN connection (Attempt {attempt + 1}/{max_attempts})...")
        if is_vpn_connected(env_data.api_url):
            print("VPN connected successfully.")
            break
        time.sleep(2)
    else:
        pytest.exit("Failed to establish VPN connection after multiple attempts.")

    # Yield control to the tests
    yield

    print("\n[Teardown] Closing VPN connection...")
    try:
        # Command to stop the VPN connection
        subprocess.check_call(["sudo", "killall", "openvpn"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop VPN connection: {e}")
