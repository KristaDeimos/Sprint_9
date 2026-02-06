import allure
from .base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators()

    def fill_email(self, email):
        self.send_keys(self.locators.EMAIL_INPUT, email, "Ввод email")

    def fill_password(self, password):
        self.send_keys(self.locators.PASSWORD_INPUT, password, "Ввод пароля")

    def click_login_button(self):
        self.click_element(self.locators.LOGIN_BUTTON, "Нажатие кнопки входа")

    def login(self, email, password):
        with allure.step("Авторизация пользователя"):
            self.fill_email(email)
            self.fill_password(password)
            self.click_login_button()

    def is_logout_button_displayed(self):
        with allure.step("Проверка отображения кнопки Выхода"):
            return self.is_element_displayed(self.locators.LOGOUT_BUTTON)
