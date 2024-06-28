from typing import Generator
import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

from test_data import TestData


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url=f"{TestData.return_example_api_url()}"
    )
    yield request_context
    request_context.dispose()


def login(api_request_context: APIRequestContext) -> str:
    data = {
        "email": f"{TestData.return_example_user_name()}",
        "credentials": {
            "password": f"{TestData.return_example_password()}"
        }
    }
    login_response = api_request_context.post("auth/login", data=data)
    assert login_response.ok
    login_to_json = login_response.json()
    assert 'accessToken' in login_to_json, "accessToken is not in the response"
    assert login_to_json['accessToken'] != 0, "accessToken should not be zero"
    return login_to_json['accessToken']


@pytest.mark.api
def test_get_count(api_request_context: APIRequestContext) -> None:
    get_count_response = api_request_context.get("storyfiles/count",
                                                 headers={"Authorization": f"Bearer {login(api_request_context)}"})
    assert get_count_response.ok


@pytest.mark.api
def test_get_template_count(api_request_context: APIRequestContext) -> None:
    get_count_response = api_request_context.get("templates/count",
                                                 headers={"Authorization": f"Bearer {login(api_request_context)}"})
    assert get_count_response.ok
