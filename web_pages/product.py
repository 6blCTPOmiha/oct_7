from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, browser):
        self.browser = browser


    def wait_for_page_load(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h2'),
        ))


    def check_title_is(self, title):
        page_title = self.browser.find_element(By.CSS_SELECTOR, "h2")
        assert page_title.text == title
