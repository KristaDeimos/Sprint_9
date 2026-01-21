import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_create_recipe(driver):

    driver.get("https://foodgram-frontend-1.prakticum-team.ru/signin")
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("securepassword123")
    driver.find_element(By.ID, "submit-btn").click()

    create_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "create-recipe-tab"))
    )
    create_tab.click()

    recipe_name = "Тестовый рецепт"
    driver.find_element(By.NAME, "title").send_keys(recipe_name)
    driver.find_element(By.NAME, "description").send_keys("Описание тестового рецепта")
    driver.find_element(By.NAME, "steps").send_keys("Шаг 1: сделать то-то")

    ingredient_input = driver.find_element(By.NAME, "ingredient")
    ingredient_input.send_keys("Молоко")

    ingredient_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".ingredient-option"))
    )
    ingredient_option.click()

    driver.find_element(By.ID, "create-btn").click()

    recipe_card = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".recipe-card"))
    )
    assert recipe_card.is_displayed(), "Карточка рецепта не отображается"

    card_title = recipe_card.find_element(By.CSS_SELECTOR, ".recipe-title").text
    assert card_title == recipe_name, f"Название рецепта не совпадает: {card_title}"
