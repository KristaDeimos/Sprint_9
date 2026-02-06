from selenium.webdriver.common.by import By
from .base_locators import BaseLocators

class RegistrationLocators(BaseLocators):
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='first_name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='last_name']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//form//button[contains(., 'Создать аккаунт')]")
    REGISTRATION_FORM = (By.XPATH, "//h1[contains(., 'Регистрация')]")
    LOGIN_FORM = (By.XPATH, "//h1[contains(., 'Войти на сайт')]")
