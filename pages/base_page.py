import logging

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from variables import BASE_PAGE_URL

logger = logging.getLogger()


class BasePage:
    def __init__(self, driver, base_url=BASE_PAGE_URL):
        self.base_url = base_url
        self.driver = driver

    def find_element(self, *locator):
        logger.debug(f"Looking for element with locator {locator}")
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        logger.debug(f"Open URL: {url}")
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def wait_element(self, *locator):
        try:
            wait_seconds = 10
            logger.debug(f"Waiting for element presence {locator} for {wait_seconds} seconds")
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            print(f"\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {locator[1]}s")
            self.driver.quit()
