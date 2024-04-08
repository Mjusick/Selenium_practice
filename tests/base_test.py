import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utils.logger import get_logger
from variables import BASE_PAGE_URL
from utils.locators import HomePageLocators

logger = get_logger(__name__)


class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(BASE_PAGE_URL)
        self.accept_consent_screen()

    def tearDown(self):
        self.driver.close()

    def accept_consent_screen(self):
        policy_locator = HomePageLocators.POLICY_CONSENT_CONFIRM_BUTTON
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(policy_locator))
            consent_button = self.driver.find_element(*policy_locator)
            consent_button.click()
        except TimeoutException:
            logger.debug("Consent screen didn't appear.")
