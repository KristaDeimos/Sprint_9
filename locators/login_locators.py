from selenium.webdriver.common.by import By
from .base_locators import BaseLocators

class LoginLocators(BaseLocators):
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.XPATH, "//form//button[contains(., 'Войти')]")
    LOGIN_FORM = (By.XPATH, "//h1[contains(., 'Войти на сайт')]")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(., 'Выход')]")
