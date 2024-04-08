from models.client_model import Client
from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestCreateAccount(BaseTest):

    def test_create_account(self):
        home_page = HomePage(self.driver)
        create_account_page = home_page.go_to_create_account_page()
        client: Client = Client("apaw", "muz", "pawmuzd@dssa.com", "Kurczaki1!")
        create_account_page.fill_account_creation_form(client)
        create_account_page.submit_account_creation_form()
#         TODO: validate account creation, implement faker
#       landing on  https://magento.softwaretestingboard.com/customer/account/
#       message = "Thank you for registering with Main Website Store."
#       check ACCOUNT_CREATED_BANNER with message

