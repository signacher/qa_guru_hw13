"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture(params=[((1280, 720), (320, 480), (1980, 1080), (360, 640))])
def setup_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    yield browser
    browser.quit()

@pytest.mark.parametrize("setup_browser", [(1280, 720), (1980, 1080)], indirect=True)
def test_github_desktop(setup_browser):
    browser.open('https://github.com/')
    browser.element('a.HeaderMenu-link--sign-in').click()

@pytest.mark.parametrize("setup_browser", [(320, 480), (360, 640)], indirect=True)
def test_github_mobile(setup_browser):
    browser.open('https://github.com/')
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
