import allure
from pages.create_recipe_page import CreateRecipePage
from data.test_data import TestData
from data.test_data import URLs


@allure.feature("Создание рецепта")
class TestCreateRecipe:
    @allure.title("Тест создания рецепта с ингредиентами")
    def test_create_recipe_with_ingredients(self, driver, logged_in_user):
        create_recipe_page = CreateRecipePage(driver)

        create_recipe_page.go_to_create_recipe()
        create_recipe_page.fill_basic_info(
            TestData.RECIPE_NAME,
            TestData.COOKING_TIME,
            TestData.DESCRIPTION
        )
        create_recipe_page.add_ingredients(TestData.INGREDIENTS)
        create_recipe_page.upload_image(TestData.IMAGE_PATH)
        create_recipe_page.create_recipe()

        assert URLs.RECIPES_URL in create_recipe_page.get_current_url()
        assert create_recipe_page.test_recipe_title_displayed() == TestData.RECIPE_NAME
