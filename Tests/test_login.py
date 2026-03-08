import time

from Pages.login_page import LoginPage

def test_login_title(driver,get_baseurl,get_credentials):
    login = LoginPage(driver)
    login.load(get_baseurl)
    print(get_credentials.get("username"), get_credentials.get("password"), sep=" , ")
    login.login_to_page(get_credentials.get("username"),get_credentials.get("password"))
    time.sleep(5)
    assert "Swag Labs" == driver.title, "url doesn't match"

def test_login_url(driver,get_baseurl,get_credentials):
    login = LoginPage(driver)
    login.load(get_baseurl)
    print(get_credentials.get("username"),get_credentials.get("password"),sep=" , ")
    login.login_to_page(get_credentials.get("username"),get_credentials.get("password"))
    time.sleep(5)
    assert "wrong_url" in driver.current_url, "url doesn't match"
