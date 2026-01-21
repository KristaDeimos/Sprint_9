from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://foodgram-frontend-1.prakticum-team.ru/signin")

    create_button = driver.find_element(By.ID, "create-account-btn")
    create_button.click()

    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("securepassword123")

    submit_button = driver.find_element(By.ID, "submit-btn")
    submit_button.click()

    time.sleep(2)

    assert "login" in driver.current_url.lower(), "Не произошло перехода на страницу авторизации"

    login_form = driver.find_element(By.ID, "login-form")
    assert login_form.is_displayed(), "Форма авторизации не отображается"

    print("Тест пройден успешно!")

finally:
    driver.quit()
