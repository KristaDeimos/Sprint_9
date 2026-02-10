from pathlib import Path

class TestData:
    RECIPE_NAME = "Сливочное Пиво"
    INGREDIENTS = {
        "сливочное масло": "100",
        "сливки": "1"
    }
    COOKING_TIME = "30"
    DESCRIPTION = "Это тестовый рецепт сливочного пива созданный автоматизированным тестом"
    IMAGE_PATH = str(Path(__file__).parent.parent / "assets" / "butterbeer.png")


class URLs:
    BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru"
    RECIPES_URL = f"{BASE_URL}/recipes"
    SIGNIN_URL = f"{BASE_URL}/signin"
    SIGNUP_URL = f"{BASE_URL}/signup"
    CREATE_RECIPIE_URL = f"{RECIPES_URL}/create"

class Timeouts:
    ELEMENT_TIMEOUT = 15
    PAGE_TIMEOUT = 20
