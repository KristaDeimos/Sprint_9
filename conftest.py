import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия драйвера Chrome"""
    
    chrome_options = Options()
    
    # Обязательные опции для Docker/контейнеров
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-setuid-sandbox")
    
    # Дополнительные опции для стабильности
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    # Отключаем уведомления
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    
    # Явно отключаем сборщик мусора
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    # Используем Chrome в контейнере
    try:
        # Вариант 1: Используем Selenium 4+ с автоматическим управлением драйвером
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"Ошибка при создании драйвера (вариант 1): {e}")
        
        try:
            # Вариант 2: Явно указываем путь к chromedriver
            chrome_options.binary_location = "/usr/bin/google-chrome"
            
            # Проверяем существование chromedriver
            chromedriver_path = "/usr/local/bin/chromedriver"
            if os.path.exists(chromedriver_path):
                service = Service(executable_path=chromedriver_path)
                driver = webdriver.Chrome(service=service, options=chrome_options)
            else:
                # Вариант 3: Используем Selenium Manager (автоматическая загрузка драйвера)
                from selenium.webdriver.chrome.service import Service as ChromeService
                from webdriver_manager.chrome import ChromeDriverManager
                
                service = ChromeService(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=service, options=chrome_options)
                
        except Exception as e2:
            print(f"Ошибка при создании драйвера (вариант 2): {e2}")
            raise
    
    driver.implicitly_wait(10)
    yield driver
    
    # Закрытие драйвера
    try:
        driver.quit()
    except:
        pass
