import allure
from web_pages.homepage import HomePage
from web_pages.product import ProductPage
from web_pages.monitors import MonitorsPage


@allure.feature('side site')
@allure.story('phone')
def test_open_galaxy_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s_6()
    product_page = ProductPage(browser)
    product_page.check_title_is("Samsung galaxy s6")


@allure.feature('side site')
@allure.story('PC')
def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    monitors = MonitorsPage(browser)
    monitors.wait_for_page_load()
    monitors.check_count(2)
