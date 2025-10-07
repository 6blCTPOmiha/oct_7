from selenium.webdriver.common.by import By


class MonitorsPage:
    def __init__(self, browser):
        self.browser = browser


    def check_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count
