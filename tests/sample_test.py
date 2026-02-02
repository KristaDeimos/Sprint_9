import pytest


def test_simple():
    """Простой тест для проверки работы pytest"""
    assert 1 + 1 == 2


def test_with_fixture(driver):
    """Тест с фикстурой driver"""
    driver.get("https://google.com")
    assert "Google" in driver.title
    print(f"Title: {driver.title}")
