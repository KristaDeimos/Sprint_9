from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://foodgram-frontend-1.prakticum-team.ru/signin")

    login_button = driver.find_element(By.ID, "login-btn")
    login_button.click()

    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("securepassword123")

    submit_button = driver.find_element(By.ID, "submit-btn")
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("home")
    )

    logout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "logout-btn"))
    )
    assert logout_button.is_displayed(), "Кнопка 'Выход' не отображается"

    print("Тест авторизации пройден успешно!")

finally:
    driver.quit()
