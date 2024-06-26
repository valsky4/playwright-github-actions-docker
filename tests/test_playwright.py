from playwright.sync_api import Page

from pages.test_playwright import PlaywrightPage


def test_has_title(page: Page):
    playwright_page = PlaywrightPage(page)
    playwright_page.navigate()
    playwright_page.assert_title_contains("Playwright")


def test_get_started_link(page: Page):
    playwright_page = PlaywrightPage(page)
    playwright_page.navigate()
    playwright_page.click_button(role='link', name='Get started')
    playwright_page.assert_page_role_to_be_visible(role='heading', name='Installation')
