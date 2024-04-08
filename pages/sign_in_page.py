from pages.base_page import BasePage
from utils.locators import SignInPageLocators


class SignInPage(BasePage):
    def __init__(self, driver):
        self.locator = SignInPageLocators()
        super().__init__(driver)
