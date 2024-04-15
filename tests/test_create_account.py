from models.client_model import Client
from pages.account_details_page import AccountDetailsPage
from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestCreateAccount(BaseTest):

    def test_create_account(self):
        home_page = HomePage(self.driver)
        create_account_page = home_page.go_to_create_account_page()
        client: Client = Client("sample_name", "sample_last_name", "testowy@testy.com", "Test123!")
        create_account_page.fill_account_creation_form(client)
        create_account_page.submit_account_creation_form()
        account_details_page = AccountDetailsPage(self.driver)
        self.assertEqual(self.driver.current_url, "https://magento.softwaretestingboard.com/customer/account/")
        self.assertEqual(account_details_page.get_account_creation_confirmation_message(), "Thank you for registering "
                                                                                           "with Main Website Store.")

