from pages.base_page import BasePage


class PlaywrightPage(BasePage):

    def navigate(self):
        self.page.goto("https://playwright.dev/")


