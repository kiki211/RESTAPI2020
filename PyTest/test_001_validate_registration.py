from selenium.webdriver import Chrome

def test_registration_valid_data():
    path =("../chromedriver")
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testing")

