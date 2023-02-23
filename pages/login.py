from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver


    locators = {
        'username':('NAME','username'),
        'password':('NAME','password'),
        'login_btn':('XPATH','//button[@type="submit"]')
    }

    def enter_username(self):
        self.username.set_text("Admin")

    def enter_password(self):
        self.password.set_text("admin123")

    def click_login(self):
        self.login_btn.click()