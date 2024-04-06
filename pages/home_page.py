from pages.base_page import BasePage
from utils.locators import HomePageLocators
from utils.logger import get_logger

logger = get_logger(__name__)


class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver)

    def check_logo_appearance(self):
        logger.info("Checking if logo appeared on homepage.")
        return self.find_element(*self.locator.LOGO)

