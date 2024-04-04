from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestPageLoaded(BaseTest):

    def test_page_load(self):
        print("Check if page is loaded.")
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.check_page_loaded())
