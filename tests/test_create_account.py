from models.client_model import Client
from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestCreateAccount(BaseTest):

    def test_create_account(self):
        home_page = HomePage(self.driver)
        create_account_page = home_page.go_to_create_account_page()
        client: Client = Client("paw", "muz", "pawmuz@dss.com", "Kurczaki1!")
        create_account_page.fill_input_field(client)
        create_account_page.submit_account_creation_form()


