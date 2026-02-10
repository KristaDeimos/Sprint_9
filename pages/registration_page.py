import allure
from pages.base_page import BasePage
from locators.registration_locators import RegistrationLocators


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RegistrationLocators()

    def fill_first_name(self, first_name):
        self.send_keys(self.locators.FIRST_NAME_INPUT, first_name, "Ввод имени")

    def fill_last_name(self, last_name):
        self.send_keys(self.locators.LAST_NAME_INPUT, last_name, "Ввод фамилии")

    def fill_username(self, username):
        self.send_keys(self.locators.USERNAME_INPUT, username, "Ввод username")

    def fill_email(self, email):
        self.send_keys(self.locators.EMAIL_INPUT, email, "Ввод email")

    def fill_password(self, password):
        self.send_keys(self.locators.PASSWORD_INPUT, password, "Ввод пароля")

    def click_create_account_button(self):
        self.click_element(self.locators.CREATE_ACCOUNT_BUTTON, "Нажатие кнопки создания аккаунта")

    def is_registration_form_displayed(self):
        with allure.step("Проверка отображения формы регистрации"):
            return self.is_element_displayed(self.locators.REGISTRATION_FORM)

    def is_login_form_displayed(self):
        with allure.step("Проверка отображения формы входа"):
            return self.is_element_displayed(self.locators.LOGIN_FORM)

    def register(self, first_name, last_name, username, email, password):
        with allure.step("Заполнение формы регистрации"):
            self.fill_first_name(first_name)
            self.fill_last_name(last_name)
            self.fill_username(username)
            self.fill_email(email)
            self.fill_password(password)
            self.click_create_account_button()

