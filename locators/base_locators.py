from selenium.webdriver.common.by import By

class BaseLocators:
    RECIPIE_BUTTON_HEADER = (By.XPATH, "//a[@href='/recipes' and contains(text(), 'Рецепты')]")
