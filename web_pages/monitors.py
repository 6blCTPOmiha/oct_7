from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MonitorsPage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_page_load(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[src="imgs/asusm.jpg"]'),
        ))

    def check_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count
