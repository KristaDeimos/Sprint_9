import allure
from data.test_data import URLs
from pages.base_page import BasePage
from locators.create_recipe_locators import CreateRecipeLocators


class CreateRecipePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CreateRecipeLocators()

    def go_to_create_recipe(self):
        with allure.step("Переход на страницу создания рецепта"):
            self.go_to(URLs.CREATE_RECIPIE_URL)

    def fill_basic_info(self, name, cooking_time, description):
        with allure.step("Заполнение основных полей формы"):
            self.send_keys(self.locators.RECIPE_NAME_INPUT, name, "Ввод названия рецепта")
            self.send_keys(self.locators.COOKING_TIME_INPUT, cooking_time, "Ввод времени приготовления")
            self.send_keys(self.locators.DESCRIPTION_TEXTAREA, description, "Ввод описания")

    def add_ingredients(self, ingredients_dict=None):
        with allure.step("Добавление ингредиентов"):
            for name, amount in ingredients_dict.items():
                self.add_single_ingredient(name, amount)
                add_button = self.find_element(self.locators.ADD_INGREDIENT_BUTTON)
                add_button.click()

    def add_single_ingredient(self, name, amount):
        with allure.step(f"Добавление ингредиента: {name} - {amount}"):
            name_input = self.find_element(self.locators.INGREDIENT_NAME_INPUT)
            amount_input = self.find_element(self.locators.INGREDIENT_AMOUNT_INPUT)

            name_input.clear()
            name_input.send_keys(name)

            self.wait_and_select_first_option()

            amount_input.clear()
            amount_input.send_keys(amount)

    def upload_image(self, image_path):
        with allure.step("Загрузка изображения"):
            image_input = self.find_element(self.locators.IMAGE_UPLOAD)
            image_path_absolute = image_path
            image_input.send_keys(image_path_absolute)

    def create_recipe(self):
        with allure.step("Создание рецепта"):
            self.click_element(self.locators.CREATE_BUTTON, "Нажатие кнопки создания рецепта")

    def test_recipe_title_displayed(self):
        with allure.step("Проверка названия созданного рецепта"):
            title_element = self.wait_for_element_visible(self.locators.RECIPE_TITLE)
            return title_element.text

    def wait_for_ingredient_dropdown(self):
        return self.wait_for_element_visible(self.locators.INGREDIENT_DROPDOWN_CONTAINER)

    def select_first_dropdown_option(self):
        first_option = self.find_element(self.locators.FIRST_DROPDOWN_OPTION)
        first_option.click()
        return first_option

    def wait_and_select_first_option(self):
        self.wait_for_ingredient_dropdown()
        return self.select_first_dropdown_option()

