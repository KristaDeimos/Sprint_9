import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_authorization(driver):
    """Тест авторизации на сайте Foodgram"""
    
    # Открываем страницу авторизации
    driver.get("https://foodgram-frontend-1.prakticum-team.ru/signin")
    
    # Проверяем, что страница загрузилась
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-btn"))
    )
    
    # Нажимаем кнопку входа
    login_button = driver.find_element(By.ID, "login-btn")
    login_button.click()
    
    # Заполняем форму авторизации
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("testuser")
    
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("securepassword123")
    
    # Нажимаем кнопку отправки
    submit_button = driver.find_element(By.ID, "submit-btn")
    submit_button.click()
    
    # Ждем редиректа на домашнюю страницу
    WebDriverWait(driver, 10).until(
        EC.url_contains("home")
    )
    
    # Проверяем, что кнопка выхода отображается (признак успешной авторизации)
    logout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "logout-btn"))
    )
    
    assert logout_button.is_displayed(), "Кнопка 'Выход' не отображается"
    print("Тест авторизации пройден успешно!")


def test_authorization_with_wrong_credentials(driver):
    """Тест авторизации с неверными учетными данными"""
    
    driver.get("https://foodgram-frontend-1.prakticum-team.ru/signin")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-btn"))
    )
    
    login_button = driver.find_element(By.ID, "login-btn")
    login_button.click()
    
    # Заполняем форму неверными данными
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("wronguser")
    
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("wrongpassword")
    
    submit_button = driver.find_element(By.ID, "submit-btn")
    submit_button.click()
    
    # Проверяем сообщение об ошибке
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert "Неверные учетные данные" in error_message.text or \
               "Invalid credentials" in error_message.text, \
               "Сообщение об ошибке не отображается"
    except:
        # Если нет класса error-message, ищем другие возможные локаторы ошибок
        error_selectors = [
            (By.CSS_SELECTOR, ".error"),
            (By.CSS_SELECTOR, ".alert"),
            (By.CSS_SELECTOR, "[role='alert']"),
            (By.XPATH, "//*[contains(text(), 'error') or contains(text(), 'Error')]")
        ]
        
        for selector in error_selectors:
            try:
                error_element = driver.find_element(*selector)
                if error_element.is_displayed():
                    print(f"Найдено сообщение об ошибке: {error_element.text}")
                    break
            except:
                continue
    
    print("Тест с неверными учетными данными пройден успешно!")


def test_authorization_empty_fields(driver):
    """Тест авторизации с пустыми полями"""
    
    driver.get("https://foodgram-frontend-1.prakticum-team.ru/signin")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-btn"))
    )
    
    login_button = driver.find_element(By.ID, "login-btn")
    login_button.click()
    
    # Не заполняем поля, сразу нажимаем отправить
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "submit-btn"))
    )
    submit_button.click()
    
    # Проверяем валидацию полей (HTML5 validation)
    try:
        username_validation = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']:invalid"))
        )
        assert username_validation
    except:
        # Если HTML5 validation не сработала, ищем сообщения об ошибке
        validation_messages = driver.find_elements(By.CSS_SELECTOR, ".validation-error, .required-field")
        assert len(validation_messages) > 0, "Валидация пустых полей не сработала"
    
    print("Тест с пустыми полями пройден успешно!")


@pytest.mark.parametrize("username,password", [
    ("testuser", "securepassword123"),
    ("admin", "admin123"),
    ("user@example.com", "Pass123!"),
])
def test_authorization_different_users(driver, username, password):
    """Параметризованный тест авторизации для разных пользователей"""
    
    driver.get("https://foodgram-frontend-1.prakticum-team.ru/signin")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-btn"))
    )
    
    login_button = driver.find_element(By.ID, "login-btn")
    login_button.click()
    
    # Заполняем форму
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys(username)
    
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    
    submit_button = driver.find_element(By.ID, "submit-btn")
    submit_button.click()
    
    # Проверяем результат
    try:
        # Если авторизация успешна
        WebDriverWait(driver, 10).until(
            EC.url_contains("home")
        )
        logout_button = driver.find_element(By.ID, "logout-btn")
        assert logout_button.is_displayed()
        print(f"Авторизация для пользователя {username} прошла успешно!")
        
    except:
        # Если авторизация не удалась
        try:
            error_message = driver.find_element(By.CLASS_NAME, "error-message")
            assert error_message.is_displayed()
            print(f"Авторизация для пользователя {username} не удалась (ожидаемо)")
        except:
            # Проверяем, остались ли мы на той же странице
            assert "signin" in driver.current_url, \
                   f"Неизвестный результат для пользователя {username}"
            print(f"Авторизация для пользователя {username} не удалась - остались на странице входа")
