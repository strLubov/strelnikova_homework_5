import pytest
from selene import browser


@pytest.fixture()
def browser_setup():
    browser.config.window_width = 1080
    browser.config.window_height = 1440
    browser.config.base_url = 'https://demoqa.com'
