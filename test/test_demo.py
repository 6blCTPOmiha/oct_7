import allure
import pytest



@pytest.fixture
def before_after():
    print("\nBefore test")
    yield
    print("\nAfter test")


@allure.feature('true test')
@allure.story('phone')
def test_demo1():
    assert 1 == 1


@allure.feature('error test')
@allure.story('PC')
def test_demo2(before_after):
    assert 2 == 3
