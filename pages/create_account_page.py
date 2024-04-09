from models.client_model import Client
from pages.base_page import BasePage
from utils.locators import CreateAccountPageLocators
from utils.logger import get_logger

logger = get_logger(__name__)


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        self.locators = CreateAccountPageLocators()
        super().__init__(driver)

    def fill_account_creation_form(self, client: Client):
        self.fill_input_field(self.locators.FIRST_NAME_FIELD, input_value=client.first_name)
        self.fill_input_field(self.locators.LAST_NAME_FIELD, input_value=client.last_name)
        self.fill_input_field(self.locators.EMAIL_FIELD, input_value=client.email)
        self.fill_input_field(self.locators.PASSWORD_FIELD, input_value=client.password)
        self.fill_input_field(self.locators.CONFIRM_PASSWORD_FIELD, input_value=client.password)

    def submit_account_creation_form(self):
        logger.info("Submitting account creation form.")
        submit_form_button = self.find_element_with_wait(self.locators.SUBMIT_FORM_BUTTON)
        submit_form_button.click()
