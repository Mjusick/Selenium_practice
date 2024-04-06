from pages.home_page import HomePage
from tests.base_test import BaseTest
from utils.logger import get_logger

logger = get_logger(__name__)


class TestPageLoaded(BaseTest):

    def test_page_load(self):
        logger.info("Home Page load test started...")
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.check_logo_appearance())
        logger.info("Page loaded successfully.")
