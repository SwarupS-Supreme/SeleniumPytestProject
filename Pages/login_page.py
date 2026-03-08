# from base_page import BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID,"login-button")

    def load(self,get_baseurl: str):
        self.open(get_baseurl)

    def login_to_page(self,username:str, password:str):
        self.type(self.USERNAME,username)
        self.type(self.PASSWORD,password)
        self.click(self.LOGIN_BTN)



