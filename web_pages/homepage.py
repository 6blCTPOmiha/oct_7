from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get("https://demoblaze.com")


    def click_galaxy_s_6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, '''//a[text()="Samsung galaxy s6"]''')
        galaxy_s6.click()


    def click_monitor(self):
        monitor = self.browser.find_element(By.XPATH, '''//a[text()="Monitors"]''')
        monitor.click()


