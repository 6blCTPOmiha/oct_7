import time
from web_pages.homepage import HomePage
from web_pages.product import ProductPage
from web_pages.monitors import MonitorsPage


def test_open_galaxy_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s_6()
    product_page = ProductPage(browser)
    product_page.check_title_is("Samsung galaxy s6")


def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(5)
    monitors = MonitorsPage(browser)
    monitors.check_count(2)
