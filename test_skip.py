import pytest
from selene import browser
from selenium import webdriver

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""


@pytest.fixture(params=[(1280, 720), (1980, 1080), (320, 480), (360, 640)])
def setup_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


def test_github_desktop(setup_browser):
    if browser._config.window_width < 1280:
        pytest.skip('Разрешение браузера для мобильного устройства')
    browser.open("https://github.com/")
    browser.element('a.HeaderMenu-link--sign-in').click()


def test_github_mobile(setup_browser):
    if browser._config.window_width > 1279:
        pytest.skip('Разрешение браузера для декстопной версии')
    browser.open("https://github.com/")
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
