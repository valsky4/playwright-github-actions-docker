from pages.base_page import BasePage


class DemoQaHomepage(BasePage):
    ELEMENTS_CARD = "div.card-body h5:has-text('Elements')"

    def navigate(self, url: str = None):
        self.page.goto(url)

    def click_elements_card(self):
        self.page.click(self.ELEMENTS_CARD)
