import allure
from pages.registration_page import RegistrationPage
from data.test_data import URLs
from utils.test_user import generate_test_user


@allure.feature("Регистрация пользователя")
class TestRegistration:
    @allure.title("Тест создания аккаунта")
    def test_create_account(self, driver, generated_test_user):
        registration_page = RegistrationPage(driver)

        registration_page.go_to(URLs.SIGNUP_URL)
        registration_page.is_registration_form_displayed()

        registration_page.register(
            generated_test_user['first_name'],
            generated_test_user['last_name'],
            generated_test_user['username'],
            generated_test_user['email'],
            generated_test_user['password']
        )

        current_url = registration_page.get_current_url()
        assert current_url == URLs.SIGNUP_URL, f"Неверный URL после регистрации: {current_url}"
        assert registration_page.is_login_form_displayed()
