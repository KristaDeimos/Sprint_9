from selenium.webdriver.common.by import By
from .base_locators import BaseLocators


class CreateRecipeLocators(BaseLocators):
    # Основные локаторы формы создания рецептов
    RECIPE_NAME_INPUT = (By.XPATH, "//label[.//div[contains(text(), 'Название рецепта')]]//input")
    COOKING_TIME_INPUT = (By.XPATH, "//label[.//div[contains(text(), 'Время приготовления')]]//input")
    DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, "textarea[class*='styles_textareaField']")
    IMAGE_UPLOAD = (By.CSS_SELECTOR, "input[class*=styles_fileInput][type='file']")
    CREATE_BUTTON = (By.CSS_SELECTOR, "button[class*=style_button]")

    # Локаторы для ингредиентов

    INGREDIENT_NAME_INPUT = (By.CSS_SELECTOR, "input[class*=styles_ingredientsInput]")
    INGREDIENT_AMOUNT_INPUT = (By.CSS_SELECTOR, "input[class*=styles_ingredientsAmountValue]")
    ADD_INGREDIENT_BUTTON = (By.CSS_SELECTOR, "[class*='styles_ingredientAdd']")

    # Кнопка когда она активна
    CREATE_BUTTON_ACTIVE = (By.CSS_SELECTOR, "button[class*=style_button]:not([disabled])")

    # Теги
    TAGS_CONTAINER = (By.XPATH, "//div[contains(@class, 'checkboxGroup')]")
    TAG_BUTTONS = (By.XPATH, "//div[contains(@class, 'checkboxGroup')]//button")
    ACTIVE_TAG = (By.XPATH, "//button[contains(@class, 'checkbox_active')]")

    # Выпадающий список ингредиентов
    INGREDIENT_DROPDOWN_CONTAINER = (By.CSS_SELECTOR, "[class*='styles_container__']")
    INGREDIENT_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, "[class*='styles_container__'] > div")
    FIRST_DROPDOWN_OPTION = (By.CSS_SELECTOR, "[class*='styles_container__'] > div:first-child")

    # Название рецепта
    RECIPE_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_single-card__title') and contains(text(), 'Сливочное Пиво')]")
