from playwright.sync_api import APIRequestContext, Page, expect

from helpers.db import get_user_data
from pages.demo_qa_page import DemoQaHomepage


def test_db_user_data(mongodb_client):
    result = get_user_data(mongodb_client)
    assert result == ('admin', 'password123')


def test_api_call_with_valid_data(api_request_context: APIRequestContext, auth_token: str):
    """
        Test creating and updating a booking with valid data.
        """
    # Step 1: Create a new booking
    create_booking_endpoint = "/booking"
    new_booking_payload = {
        "firstname": "Initial",
        "lastname": "User",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-10-01",
            "checkout": "2023-10-10"
        },
        "additionalneeds": "Breakfast"
    }

    create_response = api_request_context.post(create_booking_endpoint, data=new_booking_payload)
    assert create_response.status == 200, f"Failed to create booking. Status code: {create_response.status}"

    create_response_data = create_response.json()
    booking_id = create_response_data.get("bookingid")
    assert booking_id is not None, "Booking ID not returned in create booking response."

    # Step 2: Prepare to update the booking
    endpoint = f"/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
    update_payload = {
        "firstname": "James",
        "lastname": "Brown"
    }

    # Step 3: Make the PATCH request
    response = api_request_context.patch(endpoint, data=update_payload, headers=headers)
    assert response.status == 200, f"Expected status code 200, got {response.status}"

    # Step 4: Validate the response
    response_data = response.json()
    assert response_data.get("firstname") == "James", "Firstname was not updated correctly."
    assert response_data.get("lastname") == "Brown", "Lastname was not updated correctly."

    print("Booking updated successfully:", response_data)


def test_demo_qa_homepage(env_data, page: Page):
    """
    Test that navigates to the demoqa homepage and verifies the page title.

    Args:
        env_data: Fixture that provides environment data, including client_url.
        page: Playwright Page object provided by pytest-playwright.
    """
    # Instantiate the DemoQaHomepage with the page and client URL from env_data
    homepage = DemoQaHomepage(page)
    homepage.navigate(env_data.client)

    # Step 2: Verify the page title
    expected_title = "DEMOQA"
    assert page.title() == expected_title, f"Expected title '{expected_title}', got '{page.title()}'"

    # Step 3: Optionally, interact with the page
    # Example: Click on the "Elements" card
    homepage.click_elements_card()

    # Verify navigation to the Elements page
    expect(page).to_have_url(f"{env_data.client}/elements")
    print("Navigated to the Elements page successfully.")


def test_demo_qa_homepage_failure(env_data, page: Page):
    """
    Test that navigates to the demoqa homepage and verifies the page title.

    Args:
        env_data: Fixture that provides environment data, including client_url.
        page: Playwright Page object provided by pytest-playwright.
    """
    # Instantiate the DemoQaHomepage with the page and client URL from env_data
    homepage = DemoQaHomepage(page)
    homepage.navigate(env_data.client)

    # Step 2: Verify the page title
    expected_title = "DEMOQA1"
    assert page.title() == expected_title, f"Expected title '{expected_title}', got '{page.title()}'"

    # Step 3: Optionally, interact with the page
    # Example: Click on the "Elements" card
    homepage.click_elements_card()

    # Verify navigation to the Elements page
    expect(page).to_have_url(f"{env_data.client}/elements")
    print("Navigated to the Elements page successfully.")


def test_demo_qa_homepage_failure_two(env_data, page: Page):
    """
    Test that navigates to the demoqa homepage and verifies the page title.

    Args:
        env_data: Fixture that provides environment data, including client_url.
        page: Playwright Page object provided by pytest-playwright.
    """
    # Instantiate the DemoQaHomepage with the page and client URL from env_data
    homepage = DemoQaHomepage(page)
    homepage.navigate(env_data.client)

    # Step 2: Verify the page title
    expected_title = "DEMOQA1"
    assert page.title() == expected_title, f"Expected title '{expected_title}', got '{page.title()}'"

    # Step 3: Optionally, interact with the page
    # Example: Click on the "Elements" card
    homepage.click_elements_card()

    # Verify navigation to the Elements page
    expect(page).to_have_url(f"{env_data.client}/elements")
    print("Navigated to the Elements page successfully.")