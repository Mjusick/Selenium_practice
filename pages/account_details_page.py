from pages.base_page import BasePage
from utils.locators import AccountDetailsPageLocators


class AccountDetailsPage(BasePage):
    def __init__(self, driver):
        self.locators = AccountDetailsPageLocators()
        super().__init__(driver)

    def get_account_creation_confirmation_message(self):
        banner = self.find_element_with_wait(self.locators.ACCOUNT_CREATED_BANNER)
        return banner.text
