from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utils.logger import get_logger
from variables import BASE_PAGE_URL

logger = get_logger(__name__)


class BasePage:
    def __init__(self, driver, base_url=BASE_PAGE_URL):
        self.base_url = base_url
        self.driver = driver

    def find_element_with_wait(self, *locator, wait_seconds=10):
        logger.info(f"Looking for element with locator {locator} for {wait_seconds} seconds.")
        self.wait_element(locator, wait_seconds=wait_seconds)
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        logger.info(f"Open URL: {url}")
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def wait_element(self, *locator, wait_seconds=10):
        try:
            logger.info(f"Waiting for element presence {locator} for {wait_seconds} seconds")
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            logger.exception(f"\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {locator[1]}s")
            self.driver.quit()

    def fill_input_field(self, *locator, input_value):
        input_field = self.find_element_with_wait(locator)
        logger.info(f"Clicking on input field and sending input: {input_value}")
        input_field.click()
        input_field.clear()
        input_field.send_keys(input_value)
