from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = "https://foodgram-frontend-1.prakticum-team.ru"
    
    def open(self, url=""):
        self.driver.get(f"{self.base_url}{url}")
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def is_element_displayed(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
    
    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))
