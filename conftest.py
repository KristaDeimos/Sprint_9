import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from utils.test_user import generate_test_user
from data.test_data import URLs, Timeouts


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.set_capability('acceptInsecureCerts', True)

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        desired_capabilities=capabilities,
        options=chrome_options)

    yield driver
    driver.quit()


@pytest.fixture
def generated_test_user(driver):
    return generate_test_user()


@pytest.fixture
def registered_user(driver, generated_test_user):
    registration_page = RegistrationPage(driver)

    registration_page.go_to(URLs.SIGNUP_URL)
    registration_page.register(
        generated_test_user['first_name'],
        generated_test_user['last_name'],
        generated_test_user['username'],
        generated_test_user['email'],
        generated_test_user['password']
    )

    return generated_test_user


@pytest.fixture
def logged_in_user(driver, registered_user):
    login_page = LoginPage(driver)
    login_page.go_to(URLs.SIGNIN_URL)
    login_page.login(registered_user['email'], registered_user['password'])
    login_page.click_login_button()
    login_page.is_element_displayed(login_page.locators.LOGOUT_BUTTON, Timeouts.ELEMENT_TIMEOUT)

    return registered_user
