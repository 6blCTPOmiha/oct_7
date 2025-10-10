import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.wait = WebDriverWait(browser, 10)
    browser.maximize_window()
    yield browser
