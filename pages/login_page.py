from selenium.webdriver.common.by import By
from .base_page import BasePage


class AuthPage(BasePage):
    
    # Локаторы
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    AUTH_FORM = (By.CLASS_NAME, "form__container")
    ERROR_MESSAGE = (By.CLASS_NAME, "form__error")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.open("/signin")
    
    def is_auth_form_displayed(self):
        return self.is_element_displayed(self.AUTH_FORM)
    
    def login(self, email, password):
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
    
    def go_to_registration(self):
        self.click_element(self.REGISTER_LINK)
    
    def is_logged_in(self):
        try:
            self.wait_for_url_contains("/")
            return self.is_element_displayed(self.LOGOUT_BUTTON)
        except:
            return False
    
    def get_error_message(self):
        if self.is_element_displayed(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
