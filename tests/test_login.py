import allure
from pages.login_page import LoginPage
from data.test_data import URLs


@allure.feature("Авторизация пользователя")
class TestLogin:
    @allure.title("Тест авторизации")
    def test_login(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.go_to(URLs.SIGNIN_URL)
        login_page.login(registered_user['email'], registered_user['password'])

        assert login_page.is_logout_button_displayed(), "Авторизация не прошла успешно"
        assert login_page.get_current_url() == URLs.RECIPES_URL, "Не перешли на главную страницу"
