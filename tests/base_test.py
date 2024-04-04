import logging
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.selenium_manager import SeleniumManager

from variables import BASE_PAGE_URL

logger = logging.getLogger()


class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(BASE_PAGE_URL)
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('app.log')
        logger.addHandler(file_handler)

    def tearDown(self):
        self.driver.close()
