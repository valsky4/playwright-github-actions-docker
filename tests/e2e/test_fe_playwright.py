import pytest
from playwright.sync_api import Page

from pages.playwright_page import PlaywrightPage


@pytest.mark.web
def test_has_title(page: Page):
    playwright_page = PlaywrightPage(page)
    playwright_page.navigate()
    playwright_page.assert_title_contains("Playwright")


@pytest.mark.web
def test_get_started_link(page: Page):
    playwright_page = PlaywrightPage(page)
    playwright_page.navigate()
    playwright_page.click_button(role='link', name='Get started')
    playwright_page.assert_page_role_to_be_visible(role='heading', name='Installatio32n')


@pytest.mark.web
def test_abra_cadabra(page: Page):
    playwright_page = PlaywrightPage(page)
    playwright_page.navigate()
    playwright_page.click_button(role='link', name='Get started')
    playwright_page.assert_page_role_to_be_visible(role='heading', name='Installatio32n')
