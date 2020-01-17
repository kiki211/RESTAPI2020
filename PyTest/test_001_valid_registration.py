from selenium.webdriver import Chrome



def test_registartion_valid():
    path = "/usr/local/bin/chromedriver"

    driver = Chrome(executable_path=path)

    driver.get('http://www.thetestingworld.com/testings')