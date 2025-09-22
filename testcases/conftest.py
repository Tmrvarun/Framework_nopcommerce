from selenium import webdriver
import pytest



# @pytest.fixture()
# def setup(): #Basic Chrome setup to initiate chrome driver
#   driver=webdriver.chrome()
#   return driver

@pytest.fixture()
def setup(browser):# Modified -this setup method is used in test case , to choose a driver eg. chrome, ie , FF
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie() #if we do not pass any value in browser then it should be default IE
    return driver


def pytest_addoption(parser): #this will get the value of browser from CLI/HOOK
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):# This will put the value of browser from parser to the setup fixture above
    return request.config.getoption("--browser")