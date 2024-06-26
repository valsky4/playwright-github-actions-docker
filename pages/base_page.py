import re

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def assert_title_contains(self, substring: str) -> None:
        expect(self.page).to_have_title(re.compile(substring))

    def click_button(self, role, name: str) -> None:
        self.page.get_by_role(role=role, name=name).click()

    def assert_page_role_to_be_visible(self, role, name: str) -> None:
        expect(self.page.get_by_role(role=role, name=name)).to_be_visible()

    def get_title(self) -> str:
        return self.page.title()
