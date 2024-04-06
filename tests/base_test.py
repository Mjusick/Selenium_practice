import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from variables import BASE_PAGE_URL


class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(BASE_PAGE_URL)

    def tearDown(self):
        self.driver.close()
