from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome("../drivers/chromedriver")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to set up method
    return request.config.getoption("--browser")
