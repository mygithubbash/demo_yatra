import time
import pytest
from pytest import fixture
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    #if browser == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #else:
        #print('Invalid browser')
    driver.get('https://www.yatra.com/')
    driver.maximize_window()
    ac = ActionChains(driver)
    request.cls.driver=driver
    request.cls.ac = ac
    time.sleep(2)
    yield
    driver.close()
    #def pytest_addoption(parser):
        #parser.addopion("--browser")

    #@pytest.fixture(scope='class', autouse=True)
    #def browser(request):
        #return request.config.getoption("--browser")