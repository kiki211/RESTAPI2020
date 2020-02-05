from selenium.webdriver import Chrome
import pytest

@pytest.fixture(scope="module")
def setPath():
    global driver
    path = "/usr/local/bin/chromedriver"
    driver = Chrome(executable_path=path)
    yield
    #driver.close()


a = 100
@pytest.mark.skipif(a > 100, reason="Don't executing on current build")
def test_registartion_valid(setPath):
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()
    assert driver.title == "Login & Sign Up Forms"

@pytest.mark.Sanity
def test_invalid(setPath):
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()
    assert driver.current_url == "https://www.thetestingworld.com/testings/"

@pytest.mark.Smoke
def test_registartion_invalid(setPath):
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()



