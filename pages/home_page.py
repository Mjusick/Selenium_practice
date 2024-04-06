from pages.base_page import BasePage
from pages.create_account_page import CreateAccountPage
from utils.locators import HomePageLocators
from utils.logger import get_logger

logger = get_logger(__name__)


class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver)

    def check_logo_appearance(self):
        logger.info("Checking if logo appeared on homepage.")
        return self.find_element_with_wait(*self.locator.LOGO)

    def go_to_create_account_page(self):
        logger.info("Going to sign in page")
        create_account_button = self.find_element_with_wait(*self.locator.CREATE_ACCOUNT_BUTTON)
        create_account_button.click()
        return CreateAccountPage(self.driver)