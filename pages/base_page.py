from pathlib import Path
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data.test_data import Timeouts, URLs
from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = URLs.BASE_URL
        self.wait = WebDriverWait(driver, Timeouts.PAGE_TIMEOUT)

    def _allure_step(self, step_name, action, *args, **kwargs):

        with allure.step(step_name):
            return action(*args, **kwargs)

    def find_element(self, locator, timeout=Timeouts.ELEMENT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=Timeouts.ELEMENT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator, step_name=None):
        if step_name:
            return self._allure_step(step_name, self._click_element, locator)
        else:
            return self._click_element(locator)

    def _click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text, step_name=None):
        if step_name:
            return self._allure_step(step_name, self._send_keys, locator, text)
        else:
            return self._send_keys(locator, text)

    def _send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_element_displayed(self, locator, timeout=Timeouts.ELEMENT_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def wait_for_element_visible(self, locator, timeout=Timeouts.ELEMENT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def go_to(self, path=""):
        url = path
        self.driver.get(url)

        WebDriverWait(self.driver, Timeouts.PAGE_TIMEOUT).until(
            EC.presence_of_element_located(BaseLocators.RECIPIE_BUTTON_HEADER)
        )

    def get_current_url(self):
        return self.driver.current_url
