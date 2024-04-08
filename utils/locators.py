from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGO = (By.XPATH, "//a[@class='logo']")
    SIGN_IN_BUTTON = (By.XPATH, "//a[contains(text(), 'Sign In')]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(text(),'Create an Account')]")
    POLICY_CONSENT_CONFIRM_BUTTON = (By.XPATH, "//p[text()='Consent']")


class SignInPageLocators:
    ...


class CreateAccountPageLocators:
    FIRST_NAME_FIELD = (By.XPATH, "//input[@id='firstname']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@id='lastname']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='email_address']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@id='password-confirmation']")
    SUBMIT_FORM_BUTTON = (By.XPATH, "//button[@title='Create an Account']")


class AccountDetailsPageLocators:
    ACCOUNT_CREATED_BANNER = (By.XPATH, "//div[text()='Thank you for registering with Main Website Store.']")
